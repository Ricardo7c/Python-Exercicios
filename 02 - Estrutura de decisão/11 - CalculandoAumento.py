# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
# e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo
# o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Digite o salario: '))

if salario <= 280:
    aumento = salario*0.20
    percet = "20%"
elif salario > 280 and salario <= 700:
    aumento = salario*0.15
    percet = "15%"
elif salario > 700 and salario <= 1500:
    aumento = salario*0.10
    percet = "10%"
else:
    aumento = salario*0.05
    percet = "5%"

print(f'Salario original: R${salario:.2f}')
print(f'Percentual de aumento: {percet}')
print(f'Valor do aumento: R${aumento:.2f}')
print(f'Novo Salario: R${salario+aumento:.2f}')