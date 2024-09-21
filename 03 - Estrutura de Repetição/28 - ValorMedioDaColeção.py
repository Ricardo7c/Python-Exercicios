# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
# e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor
# para cada um.

cds = int(input('Quantos CDs você tem? '))


quant = cds
soma = 0
n = 1
while quant > 0:
    preco = float(input(f'Quanto custou o {n}º CD: '))
    soma += preco
    quant -= 1
    n += 1

media = soma/cds

print(f'Você gastou em media R${media:.2f} por CD')