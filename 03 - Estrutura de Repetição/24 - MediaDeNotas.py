# Faça um programa que calcule o mostre a média aritmética de N notas.

quant = int(input('Quantas notas vai digitar? '))
n = 1
soma = 0
for cada in range(0, quant):
    nota = float(input(f'Digite a {n}ª nota ou # para finalizar: '))
    soma += nota
    n += 1

media = soma/quant

print(f'A media entre as {quant} notas digitadas foi: {media}')
    