# Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, 
# se seu argumento for zero ou negativo.

def verificar(x):
    if x > 0:
        return 'POSITIVO!'
    else:
        return 'NEGATIVO!'
    
num = int(input('Digite um numero: '))

print(verificar(num))