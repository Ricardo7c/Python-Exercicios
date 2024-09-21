nota1 = float(input('Ditie a primeira nota: '))
nota2 = float(input('Ditie a segunda nota: '))
nota3 = float(input('Ditie a terceira nota: '))

media = (nota1+nota2+nota3)/3

if media < 7:
    msg = "REPROVADO"
elif media >= 7 and media < 10:
    msg = "APROVADO"
else:
    msg = "APROVADO COM DESTINÇÂO"

print(f'O aluno teve media {media} e foi {msg}')