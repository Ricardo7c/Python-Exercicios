# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
# para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
# compradas e o preço total.

area = int(input('Qual o tamanho da area a ser pintada: '))
litros = area/3
latas = 1
while litros > 18:
    latas = latas+1
    litros = litros-18

print(f'Você vai precisar de {latas} latas que vai custar R${latas*80}')