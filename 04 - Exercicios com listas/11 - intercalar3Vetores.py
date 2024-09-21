# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada

numeros = [2, 3, 8, 9, 4, 12, 3, 4, 7, 5]
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
simbolos = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
misto = []

for num, letra, simbol in zip(numeros, letras, simbolos):
    misto.append(num)
    misto.append(letra)
    misto.append(simbol)


print(*misto)