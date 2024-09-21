# Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
# As turmas não podem ter mais de 40 alunos.

turmas = int(input('Quantas turmas são? '))
n = 1
soma = 0
qturmas = turmas
while qturmas > 0:
    alunos = int(input('A {n}ª turma tem quantos alunos: '))
    if alunos > 40:
        print('Uma turma não pode ter mais de 40 alunos')
    else:
        soma += alunos
        qturmas -= 1
media = int(soma/turmas)

print(f'O numero medio de alunos por turma é {media}')