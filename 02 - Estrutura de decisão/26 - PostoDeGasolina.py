# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool: até 20 litros, desconto de 3% por litro. acima de 20 litros, desconto de 5% por litro
# Gasolina:até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, 
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da 
# gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

combustivel = input('Qual o combustivel desejado: (G)asolina ou (A)lcool? ').upper()
litros = int(input('Qaul a quantidade em litros? '))

if combustivel == 'A':
    valor = (litros*1.90)
    if litros <= 20:
        valor = valor-(valor*0.03)
    elif litros > 20:
        valor = valor-(valor*0.05)

if combustivel == 'G':
    valor = (litros*2.50)
    if litros <= 20:
        valor = valor-(valor*0.04)
    elif litros > 20:
        valor = valor-(valor*0.06)

print(f'O valor a ser pago é de R${valor:.2f}')