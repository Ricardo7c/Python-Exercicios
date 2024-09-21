# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

numeros = [2, 3, 8, 9, 4, 12, 3, 4, 7, 5]
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
misto = []

for num, letra in zip(numeros, letras):
    misto.append(num)
    misto.append(letra)



print(*misto)