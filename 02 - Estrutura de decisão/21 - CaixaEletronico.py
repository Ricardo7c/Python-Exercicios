# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque
# e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de
#  1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
# uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


saque = int(input('Digite o valor do saque: '))
n100 = n50 = n10 = n5 = n1 = 0

while saque >= 100:
    n100 += 1
    saque -= 100

while saque >= 50:
    n50 += 1
    saque -= 50

while saque >= 10:
    n10 += 1
    saque -=10

while saque >= 5:
    n5 += 1
    saque -=5

while saque >= 1:
    n1 += 1
    saque -= 1

if n100 > 0:
    if n100 > 1:
        n100 = f'{n100}x notas de R$ 100,00'
    else:
        n100 = f'{n100}x nota de R$ 100,00'
    print(n100)

if n50 > 0:
    if n50 > 1:
        n50 = f'{n50}x notas de R$ 50,00'
    else:
        n50 = f'{n50}x nota de R$ 50,00'
    print(n50)

if n10 > 0:
    if n10 > 1:
        n10 = f'{n10}x notas de R$ 10,00'
    else:
        n10 = f'{n10}x nota de R$ 10,00'
    print(n10)

if n5 > 0:
    if n5 > 1:
        n5 = f'{n5}x notas de R$ 5,00'
    else:
        n5 = f'{n5}x nota de R$ 5,00'
    print(n5)

if n1 > 0:
    if n1 > 1:
        n1 = f'{n1}x notas de R$ 1,00'
    else:
        n1 = f'{n1}x nota de R$ 1,00'
    print(n1)