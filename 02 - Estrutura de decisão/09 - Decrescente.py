# Faça um Programa que leia três números e mostre-os em ordem decrescente

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite mais um numero: '))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f'{num1}, {num2}, {num3}')
    else:
         print(f'{num1}, {num3}, {num2}')   

elif num2 > num1 and num2 > num3:
    if num1 > num3:
         print(f'{num2}, {num1}, {num3}')
    else:
         print(f'{num2}, {num3}, {num1}')

elif num3 > num2 and num3 > num1:
    if num2 > num1:
        print(f'{num3}, {num2}, {num1}')
    else:
        print(f'{num3}, {num1}, {num2}')