texto = input('Digite a frase ou palavra: ')

texto = texto.replace(' ', '')

if texto == texto[::-1]:
    print('é um palindromo!')
else:
    print('Não é palindromo!')