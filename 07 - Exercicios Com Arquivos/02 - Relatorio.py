
dicionario = {}

with open('02 - usuarios.txt', 'r') as usuarios:
    for usuario in usuarios:
        if ' ' in usuario:
            chave, valor = usuario.split(' ', 1)

            chave = chave.strip()
            valor = valor.strip()

            dicionario[chave] = valor


print(dicionario)