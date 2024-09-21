# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

total = int(input('Informe o numero total de eleitores: '))
a = b = c =0
while total > 0:
    print('Escolha o seu candidato:')
    print('A) Pedro')
    print('B) João')
    print('C) Vitor')
    voto = input('Digite a letra correspondente ao candidato: ').upper()
    if voto not in 'ABC':
        print('Voto invalido! tente novamente.')
    else:
        print('Voto computado!')
        total -= 1
        if voto == 'A':
            a += 1
        elif voto == 'B':
            b += 1
        elif voto == 'C':
            c += 1
print('-----------------')
print('VOTAÇÃO ENCERRADA')
print('')
print(f'Pedro: {a} votos')
print(f'João: {b} votos')
print(f'Vitor: {c} votos')
