# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

while True:
    while True:
        nome = input('Digite o seu nome: ')
        if len(nome) > 3:
            break
        else:
            print('O nome deve ter mais de 3 caracteres. tente novamente!')
            print('------------------------------------------------------')
    while True:
        idade = int(input('Digite a sua idade: '))
        if idade > 0 and idade <= 150:
            break
        else:
            print('Valor invalido, tente novamente!')
            print('--------------------------------')
    while True:
        salario = float(input('Digite o seu salario: '))
        if salario > 0:
            break
        else:
            print('Valor invalido, tente novamente!')
            print('--------------------------------')
    while True:
        sexo = input('Qual o seu sexo M/F? ').upper()
        if sexo in 'MF':
            break
        else:
            print('Valor invalido, tente novamente!')
            print('--------------------------------')
    while True:
        estadocivil = input('Qual o seu estado civil S/C/V/D? ').upper()
        if estadocivil in 'SCVD':
            break
        else:
            print('Valor invalido, tente novamente!')
            print('--------------------------------')
    break
print('-------------------------------')
print('Cadastro realizado com sucesso!')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salário: R${salario:.2f}')
print(f'Sexo: {sexo}')
print(f'Estado Civil: {estadocivil}')
print('-------------------------------')