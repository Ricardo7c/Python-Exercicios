# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele
# deseja realizar. O resultado da operação deve ser acompanhado de uma frase que
# diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))

while True:
    operador = input('Escolha o operador (+, -, /, *): ')
    if operador in '+-/*':
        if operador == '+':
            resultado = num1+num2
            break
        elif operador == '-':
            resultado = num1-num2
            break
        elif operador == '/':
            resultado = num1/num2
            break
        elif operador == '*':
            resultado = num1*num2
            break
    else:
        print('Operador invalido, tente de novo!')


if resultado % 2 == 0:
    parInp = "Par"
else:
    parInp = "Impar"


if resultado < 0:
    PosNeg = "Negativo"
else:
    PosNeg = "Positivo"


resultadoR = round(resultado)
if resultado == resultadoR:
    DecInt = "Inteiro"
else:
    DecInt = "Decimal"

print(f'O resultado da operação é {resultado} um numero {parInp}, {PosNeg} e {DecInt}')