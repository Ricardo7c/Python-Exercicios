# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos
# alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = [12, 14, 11, 15, 13, 10, 14, 12, 13, 11, 15, 10, 14, 12, 13, 15, 11, 10, 14, 13, 12, 15, 11, 14, 13, 10, 15, 12, 11, 14]
alturas = [160.5, 172.3, 168.7, 155.2, 180.0, 170.4, 164.6, 177.8, 169.0, 158.3, 165.2, 180.1, 161.7, 174.5, 167.4, 156.8, 162.9, 175.3, 163.4, 179.0, 166.1, 157.7, 161.5, 173.6, 160.2, 172.9, 168.1, 159.4, 164.8, 176.7]

soma = 0
for altura in alturas:
    soma += altura

media = soma/30

alunos = 0
for idade, altura in zip(idades, alturas):
    if idade > 13 and altura < media:
        alunos += 1


print(f'{alunos} alunos com 13 anos tem altura inferior a media')