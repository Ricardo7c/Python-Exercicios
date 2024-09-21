# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

maior = 0
menor = 0
soma = 0
while True:
    num = int(input('Digite um numero: '))
    if num > 1000 or num < 0:
        print('Valor invalido, tente novamente!')
    else:
        soma += num
        
        if num > maior:
            maior = num
        elif num < menor or menor == 0:
            menor = num
            
        res = input('Quer continuar S/N? ').upper()
        if res in 'N':
            break

print(f'O maior foi: {maior}')
print(f'O menor foi: {menor}')
print(f'A soma dos numeros foi: {soma}')