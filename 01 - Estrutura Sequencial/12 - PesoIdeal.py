# Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, 
# Fórmula: (72.7*altura) - 58

alt = float(input('Qual sua altura: '))
ideal = (72.7*alt)-58
print(f'Seu peso ideal é: {ideal:.2f}kg')