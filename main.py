import os

def criar_arquivo_entrada(arquivo):
    if not os.path.exists(arquivo):
        with open(arquivo, 'w', encoding='utf-8') as file:
            file.write("Exemplo de texto para contar palavras. Palavra palavra Palavra palavra.")
            print("Arquivo de entrada criado:", arquivo)

def contar_palavras(arquivo):
    contagem = {}
    with open(arquivo, 'r', encoding='utf-8') as file:
        for linha in file:
            palavras = linha.split()
            for palavra in palavras:
                palavra = palavra.strip('.,!?;:').lower()
                contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

def escrever_resultados(contagem, arquivo_saida):
    with open(arquivo_saida, 'w', encoding='utf-8') as file:
        palavras_ordenadas = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
        for palavra, ocorrencias in palavras_ordenadas:
            file.write(f"{palavra}: {ocorrencias}\n")

arquivo_entrada = "texto.txt"
arquivo_saida = "resultados.txt"

criar_arquivo_entrada(arquivo_entrada)

contagem_palavras = contar_palavras(arquivo_entrada)

escrever_resultados(contagem_palavras, arquivo_saida)

print("Resultados foram escritos no arquivo:", arquivo_saida)