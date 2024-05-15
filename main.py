class Contato:
  def __init__(self, nome, endereco, data_nascimento, telefones=[], emails=[]):
      self.nome = nome
      self.endereco = endereco
      self.data_nascimento = data_nascimento
      self.telefones = telefones
      self.emails = emails

  def adicionar_telefone(self, telefone):
      self.telefones.append(telefone)

  def adicionar_email(self, email):
      self.emails.append(email)

class Agenda:
  def __init__(self):
      self.contatos = {}

  def adicionar_contato(self, contato):
      self.contatos[contato.nome] = contato

  def buscar_contato(self, nome):
      if nome in self.contatos:
          return self.contatos[nome]
      else:
          return None

  def remover_contato(self, nome):
      if nome in self.contatos:
          del self.contatos[nome]
          print("Contato removido com sucesso.")
      else:
          print("Contato não encontrado.")

  def listar_contatos(self):
      print("Lista de Contatos:")
      for contato in self.contatos.values():
          print("Nome:", contato.nome)
          print("Endereço:", contato.endereco)
          print("Data de Nascimento:", contato.data_nascimento)
          print("Telefones:", contato.telefones)
          print("Emails:", contato.emails)
          print("--------------------")

def menu():
  print("\n==== Menu ====")
  print("1. Adicionar Contato")
  print("2. Buscar Contato")
  print("3. Remover Contato")
  print("4. Listar Contatos")
  print("5. Sair")

def main():
  agenda = Agenda()

  while True:
      menu()
      opcao = input("Escolha uma opção: ")

      if opcao == "1":
          nome = input("Nome: ")
          endereco = input("Endereço: ")
          data_nascimento = input("Data de Nascimento: ")
          telefones = input("Telefones (separados por vírgula): ").split(",")
          emails = input("Emails (separados por vírgula): ").split(",")
          novo_contato = Contato(nome, endereco, data_nascimento, telefones, emails)
          agenda.adicionar_contato(novo_contato)
          print("Contato adicionado com sucesso.")

      elif opcao == "2":
          nome = input("Digite o nome do contato a ser buscado: ")
          contato_encontrado = agenda.buscar_contato(nome)
          if contato_encontrado:
              print("Contato encontrado:")
              print("Nome:", contato_encontrado.nome)
              print("Endereço:", contato_encontrado.endereco)
              print("Data de Nascimento:", contato_encontrado.data_nascimento)
              print("Telefones:", contato_encontrado.telefones)
              print("Emails:", contato_encontrado.emails)
          else:
              print("Contato não encontrado.")

      elif opcao == "3":
          nome = input("Digite o nome do contato a ser removido: ")
          agenda.remover_contato(nome)

      elif opcao == "4":
          agenda.listar_contatos()

      elif opcao == "5":
          print("Saindo...")
          break

      else:
          print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
  main()
