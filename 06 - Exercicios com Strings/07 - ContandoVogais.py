texto = input('Digite o texto: ')

vogal = espacos = 0
for c in texto:
    if c in 'aeiou':
        vogal += 1
    elif c in " ":
        espacos += 1

print(f'O texto tem {vogal} vogais')
print(f'O texto tem {espacos} espaços')