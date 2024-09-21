# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
# no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para
# o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.


hora = float(input('Quanto você ganha por hora? '))
tempo = int(input('Quantas horas você trabalha no mês? '))
salario = hora*tempo
ir = salario*0.11
inss = salario*0.08
sindicato = salario*0.05
print(f'Salario bruto é R${salario:.2f}')
print(f'IR(11%) é: R${ir:.2f}')
print(f'INSS (8%) é: R${inss:.2f}')
print(f'Sindicato (5%) é: R${sindicato:.2f}')
print(f'Salario liquido é: R${salario-(ir+inss+sindicato):.2f}')