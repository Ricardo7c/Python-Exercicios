# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n

# para um n informado pelo usuário. Use uma função que receba um valor n inteiro
# e imprima até a n-ésima linha.

def numeros(x):
    for cada in range(0, x):
        print('')
        for n in range(0, cada):
            print(cada, end='')


num = int(input('Digite um numero: '))

numeros(num)