# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento
# iniciais. Valide a entrada e permita repetir a operação.

while True:
    a = int(input('Digite a população do país A: '))
    tax_a = float(input('Digite a taxa de crescimento do país A: '))
    tax_a = tax_a/100

    b = int(input('Digite a população do país B: '))
    tax_b = float(input('Digite a taxa de crescimento do país B: '))
    tax_b = tax_b/100

    anos = 0
    while a < b:
        a += (a*0.03)
        b += (b*0.015)
        anos += 1

    print(f'Serão nescessarios {anos} anos')
    print('-------------------------------')

    fim = input('Deseja fazer um novo calculo S/N? ').upper()
    if fim == 'N':
        break