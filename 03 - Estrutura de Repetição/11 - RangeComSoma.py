# Altere o programa anterior para mostrar no final a soma dos números.


num1 = int(input('Digite o inicio da contagem: '))
num2 = int(input('Digite o final da contagem: '))
soma = 0
for cada in range((num1+1), num2):
    soma += cada
    print(cada, end=' ')
    
print(f'= {soma}')