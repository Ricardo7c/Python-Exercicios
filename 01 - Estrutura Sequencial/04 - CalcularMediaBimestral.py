# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

contador = 1
soma = 0
while contador <= 4:
    nota = float(input(f'Digite a {contador}º nota: '))
    soma += nota
    contador += 1
media = soma/4

print(f'A media bimestral é {media}')