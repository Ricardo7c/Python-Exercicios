# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

hora = float(input('Quanto você ganha por hora? '))
tempo = int(input('Quantas horas você trabalha no mês? '))
salario = hora*tempo
print(f'O seu salario no final do mês é de R${salario:.2f}')