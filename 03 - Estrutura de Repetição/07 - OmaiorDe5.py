# Faça um programa que leia 5 números e informe o maior número.

maior = 0
for cada in range(0, 5):
    num = int(input(f'Digite {cada+1}º numero:'))
    if num > maior:
        maior = num

print(f'O maior numero digitado foi: {maior}')