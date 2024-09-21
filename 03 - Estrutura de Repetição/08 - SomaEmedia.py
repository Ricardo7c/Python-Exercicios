# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
for cada in range(0, 5):
    num = int(input(f'Digite {cada+1}º numero:'))
    soma += num

media = soma/5

print(f'A soma dos numeros foi: {soma}')
print(f'A media dos numeros somados foi: {media}')