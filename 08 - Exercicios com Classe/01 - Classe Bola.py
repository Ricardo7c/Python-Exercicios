# Classe Bola: Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor


class Bola:
    def __init__(self, cor, circunferencia, material) -> None:
        self.cor = cor
        self.circu = circunferencia
        self.material = material

    def trocarCor(self, cor):
        self.cor = cor
    
    def mostraCor(self):
        return self.cor
    

b1 = Bola('Amarela', 23, 'Plastico')

print(b1.mostraCor())
b1.trocarCor('Cinza')
print(b1.mostraCor())
