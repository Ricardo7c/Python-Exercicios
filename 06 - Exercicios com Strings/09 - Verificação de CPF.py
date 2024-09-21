cpf = input('Digite o numero do CPF: ')

cpfTratado = cpf.replace('.','')
cpfTratado = cpfTratado.replace('-','')

numeros = []

for c in cpfTratado:
    numeros.append(int(c))

lista = []
soma1 = soma2 = 0
for num in range(0, 9):
    soma1 += (numeros[num]*(num+1))

digito  = soma1%11

if digito == 10:
    digito = 0

for num in range(0, 10):
    soma2 += (numeros[num]*(num))

digito2  = soma2%11

if digito2 == 10:
    digito2 = 0

if digito == numeros[9] and digito2 == numeros[10]:
    print('CPF Valido!')
else:
    print('CPF Invalido!')