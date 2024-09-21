# Faça um programa que receba dois números inteiros e gere os números 
# inteiros que estão no intervalo compreendido por eles.

num1 = int(input('Digite o inicio da contagem: '))
num2 = int(input('Digite o final da contagem: '))

for cada in range((num1+1), num2):
    print(cada, end=' ')