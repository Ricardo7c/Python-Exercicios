# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos:
# nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). 
# Faça um programa ou teste interativamente, criando pelo menos dois macacos,
# alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo
# do estomago a cada refeição.
# Experimente fazer com que um macaco coma o outro.
# É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        if isinstance(comida, Macaco):  # Verifica se comida é uma instancia da classe macaco
            self.bucho.extend(comida.bucho) # Junta o conteudo da instancia comida com o conteudo da instancia atual
            self.bucho.append(comida.nome)  # Adiciona o nome da instancia comida ao bucho da instancia atual
        else:
            self.bucho.append(comida)

    def verBucho(self):
        print(f'{self.nome} comeu: {self.bucho}')

    def digerir(self):
        if self.bucho:
            digeriu = self.bucho.pop(0)
            return f'{self.nome} digeriu: {digeriu}'
        else:
            print('Não a nada para digerir!')



m1 = Macaco('Gorila')
m2 = Macaco('UrangoTango')


m1.comer('Banana')
m1.comer('abacate')
m1.digerir()
m1.verBucho()
m2.comer('Pêra')
m2.verBucho()
m1.comer(m2)
m1.verBucho()