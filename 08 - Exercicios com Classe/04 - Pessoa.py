# Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano
# que nossa pessoa envelhece, sendo a idade dela menor que 21 anos,
# ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        if self.idade <= 21:
            for cada in range (self.idade, 21):
                self.altura += 0.05
        self.idade += anos

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self):
        self.altura

    def mostarPessoa(self):
        print(f'Nome: {self.nome}')
        print(f'idade: {self.idade}')
        print(f'Peso: {self.peso}')
        print(f'altura: {self.altura:.2f}')



p1 = Pessoa('Ricardo', 15, 65, 1.55)

p1.mostarPessoa()
print('--------------')
p1.envelhecer(10)
p1.mostarPessoa()