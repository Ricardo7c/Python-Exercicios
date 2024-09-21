# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ')
if letra in "aAeEiIoOuU":
    print(f'{letra} é uma vogal')
else:
    print(f'{letra} é uma consoante')