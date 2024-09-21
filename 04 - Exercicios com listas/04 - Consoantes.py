# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes.

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

consoantes = []
for cada in letras:
    if not cada in 'aeiou':
        consoantes.append(cada)

print(f'Foram lidas {len(consoantes)} consoantes que são as seguintes: ', *consoantes)