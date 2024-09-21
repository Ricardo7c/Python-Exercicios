# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input('Qual o seu sexo (M/F)? ')
if letra == 'M':
    print('Seu sexo é Masculino')
elif letra == 'F':
    print('Seu sexo é feminino')
else:
    print('Sexo invalido, digite (M)asculino ou (F)eminino')