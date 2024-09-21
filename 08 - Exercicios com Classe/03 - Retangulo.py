# Classe Retangulo: Crie uma classe que modele um retangulo:
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades
# de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade
# de pisos e de rodapés necessárias para o local.


class Retangulo:
    def __init__(self, ladoA, ladoB) -> None:
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarLados(self, ladoA, LadoB):
        self.ladoA = ladoA
        self.ladoB = LadoB

    def mostrarLados(self):
        print(f'Comprimento: {self.ladoA}')
        print(f'Largura: {self.ladoB}')
    
    def calcularArea(self):
        area = self.ladoA*self.ladoB
        return area

    def calcularPerimetro(self):
        perimetro = (self.ladoA+self.ladoB)*2
        return perimetro
    

comprimento = float(input('Digite o comprimento: '))
largura = float(input('Digite a largura: '))

local = Retangulo(comprimento, largura)

local.mostrarLados()

print(f'Sera nescessario: {local.calcularArea()} m2 de Piso')
print(f'e {local.calcularPerimetro()} m de Rodapé')

