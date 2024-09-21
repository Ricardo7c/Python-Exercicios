# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média
# anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas = []
soma = 0
for mes in meses:
    temp = float(input(f'Digite a temperatura do mês de {mes}: '))
    temperaturas.append(temp)
    soma += temp

media = soma/12
print('-------------------------------------------')
print(f'A temperatura media anual foi: {media:.2f}')
print('Os meses que ultrapassaram a media anual foram: ')
print(' ')
for mes, temp in zip(meses, temperaturas):
    if temp > media:
        print(f'{mes}: {temp:.2f}')
