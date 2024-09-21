# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
# cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
# considere latas cheias.

area = float(input('Qual o tamanho da area a ser pintada: '))
lt = (area/6)+((area/6)*0.10)
litros = lt
latas = 0

while litros > 0:
    latas = latas+1
    litros = litros-18

print(f'Você vai precisar de {latas} latas de 18lt que vai custar R${latas*80}')
print('Ou')

litros = lt
latinha = 0

while litros > 0:
    latinha = latinha+1
    litros = litros-3.6

print(f'Você vai precisar de {latinha} latinhas de 3.6lt que vai custar R${latinha*25}')

litros = lt
latas = 0
latinha = 0

while litros > 18:
    latas = latas+1
    litros = litros-18
while litros > 0:
    latinha = latinha+1
    litros = litros - 3.6 

print('Ou')
print(f'Você vai precisar de {latas} latas e {latinha} latinha. que vai custar R${(latas*80)+(latinha*25)}')