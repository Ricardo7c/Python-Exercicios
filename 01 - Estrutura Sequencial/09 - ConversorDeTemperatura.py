# Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius.
# Formula: C = 5 * ((F-32) / 9).

temp = float(input('Qual a temperatura em Fahrenheit? '))
celcio = 5*((temp-32)/9)
print(f'{temp}° Fahrenheit equivalem a {celcio:.2f}° Celcios')