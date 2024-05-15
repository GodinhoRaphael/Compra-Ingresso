import random

questoes = [
    ("Qual é a capital da Austrália?", ["a) Sydney", "b) Canberra", "c) Melbourne", "d) Brisbane"]),
    ("Quem pintou a Mona Lisa?", ["a) Michelangelo", "b) Leonardo da Vinci", "c) Pablo Picasso", "d) Vincent van Gogh"]),
    ("Qual é o maior planeta do nosso sistema solar?", ["a) Terra", "b) Marte", "c) Júpiter", "d) Saturno"]),
    ("Qual é a montanha mais alta do mundo?", ["a) K2", "b) Monte Everest", "c) Mont Blanc", "d) Kilimanjaro"]),
    ("Quem escreveu 'Romeu e Julieta'?", ["a) William Shakespeare", "b) Jane Austen", "c) Charles Dickens", "d) F. Scott Fitzgerald"]),
    ("Qual é o elemento químico com o símbolo 'Fe'?", ["a) Ferro", "b) Cobre", "c) Ouro", "d) Prata"]),
    ("Qual é o maior oceano do mundo?", ["a) Oceano Atlântico", "b) Oceano Índico", "c) Oceano Pacífico", "d) Oceano Ártico"]),
    ("Quem foi o primeiro homem a pisar na lua?", ["a) Neil Armstrong", "b) Buzz Aldrin", "c) Yuri Gagarin", "d) Alan Shepard"]),
    ("Qual é o animal terrestre mais rápido?", ["a) Guepardo", "b) Lebre", "c) Antílope", "d) Leão"]),
    ("Quem é o autor de 'A Origem das Espécies'?", ["a) Charles Darwin", "b) Isaac Newton", "c) Albert Einstein", "d) Galileu Galilei"]),
    ("Qual é o rio mais longo do mundo?", ["a) Rio Amazonas", "b) Rio Nilo", "c) Rio Yangtze", "d) Rio Mississippi"]),
    ("Quem foi o primeiro presidente dos Estados Unidos?", ["a) George Washington", "b) Abraham Lincoln", "c) Thomas Jefferson", "d) John Adams"]),
    ("Qual é a capital do Canadá?", ["a) Toronto", "b) Vancouver", "c) Ottawa", "d) Montreal"]),
    ("Qual é o maior deserto do mundo?", ["a) Deserto do Saara", "b) Deserto de Gobi", "c) Deserto da Arábia", "d) Deserto de Kalahari"]),
    ("Quem foi o primeiro homem a voar em um avião?", ["a) Orville Wright", "b) Wilbur Wright", "c) Amelia Earhart", "d) Alberto Santos Dumont"])
]

respostas = [
    "b",
    "b",
    "c",
    "b",
    "a",
    "a",
    "c",
    "a",
    "a",
    "a",
    "a",
    "a",
    "c",
    "a",
    "b"
]

rodadas_maximas = 3
rodadas = 0

#Loop das questoes
while rodadas < rodadas_maximas:
    resposta = input('Está pronto para iniciar o jogo de trivia? [a]Sim [b]Não\n')
    acertos = 0
    if resposta == 'a':
        for _ in range(5):
            #Seleciona qual questao e resposta vai ser utilizado.
            item = random.randint(0, 14)
            questao_aleatoria, opcoes_resposta = questoes[item]
            print(questao_aleatoria)
            for opcao in opcoes_resposta:
                print(opcao)
            resposta = input('\nResposta: ')
            print('Resposta correta: ', respostas[item])
            #Verificar se a resposta esta correta
            if resposta == respostas[item]:
                acertos += 1
                print('Certa resposta!')
            else:
                print('Errouu!')
        if acertos == 5:
            if rodadas < 2:
                print('Parabéns! Acertou todas as', acertos, '\nIniciando nova rodada(3 no total).....')
                rodadas += 1
            else:
                print('Parabéns! Jogo finalizado.')
                break
        else:
            print('Quantidade de acertos: ', acertos, '\n Reiniciando o jogo....')

    else:
        print('Poxa vida....')
        break
