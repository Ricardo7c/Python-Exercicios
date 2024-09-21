# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input('Digite o preço do produto 1: '))
produto2 = float(input('Digite o preço do produto 2: '))
produto3 = float(input('Digite o preço do produto 3: '))

if produto1 < produto2 and produto1 < produto3:
    print(f'você deve comprar o produto 1')
elif produto2 < produto1 and produto2 < produto3:
    print(f'você deve comprar o produto 2')
elif produto3 < produto2 and produto3 < produto1:
    print(f'você deve comprar o produto 3')