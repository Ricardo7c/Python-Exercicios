# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

num = int(input('Fatorial de: '))

print(f'{num}!', end=' = ')
resultado = 1

for cada in range(num, 0, -1):
    resultado *= cada
    if cada != 1:
        print(cada, end='.')
    else:
        print(cada, end=' ')

print('=', resultado)