# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem 
# Custo, que é o custo de um item antes do imposto. 
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def CalcImposto(preco, imposto):
    valorImposto = preco*(imposto/100)
    novoPreco = preco+valorImposto
    return novoPreco



valor = float(input('Digite o valor do produto: '))
imposto = float(input('Digite a taxa de imposto em %:'))

total = CalcImposto(valor, imposto)

print(f'O total a pagar é: R${total:.2f}')