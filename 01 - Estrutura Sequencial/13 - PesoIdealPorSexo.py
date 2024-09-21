# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

alt = float(input('Qual sua altura? '))
sexo = input('Você é (H)omen ou (M)ulher? ').upper()
if sexo == 'H':
    ideal = (72.7*alt)-58
elif sexo == 'M':
    ideal = (62.1*alt)-44.7
else:
    print('informação invalida')

print(f'Seu peso ideal é: {ideal:.2f}kg')