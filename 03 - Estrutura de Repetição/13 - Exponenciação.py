# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número
# elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input('Digite o numero base: '))
expoente = int(input('Digite o expoente: '))

resultado = base
for casa in range(1, expoente):
    resultado *= base

if expoente < 0:
    resultado = 1/resultado

print(f'{base} elevado a {expoente} é {resultado}')