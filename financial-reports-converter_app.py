import streamlit as st
import pdfplumber
import pandas as pd
import io

st.set_page_config(page_title="Extrator de Receitas PDF", page_icon="📄")
st.title("📄 Conversor de PDF para Excel")
st.write("Faça o upload do seu relatório em PDF para extrair as tabelas e baixar em Excel.")

def limpar_moeda(valor):
    if not isinstance(valor, str):
        return valor
    limpo = valor.replace('R$', '').strip()
    limpo = limpo.replace('.', '').replace(',', '.')
    try:
        return float(limpo)
    except ValueError:
        return 0.0

arquivos_pdf = st.file_uploader("Arraste e solte seus PDFs aqui", type=["pdf"], accept_multiple_files=True)

if arquivos_pdf:
    for arquivo in arquivos_pdf:
        st.subheader(f"Processando: {arquivo.name}")
        dados_arquivo = []
        
        with st.spinner('Lendo o PDF e extraindo tabelas...'):
            with pdfplumber.open(arquivo) as pdf:
                for page in pdf.pages:
                    tabela = page.extract_table()
                    
                    if tabela:
                        for linha in tabela:
                            if not linha or linha[0] is None:
                                continue
                                
                            texto_col0 = str(linha[0]).strip()
                            
                            termos_ignorar = ["Quadra", "Relatório", "Total", "Página", "FILTROS", "RESULTADO"]
                            if any(termo in texto_col0 for termo in termos_ignorar):
                                continue
                            
                            dados_arquivo.append(linha)

        if dados_arquivo:
            df = pd.DataFrame(dados_arquivo)
            
            try:
                df.iloc[:, -1] = df.iloc[:, -1].apply(limpar_moeda) 
                df.iloc[:, -2] = df.iloc[:, -2].apply(limpar_moeda) 
                df.iloc[:, -3] = df.iloc[:, -3].apply(limpar_moeda) 
                
                colunas_map = {
                    0: 'Quadra',
                    1: 'Lote/Dados', 
                    df.columns[-1]: 'Valor Pago (R$)',
                    df.columns[-2]: 'Multa/Juros (R$)',
                    df.columns[-3]: 'Valor Original (R$)'
                }
                df.rename(columns=colunas_map, inplace=True)
                
            except Exception as e:
                st.warning(f"Aviso: Não foi possível formatar colunas de valores automaticamente. O Excel conterá texto bruto. Erro: {e}")

            st.success("Tabela extraída com sucesso! Confira a prévia abaixo:")
            st.dataframe(df, use_container_width=True)

            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Receitas')
            
            nome_excel = arquivo.name.replace(".pdf", ".xlsx")
            
            st.download_button(
                label="📥 Baixar Planilha Excel",
                data=buffer.getvalue(),
                file_name=nome_excel,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            st.divider() 
            
        else:
            st.warning(f"Nenhuma tabela encontrada no arquivo {arquivo.name}.")