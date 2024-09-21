# Faça uma classe chamada bombaCombustível, com no mínimo esses atributos:
# tipoCombustivel, valorLitro, quantidadeCombustivel

# Possua no mínimo esses métodos:
# abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
# abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
# alterarValor( ) – altera o valor do litro do combustível.
# alterarCombustivel( ) – altera o tipo do combustível.
# alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.


class BombaDeCombustivel:
    def __init__(self, tipo, valor, quant):
        self.tipo = tipo
        self.valor = valor
        self.quant = quant

    def abastecerPorValor(self, valor):
        self.quant -= valor/5
        print(f'{valor/5}lts de combustivel foram utilizados.')
        print(f'Valor: R$ {self.quant*valor}')

    def abastecerPorLitro(self, quant):
        if quant < self.quant:
            self.quant -= quant
            print(f'{quant}lts de combustivel foram utilizados.')
            print(f'Valor: R$ {self.valor*quant}')



    def alterarValor(self, valor):
        self.valor = valor

    def alterarCombustivel(self, tipo):
        self.tipo = tipo

    def alterarQuantidadeCombustivel(self, quant):
        self.quant = quant

    def mostrarBomba(self):
        print(f'Restaram {self.quant} na bomba de combustivel')


p1 = BombaDeCombustivel('Gasolina', 5, 100)

p1.abastecerPorLitro(1)
p1.mostrarBomba()