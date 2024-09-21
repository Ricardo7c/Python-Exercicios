# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números
# primos existentes entre 1 e um número inteiro informado pelo usuário.

num = int(input('Digite um numero: '))
primos = [2]
for number in range (3, num+1, 2):
        primos.append(number)

lista = []
for number in primos:
    cont = 0
    for cada in range(1, int(number**0.5)):
        if number % cada == 0:
            cont += 1
    if cont > 2:
         primos.remove(number)

print(primos)