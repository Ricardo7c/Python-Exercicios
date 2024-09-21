# Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro
# de faixas válidas.

class Tv:
    def __init__(self, canal, volume) -> None:
        self.volume = volume
        self.Canal = canal

    def trocarCanal(self, novoCanal):
        if novoCanal > 0 and novoCanal <= 200:
            self.Canal = novoCanal
        else:
            print('Canal digitado é invalido!')

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print('Volume maximo!')

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print('Mudo ativado!')

    def mostrarTv(self):
        print(f'Canal: {self.Canal} | Volume: {self.volume}')
        print('________________________________')

tv = Tv(13, 33)

tv.mostrarTv()
tv.diminuirVolume()
tv.trocarCanal(43)
tv.mostrarTv()