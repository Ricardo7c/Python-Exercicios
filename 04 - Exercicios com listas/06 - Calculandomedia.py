# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.


medias = []
for aluno in range(0, 3):
    soma = 0
    for n in range(0, 4):
        nota = float(input(f'Digite a {n+1}ª nota: '))
        soma += nota
    media = soma/4
    medias.append(media)
    print(media)

contador = 0
for nota in medias:
    if nota >= 7:
        contador += 1

print(f'{contador} alunos tiveram media maior ou igual a 7.0')