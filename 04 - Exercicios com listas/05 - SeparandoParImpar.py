# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores.

todos = []
par = []
impar = []
for n in range(0, 20):
    num = int(input(f'Digite o {n+1} numero: '))
    todos.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print('')
print('Todos os numeros: ', *todos)
print('Numeros pares: ', *par)
print('Numeros impares: ', *impar)