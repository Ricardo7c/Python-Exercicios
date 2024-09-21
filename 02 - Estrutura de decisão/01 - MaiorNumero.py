# Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 < num2:
    print(f'{num1} é menor que {num2}')
else:
    print('Os numeros são iguais')