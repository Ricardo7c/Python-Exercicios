# Classe Quadrado: Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, lado):
        self.lado = lado

    def mostrarLado(self):
        return self.lado
    
    def calcularArea(self):
        area = self.lado**2
        return area
    
q1 = Quadrado(2)

print(q1.mostrarLado())
print(q1.calcularArea())
print('-----------------')
q1.mudarLado(5)
print(q1.mostrarLado())
print(q1.calcularArea())
