
def validador(dia, mes, ano):
    ranged = 0
    if data[2] != "/" or data[5] != "/" or dia == 00 or mes == 00:
        print("Formato de data invalido, siga o modelo (dd/mm/aaaa)")
    else:
        if mes == 2:
            if ano % 400 == 0 or ano % 4 == 0:
                ranged = 29
            else:
                ranged = 28
        elif mes in [1,3,5,7,8,10,12]:
            ranged = 31
        elif mes in [4,6,9,11]:
            ranged = 30

    dia_ranged = ranged
    mes_ranged = 12

    if dia <= dia_ranged and mes <= mes_ranged:
        return(mes)
    else:
        print(f'A data {data} é invalida!')


def porextenso(data):

    meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
    return meses[data]


data = input('Digite a data(dd/mm/aaaa): ')

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])


if validador(dia, mes, ano) == mes:
    print(f'{dia} de {porextenso(mes-1)} de {ano}')

