# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado
# pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10,
# o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:

num = int(input('Montar Tabuada de: '))
inicio = int(input('Começar por: '))
fim = int(input('Terminar em: '))

print(f'Vou montar a tabuada de {num} começando por {inicio} e terminando em {fim}')

for cada in range(inicio, fim+1):
    print(f'{num} x {cada} = {num*cada}')