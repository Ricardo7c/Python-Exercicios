# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo
# usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar
# os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões)
# executados.

num = int(input('Digite um numero: '))
primos = [2]
for number in range (3, num+1, 2):
        primos.append(number)

div = 0
for number in primos:
    if number > 2:
        for cada in range(2, int(number**0.5)+1):
            div += 1
            if number % cada == 0:
                 primos.remove(number)


print(f'O numeros primos ente 1 e {num} são: ')

for cada in primos:
    if cada == primos[-1]:
        print(cada)
    else:
        print(cada, end=', ')

print(f'O total de divisões: {div}')