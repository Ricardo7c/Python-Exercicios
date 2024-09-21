# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da
# promoção, porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere 
# um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, 
# tipo de pagamento, valor do desconto e valor a pagar.

print('Qual o tipo de carne: ')
print('A) File Duplo')
print('B) Alcatra')
print('C) Picanha')

carne = input("Digite a letra correspondente: ").upper()
kg = float(input('Quantos kg deseja? '))

print('Qual a forma de pagamento: ')
print('A) Dinheiro')
print('B) Cartão Tabajara')
pag = input("Digite a letra correspondente: ").upper()

if carne == 'A':
    tipo = 'File Duplo'
    if kg <= 5:
        valor = kg*4.90
    else:
        valor = kg*5.80

elif carne == 'B':
    tipo = 'Alcatra'
    if kg <= 5:
        valor = kg*5.90
    else:
        valor = kg*6.80

elif carne == 'C':
    tipo = 'Picanha'
    if kg <= 5:
        valor = kg*6.90
    else:
        valor = kg*7.80

if pag == 'B':
    tipo_pag = 'Cartão Tabajara'
    desconto = (valor*0.05)
    valorfinal = valor - desconto
else:
    tipo_pag = 'Dinheiro'
    desconto = 0
    valorfinal = valor

print('=========== Nota fiscal ============')
print(f'{kg}kg de {tipo}')
print(f'Preço total: R${valor:.2f}')
print(f'Forma de pagamento: {tipo_pag}')
print(f'Desconto: R${desconto:.2f}')
print(f'Total a pagar: R${valorfinal:.2f}')
