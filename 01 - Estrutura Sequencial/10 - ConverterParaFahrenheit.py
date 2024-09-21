# Faça um Programa que peça a temperatura em graus Celsius, 
# transforme e mostre em graus Fahrenheit.

temp = float(input('Qual a temperatura em Celcios? '))
faren = 32+(temp*1.8)
print(f'{temp}° Celcios equivalem a {faren:.2f}° Fahrenheit')