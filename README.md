# 📊 Financial Reports Converter - Conversor de Relatórios Financeiros
*(Versão em Português abaixo)*

Professional tool designed to automate the extraction of tabular data from financial PDF reports. It processes raw PDF documents, cleans complex string-based currencies, intelligently filters out redundant headers, and generates a structured, ready-to-use Excel spreadsheet.

---

## 🏆 Business Impact & Results

* **Efficiency & Speed:** Replaces the tedious manual task of reading PDFs and typing data into Excel. What used to take hours of manual data entry is now done in **seconds**.
* **Data Accuracy:** Eliminates human error in transcribing numbers, avoiding critical financial mistakes caused by typos.
* **Operational Relief:** Frees up the financial/administrative team to focus on data analysis rather than data extraction.
* **Standardization:** Automatically standardizes Brazilian currency strings into machine-readable numbers, ensuring the final file is ready for formulas and pivots.

---

## 🚀 Key Features

* **Bulk Upload:** Upload and process multiple PDF files simultaneously.
* **Automated Filtering:** Smartly identifies and excludes irrelevant rows, such as repeated page headers, footers, and totals.
* **Currency Normalization:** Cleans strings like "R$ 1.000,00" and converts them directly into float values like "1000.00".
* **Live Web Preview:** Displays the extracted and formatted DataFrame directly on the screen before downloading.
* **In-Memory Export:** Uses buffer technology to generate the final `.xlsx` file on the fly, ensuring fast downloads without cluttering the server's local storage.

---

## 🛠️ Tech Stack

* **Python:** Core processing.
* **Streamlit:** Web interface.
* **Pandas:** Data manipulation and structuring.
* **pdfplumber:** High-precision PDF table extraction.
* **XlsxWriter:** In-memory Excel file generation engine.

---
---

# 📊 Conversor de Relatórios Financeiros (PT-BR)

Ferramenta profissional desenvolvida para automatizar a extração de dados tabulares de relatórios financeiros específicos em PDF. O sistema processa documentos brutos, limpa valores monetários complexos, filtra cabeçalhos repetitivos de forma inteligente e gera uma planilha Excel estruturada e pronta para uso.

---

## 🏆 Resultados e Impacto no Negócio

* **Eficiência e Velocidade:** Substitui o trabalho tedioso de ler PDFs e digitar os dados no Excel. O que levava horas de digitação manual agora é feito em **segundos**.
* **Precisão de Dados:** Elimina erros humanos na transcrição de números, evitando falhas financeiras críticas causadas por erros de digitação.
* **Alívio Operacional:** Libera a equipe financeira/administrativa para focar na análise dos dados em vez de perder tempo com extração.
* **Padronização:** Padroniza automaticamente textos de moeda brasileira para números reais, garantindo que o arquivo final já venha pronto para fórmulas e tabelas dinâmicas.

---

## 🚀 Funcionalidades Principais

* **Upload em Massa:** Suporte para envio e processamento de múltiplos arquivos PDF simultâneos.
* **Filtragem Automática:** Identifica e exclui de forma inteligente linhas irrelevantes, como cabeçalhos repetidos de páginas, rodapés e totais.
* **Normalização de Moeda:** Limpa textos como "R$ 1.000,00" e os converte diretamente para valores numéricos como "1000.00".
* **Pré-visualização Web:** Exibe o DataFrame extraído e formatado diretamente na tela antes de realizar o download.
* **Exportação em Memória:** Utiliza tecnologia de buffer para gerar o arquivo `.xlsx` final em tempo real, garantindo downloads rápidos sem ocupar espaço no disco do servidor.

---

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem base.
* **Streamlit:** Interface web.
* **Pandas:** Estruturação e manipulação de dados.
* **pdfplumber:** Extração de tabelas em PDF com alta precisão.
* **XlsxWriter:** Motor de geração de arquivos Excel em memória.
