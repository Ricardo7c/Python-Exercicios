# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A - o produto do dobro do primeiro com metade do segundo .
# B - soma do triplo do primeiro com o terceiro.
# C - o terceiro elevado ao cubo.

num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero inteiro: '))
real = float(input('Agora digite um numero real: '))
print(f'O produto do dobro de {num1} com a metade de {num2} é: {(num1*2)*(num2/2)}')
print(f'A soma do triplo de {num1} com {real} é: {real+(num1*3)}')
print(f'{real} elevado ao cubo é: {real**3:.2f}')