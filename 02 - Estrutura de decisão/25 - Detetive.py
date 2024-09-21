# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

Q1 = input('Telefonou para a vítima? ').upper()
Q2 = input('Esteve no local do crime? ').upper()
Q3 = input('Mora perto da vitima? ').upper()
Q4 = input('Devia para a vitima? ').upper()
Q5 = input('Já trabalhou com a vitima? ').upper()
pos = 0

if Q1 in 'SIM':
    pos += 1

if Q2 in 'SIM':
    pos += 1

if Q3 in 'SIM':
    pos += 1

if Q4 in 'SIM':
    pos += 1

if Q5 in 'SIM':
    pos += 1

if pos <= 1:
    resultado = 'INOCENTE'
elif pos == 2:
    resultado = 'SUSPEITO'
elif pos == 3 or pos == 4:
    resultado = 'CÚMPLICE'
elif pos == 5:
    resultado = 'CULPADO'

print(f'O interrogado foi considerado {resultado}')