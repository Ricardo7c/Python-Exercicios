# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo
# usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar
# os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões)
# executados.

num = int(input('Digite um número: '))
primos = [2]
for number in range(3, num + 1, 2):
    primos.append(number)

div = 0
primos_validados = []  # Nova lista para armazenar os números primos

for number in primos:
    if number == 2:
        primos_validados.append(number)
        continue

    eh_primo = True
    for cada in range(2, int(number**0.5) + 1):
        div += 1
        if number % cada == 0:
            eh_primo = False
            break

    if eh_primo:
        primos_validados.append(number)

print(f'Os números primos entre 1 e {num} são: ', end="")

# Imprime os primos formatados corretamente
for i, cada in enumerate(primos_validados):
    if i == len(primos_validados) - 1:
        print(cada)
    else:
        print(cada, end=', ')

print(f'O total de divisões: {div}')
