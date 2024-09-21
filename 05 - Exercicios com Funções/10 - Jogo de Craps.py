# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados,
# obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você é um "natural"
# e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde,
# no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random

def jogarDados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    total = dado1+dado2
    return dado1, dado2, total


def jogada(total, lanc):
    global ponto
    if lanc == 1:
        if total == 7 or total == 11:
            print('Você é um natural, venceu o jogo!')
            return True
        elif total == 2 or total == 3 or total == 12:
            print('CRAPS: Você perdeu!')
            return True
        else:
            print('Ponto pra você!')
            ponto = total
            return False
    elif total == ponto:
        print('Você venceu!')
        return True
    elif total == 7:
        print('Você perdeu!')
        return True
    else:
        print('Continue tentando!')
        return False

print('-------  Bem vindo ao craps  -------')
lanc = 0
play = False
while play == False:
    input('Pressione um tecla para lançar os dados!')
    d1, d2, total = jogarDados()
    lanc += 1
    print(f'{d1} e {d2} total: {total}')
    play = jogada(total, lanc)