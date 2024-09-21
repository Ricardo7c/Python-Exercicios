# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input('Digite um numero: '))
primo = True

if num < 2 or (num > 2 and num % 2 == 0):
    primo = False
else:
    for cada in range(3, num):
        if num % cada == 0:
            primo = False

if primo == False:
    print('Não é primo')
else:
    print('é primo')