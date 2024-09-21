# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes
# e limitando o fatorial a números inteiros positivos e menores que 16.

while True:
    num = int(input('Digite um número: '))
    if num > 16 or num % 2 != 0:
        print('Valor invalido, tente novamente!')
    else:
        print(f'{num}!', end=' = ')
        resultado = 1

        for cada in range(num, 0, -1):
            resultado *= cada
            if cada != 1:
                print(cada, end='.')
            else:
                print(cada, end=' ')

        print('=', resultado)