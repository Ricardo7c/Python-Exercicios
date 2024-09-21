# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
# e a quantidade de números impares.
par = 0
impar = 0
for cada in range(0, 10):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        par += 1
    elif num % 2 != 0:
        impar += 1

print(f'Foram digitados {par} numeros pares, e {impar} numeros impares')