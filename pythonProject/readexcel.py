import pandas as pd

# Read the excel file

caminho_arquivo = r"C:\\Users\\joao.ribeiro\\OneDrive - Edições CNBB\\CONTROLE DE SATISFAÇÃO.xlsx"

df = pd.read_excel('CONTROLE DE SATISFAÇÃO.xlsx')

print(df)