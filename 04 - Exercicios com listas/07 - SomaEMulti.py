# Faça um Programa que leia um vetor de 5 números inteiros,
# mostre a soma, a multiplicação e os números.

lista = [2, 6, 8, 15, 5]
soma = 0
multi = 1
for cada in lista:
    soma += cada
    multi *= cada

print('Os numeros: ', *lista)
print(f'A soma: {soma}')
print(f'A multiplicação: {multi}')