# Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
# Atributos: Nome, Fome, Saúde e Idade b.
# Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
# Obs: Existe mais uma informação que devemos levar em consideração, 
# o Humor do nosso tamagushi, este humor é uma combinação entre os atributos
# Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo
# para armazenar esta informação por que ela pode ser calculada a qualquer momento.

class tamagushi:
    def __init__(self, nome, fome, saude, idade) -> None:
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novoNome):
        self.nome = novoNome

    def alterarFome(self, nFome):
        self.fome = nFome

    def alterarSaude(self, nSaude):
        self.saude = nSaude

    def alterarIdade(self, nIdade):
        self.idade = nIdade  

    def humor(self):
        humor = (self.saude+self.fome)/2
        if humor >= 80:
            return 'Feliz'
        elif humor < 80 and humor >= 50:
            return 'Tranquilo'
        elif humor < 50 and humor >= 30:
            return 'Chatiado'
        else:
            return 'Mal humorado'
    
    
    def mostrarStatus(self):
        print(f'Nome: {self.nome}')
        print(f'Fome: {self.fome}%')
        print(f'Saude: {self.saude}%')
        print(f'Idade: {self.idade} anos')
        print(f'Humor: {self.humor()}')
        print('------------------------')


x = tamagushi('Wally', 55, 60, 5)

x.mostrarStatus()
x.alterarFome(20)
x.alterarSaude(21)
x.mostrarStatus()