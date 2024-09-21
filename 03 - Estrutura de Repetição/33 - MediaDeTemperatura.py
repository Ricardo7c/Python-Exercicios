# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que
# leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas
# informadas, bem como a média das temperaturas.


maior = menor = media = soma = cont = 0
while True:
    temp = float(input('Digite a temperatura ou 0 para sair: '))
    if temp == 0:
        break
    elif menor == 0 or menor > temp:
        menor = temp
    elif maior < temp:
        maior = temp
    cont += 1
    soma += temp

media = soma/cont

print(f'A maior temperatura registrada foi: {int(maior)} °C')
print(f'A menor temperatura registrada foi: {int(menor)} °C')
print(f'A media de temperaturas registrada foi: {int(media)} °C')
