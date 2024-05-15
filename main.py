def converter_listas_para_dict(chaves, valores):
  return dict(zip(chaves, valores))

def principal():
  entrada_chaves = input("Insira as chaves separadas por espaços: ")
  chaves = entrada_chaves.split()

  entrada_valores = input("Insira os valores separados por espaços: ")
  valores = entrada_valores.split()

  if len(chaves) != len(valores):
      print("O número de chaves deve ser igual ao número de valores.")
      return

  dicionario = converter_listas_para_dict(chaves, valores)
  print("Dicionário resultante:", dicionario)

if __name__ == "__main__":
  principal()