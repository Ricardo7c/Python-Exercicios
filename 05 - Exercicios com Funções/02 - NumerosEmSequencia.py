# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro
# imprima até a n-ésima linha.


def numeros(x):
    for cada in range(0, x):
        print('')
        for n in range(1, cada):
            print(n, end='')




num = int(input('Digite um numero: '))

numeros(num)