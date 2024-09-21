# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
# Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
# e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela.

valorhora = float(input('Qual o valor da sua hora de trabalho? '))
quanthora = int(input('Quantas horas você trabalhou esse mês? '))

salario = valorhora*quanthora
inss = salario*0.10
fgts = salario*0.11

if salario > 900 and salario <= 1500:
    ir = salario*0.05
    irperct = '5%'
elif salario > 1500 and salario <= 2500:
    ir = salario*0.10
    irperct = '10%'
elif salario > 2500:
    ir = salario*0.20
    irperct = '20%'
else:
    ir = 0
    irperct = 'ISENTO'

print(f'Salario Bruto: R${salario:.2f}')
print(f'Desconto IR {irperct}: R${ir:.2f}')
print(f'Desconto INSS 10%: R${inss:.2f}')
print(f'Deposito de FGTS 11%: R${fgts:.2f}')
print(f'Total de Descontos: R${(ir+inss):.2f}')
print(f'Salario liquido: R${salario-(ir+inss):.2f}')