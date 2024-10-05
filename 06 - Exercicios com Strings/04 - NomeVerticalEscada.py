# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.


nome = input('Digite um nome: ').upper()
for letra in range(1, len(nome)+1):
    print(nome[:letra])