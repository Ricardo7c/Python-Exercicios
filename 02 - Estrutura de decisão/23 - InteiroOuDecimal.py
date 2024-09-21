# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.

num = float(input('Digite um numero: '))
numR = round(num)

if num == numR:
    print('O numero é inteiro')
else:
    print('O numero é real')