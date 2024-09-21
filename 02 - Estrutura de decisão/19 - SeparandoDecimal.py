# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
# dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311,
# 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = int(input('Digite um numero inteiro de até mil: '))
centena = 0
dezena = 0
unidade = 0
while num >= 100:
    centena += 1
    num -= 100

while num >= 10:
    dezena += 1
    num -= 10

while num > 0:
    unidade += 1
    num -= 1

if centena > 0:
    if centena > 1:
        no_centena = "centenas"
    else:
        no_centena = "centena"
    print(f'{centena} {no_centena}')

if dezena > 0:
    if dezena > 1:
        no_dezena = "dezenas"
    else:
        no_dezena = "dezena"
    print(f'{dezena} {no_dezena}')

if unidade > 0:
    if unidade > 1:
        no_unidade = "unidades"
    else:
        no_unidade = "unidade"
    print(f'{unidade} {no_unidade}')

