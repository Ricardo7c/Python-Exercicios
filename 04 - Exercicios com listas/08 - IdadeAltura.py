# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu
# respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []

for cada in range(0, 5):
    idade = int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura: '))
    print('Cadastro salvo!')
    print('---------------')
    idades.append(idade)
    alturas.append(altura)

print('Idades na ordem reversa: ')
for idade in reversed (idades):
    print(idade, end=' ')

print('Alturas na ordem reversa: ')
for altura in reversed (alturas):
    print(altura, end=' ')