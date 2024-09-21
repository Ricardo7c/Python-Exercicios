# Faça um Programa que leia um vetor A com 10 números inteiros, 
# calcule e mostre a soma dos quadrados dos elementos do vetor.

lista = [2, 3, 8, 9, 4, 12, 3, 4, 7, 5]

soma = 0
for num in lista:
    quad = num**2
    soma += quad

print(f'A soma dos quadrados dos numeros é: {soma}')