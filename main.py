def mostrar_assentos(salas, sala):
  """
  Mostra o mapa de assentos da sala especificada.

  Args:
      salas (list): Uma lista de salas, onde cada sala é representada por uma lista de assentos.
      sala (int): O número da sala para exibir o mapa de assentos.
  """
  print(f"Mapa de Assentos da Sala {sala}:")
  print("  " + " ".join([str(i + 1) for i in range(len(salas[0][0]))]))
  for i in range(len(salas[sala])):
      print(chr(65 + i), end=" ")
      for j in range(len(salas[sala][i])):
          if salas[sala][i][j] == 'X':
              print('X', end=" ")
          else:
              print('L' if salas[sala][i][j] == 'L' else 'X', end=" ")
      print()

def reservar_assento(salas, sala, fileira, assento, nome):
  """
  Reserva um assento na sala especificada para o cliente com o nome especificado.

  Args:
      salas (list): Uma lista de salas, onde cada sala é representada por uma lista de assentos.
      sala (int): O número da sala onde o assento será reservado.
      fileira (int): O número da fileira onde o assento está localizado.
      assento (int): O número do assento na fileira.
      nome (str): O nome do cliente que está fazendo a reserva.

  Returns:
      bool: True se o assento foi reservado com sucesso, False caso contrário.
  """
  if fileira < 0 or fileira >= len(salas[sala]) or assento < 0 or assento >= len(salas[sala][0]):
      print("Assento inválido.")
      return False
  if salas[sala][fileira][assento] != 'L':
      print("Assento indisponível.")
      return False
  salas[sala][fileira][assento] = nome
  print(f"Assento {chr(65 + fileira)}-{assento + 1} reservado para {nome}.")
  return True

def procurar_reserva(salas, nome):
  """
  Procura por uma reserva associada ao nome especificado e exibe informações sobre a reserva.

  Args:
      salas (list): Uma lista de salas, onde cada sala é representada por uma lista de assentos.
      nome (str): O nome do cliente para procurar.

  Returns:
      None
  """
  for sala, assentos in enumerate(salas):
      for i, fileira in enumerate(assentos):
          for j, assento in enumerate(fileira):
              if assento == nome:
                  print(f"{nome} reservou o assento {chr(65 + i)}-{j + 1} na sala {sala + 1}.")
                  return
  print(f"{nome} não tem assento reservado.")

def main():
  num_salas = 2
  num_fileiras = 5
  assentos_por_fileira = 10
  salas = [[['L' for _ in range(assentos_por_fileira)] for _ in range(num_fileiras)] for _ in range(num_salas)]

  while True:
      print('\n-------RESERVA DE INGRESSOS-------')
      opcao = input('[1] Escolher filme\n[2] Pesquisar reserva por nome\n[3] Sair\nEscolha uma opção: ')

      if opcao == '1':
          filme = int(input('[1] Homem-Aranha\n[2] Vingadores\nEscolha um filme: '))
          if filme == 1:
              sala = 0
              print("Filme escolhido: Homem-Aranha")
          elif filme == 2:
              sala = 1
              print("Filme escolhido: Vingadores")
          else:
              print("Opção inválida. Escolha novamente.")
              continue
          mostrar_assentos(salas, sala)
          fileira = input("Digite a letra da fileira desejada (A-E): ").upper()
          assento = int(input("Digite o número do assento desejado (1-10): ")) - 1
          nome = input("Digite seu nome: ")
          if reservar_assento(salas, sala, ord(fileira) - 65, assento, nome):
              print(f"Assento {chr(65 + ord(fileira) - 65)}-{assento + 1} reservado para {nome}.")
          else:
              print("Erro ao reservar o assento.")
      elif opcao == '2':
          nome = input("Digite o nome para pesquisar a reserva: ")
          procurar_reserva(salas, nome)
      elif opcao == '3':
          print('Saindo...')
          break
      else:
          print('Opção inválida. Por favor, escolha uma opção válida.')


if __name__ == "__main__":
  main()