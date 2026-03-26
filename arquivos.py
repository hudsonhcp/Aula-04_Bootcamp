#%%
import csv

caminho_arquivo: str = "exemplo.csv"

arquivo_csv: list = list()

with open(file = caminho_arquivo, mode = "r", encoding = "utf-8") as arquivo:
    
    leitor_csv = csv.DictReader(arquivo)

    for l in leitor_csv:
        arquivo_csv.append(l)

for a in arquivo_csv:
    print(a)