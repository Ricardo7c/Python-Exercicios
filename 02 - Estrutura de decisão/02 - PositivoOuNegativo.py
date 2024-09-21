# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input('Digite um numero: '))
if num > 0:
    print('O numero digitado é positivo')
elif num < 0:
    print('O numero digitado é negativo')
else:
    print('Zero é um numero neutro, nem positivo nem negativo')