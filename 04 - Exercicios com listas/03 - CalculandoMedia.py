# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for n in range(0, 4):
    nota = float(input(f'Digite a {n+1}ª nota: '))
    notas.append(nota)

soma = 0
print('------- Notas -------')
for cada, nota in enumerate(notas):
    print(f'{cada+1}ª nota = {nota}')
    soma += nota
print(' ')
print(f'Media = {soma/4}')