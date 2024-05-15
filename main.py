import sqlite3
import string
import random

def criptografar(senha):
    """
    Criptografa a senha usando a cifra de César.

    Args:
        senha (str): A senha a ser criptografada.

    Returns:
        str: A senha criptografada.
    """
    chave = 3  
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    senha_criptografada = ''
    for char in senha:
        if char in alfabeto:
            indice = (alfabeto.index(char) + chave) % len(alfabeto)
            senha_criptografada += alfabeto[indice]
        else:
            senha_criptografada += char
    return senha_criptografada

def descriptografar(senha_criptografada):
    """
    Descriptografa a senha usando a cifra de César.

    Args:
        senha_criptografada (str): A senha criptografada.

    Returns:
        str: A senha descriptografada.
    """
    chave = 3  
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    for char in senha_criptografada:
        if char in alfabeto:
            indice = (alfabeto.index(char) - chave) % len(alfabeto)
            senha += alfabeto[indice]
        else:
            senha += char
    return senha

def gerar_senha(comprimento):
    """
    Gera uma senha aleatória com o comprimento especificado.

    Args:
        comprimento (int): O comprimento da senha a ser gerada.

    Returns:
        str: A senha gerada.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(comprimento))

def conectar_bd():
    """
    Cria uma conexão com o banco de dados.

    Returns:
        sqlite3.Connection: A conexão com o banco de dados.
    """
    conexao = sqlite3.connect('senhas.db')
    return conexao

def criar_tabela(conexao):
    """
    Cria a tabela de senhas no banco de dados.

    Args:
        conexao (sqlite3.Connection): A conexão com o banco de dados.
    """
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS senhas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            servico TEXT NOT NULL,
            username TEXT NOT NULL,
            senha TEXT NOT NULL
        );
    ''')
    conexao.commit()

def inserir_senha(conexao, servico, username, senha):
    """
    Insere uma nova senha no banco de dados.

    Args:
        conexao (sqlite3.Connection): A conexão com o banco de dados.
        servico (str): O nome do serviço.
        username (str): O username associado à senha.
        senha (str): A senha a ser inserida.
    """
    senha_criptografada = criptografar(senha)
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO senhas (servico, username, senha)
        VALUES (?, ?, ?)
    ''', (servico, username, senha_criptografada))
    conexao.commit()

def consultar_senha(conexao, servico, palavra_chave):
    """
    Consulta a senha no banco de dados.

    Args:
        conexao (sqlite3.Connection): A conexão com o banco de dados.
        servico (str): O nome do serviço para o qual deseja-se consultar a senha.
        palavra_chave (str): A palavra-chave para acesso às senhas.
    """
    if palavra_chave != 'Roma':
        print("Palavra-chave incorreta.")
        return

    cursor = conexao.cursor()
    cursor.execute('''
        SELECT username, senha FROM senhas WHERE servico = ?
    ''', (servico,))
    resultado = cursor.fetchone()

    if resultado:
        username, senha_criptografada = resultado
        senha = descriptografar(senha_criptografada)
        print(f"Username: {username}")
        print(f"Senha: {senha}")
    else:
        print("Serviço não encontrado.")

def main():
    conexao = conectar_bd()
    criar_tabela(conexao)

    while True:
        print('-------GERADOR DE SENHAS-------')
        opcao = input('[1] Gerar nova senha\n[2] Consultar senha\n[3] Sair\nEscolha uma opção: ')

        if opcao == '1':
            servico = input("Nome do serviço: ")
            username = input("Username: ")
            comprimento = int(input("Comprimento da senha: "))
            senha = gerar_senha(comprimento)
            inserir_senha(conexao, servico, username, senha)
            print("Senha gerada com sucesso")
        elif opcao == '2':
            servico = input("Nome do serviço: ")
            palavra_chave = input("Digite a palavra-chave: ")
            consultar_senha(conexao, servico, palavra_chave)
        elif opcao == '3':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')


if __name__ == "__main__":
    main()
