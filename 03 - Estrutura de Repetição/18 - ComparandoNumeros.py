# Faça um programa que, dado um conjunto de N números, determine o menor valor,
# o maior valor e a soma dos valores.

maior = 0
menor = 0
soma = 0
while True:
    num = int(input('Digite um numero: '))
    soma += num
    
    if num > maior:
        maior = num
    elif num < menor or menor == 0:
        menor = num
        
    res = input('Quer continuar S/N? ').upper()
    if res in 'N':
        break

print(f'O maior foi: {maior}')
print(f'O menor foi: {menor}')
print(f'A soma dos numeros foi: {soma}')