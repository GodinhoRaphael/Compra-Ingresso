def converter_lista_para_dict(lista_de_pares):
  dicionario = dict(lista_de_pares)
  return dicionario

# Exemplo de uso:
lista_notas_alunos = [("Ana", 8), ("João", 7), ("Maria", 9)]
dicionario_notas_alunos = converter_lista_para_dict(lista_notas_alunos)
print(dicionario_notas_alunos)