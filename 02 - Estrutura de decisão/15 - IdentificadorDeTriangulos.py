# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))

if a+b>c and a+c>b and b+c>a:
    if a == b and a == c and b == c:
        print('O Tringalo é Equilátero')
    elif a != b and a !=c and b != c:
        print('O triangulo é Escaleno')
    else:
        print('O Triangulo é isósceles')

else:
    print('os lados não formam um triangulo')