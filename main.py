import sqlite3

def criar_tabela():
    """
    Cria a tabela 'transacoes' no banco de dados 'financas.db', se ela não existir.

    A tabela 'transacoes' possui os seguintes campos:
    - id (INTEGER): Chave primária da transação.
    - tipo (TEXT): Tipo da transação, pode ser 'receita' ou 'despesa'.
    - descricao (TEXT): Descrição da transação.
    - valor (REAL): Valor da transação.
    """
    conn = sqlite3.connect('financas.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transacoes (
                    id INTEGER PRIMARY KEY,
                    tipo TEXT,
                    descricao TEXT,
                    valor REAL
                )''')
    conn.commit()
    conn.close()

def adicionar_transacao(tipo, descricao, valor):
    """
    Adiciona uma transação ao banco de dados.

    Parâmetros:
    - tipo (str): Tipo da transação, pode ser 'receita' ou 'despesa'.
    - descricao (str): Descrição da transação.
    - valor (float): Valor da transação.
    """
    conn = sqlite3.connect('financas.db')
    c = conn.cursor()
    c.execute('''INSERT INTO transacoes (tipo, descricao, valor) VALUES (?, ?, ?)''', (tipo, descricao, valor))
    conn.commit()
    conn.close()

def obter_saldo():
    """
    Obtém o saldo atual da conta somando todas as transações registradas no banco de dados.

    Retorna:
    - saldo (float): Saldo atual da conta.
    """
    conn = sqlite3.connect('financas.db')
    c = conn.cursor()
    c.execute('''SELECT SUM(valor) FROM transacoes''')
    saldo = c.fetchone()[0]
    conn.close()
    return saldo if saldo else 0

def relatorio_gastos_por_categoria():
    """
    Gera um relatório de gastos por categoria baseado nas descrições das transações.

    Retorna:
    - relatorio (list): Lista de tuplas, onde cada tupla contém a descrição da categoria e o total de gastos associado a ela.
    """
    conn = sqlite3.connect('financas.db')
    c = conn.cursor()
    c.execute('''SELECT descricao, SUM(valor) FROM transacoes WHERE valor < 0 GROUP BY descricao''')
    relatorio = c.fetchall()
    conn.close()
    return relatorio

def relatorio_receitas():
    """
    Gera um relatório de todas as receitas registradas no banco de dados.

    Retorna:
    - receitas (list): Lista de tuplas, onde cada tupla representa uma receita com os campos: id, tipo, descricao e valor.
    """
    conn = sqlite3.connect('financas.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM transacoes WHERE tipo = 'receita' ORDER BY id''')
    receitas = c.fetchall()
    conn.close()
    return receitas

def obter_transacoes():
    """
    Obtém todas as transações registradas no banco de dados e calcula o total de transações.

    Retorna:
    - transacoes (list): Lista de tuplas, onde cada tupla representa uma transação com os campos: id, tipo, descricao e valor.
    - total (float): Total de todas as transações.
    """
    conn = sqlite3.connect('financas.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM transacoes ORDER BY id''')
    transacoes = c.fetchall()
    total = sum(transacao[3] for transacao in transacoes)
    conn.close()
    return transacoes, total

def verificar_saldo_inicial():
    """
    Verifica se já existe um saldo inicial registrado no banco de dados.

    Retorna:
    - saldo_inicial_registrado (bool): True se já existe um saldo inicial registrado, False caso contrário.
    """
    conn = sqlite3.connect('financas.db')
    c = conn.cursor()
    c.execute('''SELECT COUNT(*) FROM transacoes WHERE descricao = 'Saldo Inicial' ''')
    saldo_inicial_registrado = c.fetchone()[0]
    conn.close()
    return saldo_inicial_registrado > 0

def menu_principal():
    """
    Exibe o menu principal e permite que o usuário interaja com o aplicativo de controle financeiro.
    """
    # Verificar se já existe um saldo inicial registrado
    if not verificar_saldo_inicial():
        saldo_inicial = float(input("Digite o saldo inicial da conta: "))
        adicionar_transacao('receita', 'Saldo Inicial', saldo_inicial)
        print("Saldo inicial definido com sucesso!")

    while True:
        print("-------APLICATIVO DE CONTROLE FINANCEIRO PESSOAL-------\n [1] Adicionar Receita.\n [2] Adicionar Despesa.\n [3] Ver Relatório de Gastos por Categoria\n [4] Ver Relatório de Receitas\n [5] Ver Extrato\n [6] Sair.")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            descricao = input("Digite a descrição da receita: ")
            valor = float(input("Digite o valor da receita: "))
            adicionar_transacao('receita', descricao, valor)
            print("Receita adicionada com sucesso!")

        elif escolha == "2":
            descricao = input("Digite a descrição da despesa: ")
            valor = float(input("Digite o valor da despesa: "))
            adicionar_transacao('despesa', descricao, -valor)
            print("Despesa adicionada com sucesso!")

        elif escolha == "3":
            relatorio = relatorio_gastos_por_categoria()
            print("\nRelatório de Gastos por Categoria:")
            for descricao, total in relatorio:
                print(f'{descricao}: R$ {total:.2f}')
            print(f'Total: R$ {total:.2f}')

        elif escolha == "4":
            receitas = relatorio_receitas()
            print("\nRelatório de Receitas:")
            for transacao in receitas:
                print(f'{transacao[2]}: R$ {transacao[3]:.2f}')

        elif escolha == "5":
            transacoes, total = obter_transacoes()
            print("\nExtrato:")
            for transacao in transacoes:
                print(f'{transacao[1]}: {transacao[2]} - R$ {transacao[3]:.2f}')
            print(f'Total: R$ {total:.2f}')

        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

criar_tabela()

menu_principal()