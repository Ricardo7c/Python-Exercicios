# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input('Digite um numero: '))
primo = True

cont = 0
for cada in range(1, num+1):
    if num % cada == 0:
        cont += 1
if cont > 2 or num < 2:
    primo = False


if primo == True:
    print('é primo')
else:
    print('não é primo')