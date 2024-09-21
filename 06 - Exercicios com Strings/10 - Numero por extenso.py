unidades = ["Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", 'zero']
dezenas = ["Dez", "Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]

num = int(input('Digite um numero até 99: '))

dezena = unidade = 0
cont = 0

while num >= 10:
    dezena += 1
    num -= 10

while num < 10 and num > 0:
    unidade += 1
    num -= 1


if unidade-1 == -1:
    print(f'{dezenas[dezena-1]}')
elif dezena == 0:
    print(f'{unidades[unidade-1]}')
else:
    print(f'{dezenas[dezena-1]} e {unidades[unidade-1]}')
