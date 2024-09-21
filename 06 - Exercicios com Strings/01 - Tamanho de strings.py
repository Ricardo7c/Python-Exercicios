
texto1 = input('Digite o primeiro texto: ')
texto2 = input('Digite o segundo texto: ')

print('Comparando duas strings')

print(f'string 1: {texto1}')
print(f'string 2: {texto2}')
print(f'Tamanho de {texto1}: {len(texto1)} caracteres')
print(f'Tamanho de {texto2}: {len(texto2)} caracteres')

if len(texto1) == len(texto2):
    print('Os textos tem tamanhos iguais')
else:
    print('Os textos tem tamanhos diferentes')

if texto1 == texto2:
    print('O conteudo é o mesmo')
else:
    print('Os conteudos são diferentes')
