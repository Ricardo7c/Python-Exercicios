# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar
# se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se 
# a turma é jovem, adulta ou idosa, conforme a média calculada.

soma = cont = 0
while True:
    idade = int(input('Digite uma idade ou 00 para sair: '))
    if idade == 00:
        break
    soma += idade
    cont = 1

media = soma/cont

if media > 0 and media <= 25:
    print('A turma é jovem')
elif media > 25 and media <= 60:
    print('A turma é adulta')
else:
    print('A turma é idosa')