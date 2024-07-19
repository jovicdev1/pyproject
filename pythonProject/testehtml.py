import docx2txt

# Lê o conteúdo do documento Word
caminho_arquivo = r"C:\Users\joao.ribeiro\OneDrive - Edições CNBB\Desktop\Termo de Devolução de Bem.docx"
conteudo_docx = docx2txt.process(caminho_arquivo)

# Salva o conteúdo em um arquivo HTML
with open("termo.html", "w", encoding="utf-8") as arquivo_html:
    arquivo_html.write(conteudo_docx)