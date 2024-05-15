  import csv

  def abrir_csv(nome_do_arquivo):
      try:
          with open(nome_do_arquivo, 'r') as csv_arquivo:
              leitor_csv = csv.reader(csv_arquivo)
              for linha in leitor_csv:
                  print(linha)
      except FileNotFoundError:
          print("O arquivo não pôde ser encontrado.")

  nome_do_arquivo_csv = "dados.csv"
  abrir_csv(nome_do_arquivo_csv)