import csv
import json

def converter_csv_para_json(arquivo_csv, arquivo_json):
    # Abrindo o arquivo CSV para leitura
    with open(arquivo_csv, 'r') as arquivo:
        # Lendo os dados do arquivo CSV
        leitor_csv = csv.DictReader(arquivo)
        # Convertendo os dados para uma lista de dicionários
        dados = [linha for linha in leitor_csv]

    # Escrevendo os dados em um arquivo JSON
    with open(arquivo_json, 'w') as arquivo:
        # Utilizando a biblioteca json para escrever os dados no arquivo JSON
        json.dump(dados, arquivo, indent=4)

arquivo_csv = 'dados.csv'
arquivo_json = 'dados.json'

converter_csv_para_json(arquivo_csv, arquivo_json)
