# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o 
# usuário informe um valor válido.

while True:
    nota = float(input('Digite uma nota valida entre 1/10: '))
    if nota > 0 and nota <= 10:
        print(f'{nota} é uma nota valida!')
        break
    else:
        print('Valor invalido, tente novamente!')
        print('________________________________')
    