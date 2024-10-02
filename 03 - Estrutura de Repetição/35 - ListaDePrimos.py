# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números
# primos existentes entre 1 e um número inteiro informado pelo usuário.

numero = int(input('Digite um numero: '))
lista_primos = []

for num in range(2, numero):
    primo = True
    if num < 2 or (num > 2 and num % 2 == 0):
        primo = False
    else:
        for cada in range(2, num):
            if num % cada == 0:
                primo = False

    if primo:
        lista_primos.append(num)

print(lista_primos)