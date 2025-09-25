### Estrutura de decisão

1.  **Maior de Dois Números**
    Peça dois números e imprima o maior deles.

2.  **Positivo ou Negativo**
    Solicite um valor e diga se ele é positivo ou negativo.

3.  **Verificador de Gênero**
    Peça para o usuário digitar "F" ou "M" e imprima "Feminino", "Masculino" ou "Sexo Inválido".

4.  **Vogal ou Consoante**
    Verifique se uma letra digitada é uma vogal ou uma consoante.

5.  **Aprovação Escolar**
    Leia duas notas parciais de um aluno, calcule a média e imprima:

      * "Aprovado" se a média for maior ou igual a 7.
      * "Reprovado" se a média for menor que 7.
      * "Aprovado com Distinção" se a média for igual a 10.

6.  **Maior de Três Números**
    Leia três números e mostre o maior deles.

7.  **Maior e Menor de Três Números**
    Leia três números e mostre o maior e o menor deles.

8.  **Produto Mais Barato**
    Pergunte o preço de três produtos e informe qual deles você deve comprar (o mais barato).

9.  **Números em Ordem Decrescente**
    Leia três números e mostre-os em ordem decrescente.

10. **Saudação por Turno**
    Peça ao usuário em que turno ele estuda ("M" para matutino, "V" para vespertino, "N" para noturno). Imprima "Bom Dia\!", "Boa Tarde\!", "Boa Noite\!" ou "Valor Inválido\!".

-----

### Exercícios de Lógica Complexa e Cálculos Detalhados

11. **Reajuste Salarial**
    Crie um programa que calcula o reajuste salarial de um colaborador. O programa deve receber o salário atual e aplicar um aumento baseado na seguinte tabela:

      * Salários até R$ 280,00: aumento de 20%
      * Salários entre R$ 280,00 e R$ 700,00: aumento de 15%
      * Salários entre R$ 700,00 e R$ 1.500,00: aumento de 10%
      * Salários acima de R$ 1.500,00: aumento de 5%

    Ao final, informe o salário antes e depois do reajuste, o percentual e o valor do aumento.

12. **Folha de Pagamento Completa**
    Crie um programa para o cálculo de uma folha de pagamento. Peça o valor da hora e a quantidade de horas trabalhadas no mês. O programa deve calcular:

      * Salário Bruto.
      * Desconto do Imposto de Renda (IR) conforme a tabela:
          * Até R$ 900,00: isento
          * Até R$ 1.500,00: 5% de desconto
          * Até R$ 2.500,00: 10% de desconto
          * Acima de R$ 2.500,00: 20% de desconto
      * Desconto do Sindicato (3%).
      * O depósito do FGTS (11%), que não é descontado do salário do funcionário.
      * O Salário Líquido.

    O programa deve imprimir um relatório detalhado como no exemplo:

    ```
    Salário Bruto: (valor da hora * horas trabalhadas)  : R$ XXXXX,XX
    (-) IR (XX%)                                        : R$ XXXXX,XX
    (-) Sindicato (3%)                                  : R$ XXXXX,XX
    FGTS (11%)                                          : R$ XXXXX,XX
    Total de descontos                                  : R$ XXXXX,XX
    Salário Liquido                                     : R$ XXXXX,XX
    ```

13. **Dia da Semana**
    Leia um número de 1 a 7 e exiba o dia correspondente da semana (1-Domingo, 2-Segunda, etc.). Se o número não estiver no intervalo, mostre "Valor inválido".

14. **Conceito de Aluno**
    Leia duas notas e calcule a média. Atribua um conceito com base na média, de acordo com a tabela abaixo, e mostre as notas, a média e o conceito. Informe se o aluno foi "APROVADO" (Conceito A, B ou C) ou "REPROVADO" (Conceito D ou E).

    | Média de Aproveitamento | Conceito |
    | :---: | :---: |
    | 9.0 a 10.0 | A |
    | 7.5 a 9.0 | B |
    | 6.0 a 7.5 | C |
    | 4.0 a 6.0 | D |
    | 0.0 a 4.0 | E |

15. **Tipos de Triângulo**
    Peça os 3 lados de um triângulo. Primeiro, verifique se os lados podem formar um triângulo. Se sim, informe se ele é **equilátero** (três lados iguais), **isósceles** (dois lados iguais) ou **escaleno** (três lados diferentes).
    **Dica:** A soma de dois lados deve ser sempre maior que o terceiro.

16. **Cálculo de Equação do 2º Grau**
    Peça os valores de $a$, $b$ e $c$ de uma equação do 2º grau ($ax^2 + bx + c$). O programa deve tratar os seguintes casos:

      * Se $a = 0$, a equação não é do 2º grau. Encerre o programa.
      * Calcule o delta ($\\Delta = b^2 - 4ac$).
      * Se $\\Delta \< 0$, não há raízes reais. Encerre o programa.
      * Se $\\Delta = 0$, há apenas uma raiz real. Calcule e informe-a.
      * Se $\\Delta \> 0$, há duas raízes reais. Calcule e informe-as.

17. **Ano Bissexto**
    Peça um ano e informe se ele é bissexto.

18. **Validação de Data**
    Peça uma data no formato dd/mm/aaaa e verifique se ela é válida.

-----

### Exercícios com Lógica de Divisão e Condicionais Aninhadas

19. **Decomposição de Números**
    Leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades.
    Exemplo:

      * 326 = 3 centenas, 2 dezenas e 6 unidades
      * 12 = 1 dezena e 2 unidades
      * 305 = 3 centenas e 5 unidades

20. **Aprovação com Média**
    Peça três notas parciais, calcule a média e imprima:

      * "Aprovado" se a média for maior ou igual a 7.
      * "Reprovado" se a média for menor que 7.
      * "Aprovado com Distinção" se a média for igual a 10.
        Em todos os casos, a média deve ser exibida.

21. **Caixa Eletrônico**
    Crie um programa de caixa eletrônico. O usuário deve informar o valor do saque (entre R$ 10 e R$ 600). O programa deve informar quantas notas de R$ 100, R$ 50, R$ 10, R$ 5 e R$ 1 serão fornecidas.

22. **Par ou Ímpar**
    Peça um número inteiro e diga se ele é par ou ímpar.

23. **Inteiro ou Decimal**
    Peça um número e informe se ele é inteiro ou decimal.

24. **Calculadora e Classificador**
    Leia dois números e pergunte qual operação o usuário quer realizar (+, -, \*, /). Imprima o resultado e classifique-o como:

      * Par ou ímpar
      * Positivo ou negativo
      * Inteiro ou decimal

25. **Investigação de Crime**
    Faça 5 perguntas sobre um crime ("Telefonou para a vítima?", "Esteve no local?", etc.). Com base no número de respostas positivas, classifique a pessoa:

      * **2 respostas:** Suspeita
      * **3 ou 4 respostas:** Cúmplice
      * **5 respostas:** Assassino
      * **Outro:** Inocente

26. **Descontos em Combustível**
    Calcule o valor a ser pago em um posto de gasolina. Peça o tipo de combustível ("A" para Álcool, "G" para Gasolina) e a quantidade em litros. Use a seguinte tabela de descontos:

      * **Álcool:** 3% de desconto até 20 litros; 5% acima de 20 litros.
      * **Gasolina:** 4% de desconto até 20 litros; 6% acima de 20 litros.
      * **Preços:** Álcool = R$ 1,90/litro; Gasolina = R$ 2,50/litro.

27. **Promoção de Frutas**
    Uma fruteira tem uma promoção de Morango e Maçã. Leia a quantidade (em kg) de cada fruta e calcule o valor total. Se a compra total for maior que 8 kg **ou** o valor total ultrapassar R$ 25,00, conceda um desconto de 10%.

      * **Morango:** R$ 2,50/kg (até 5 kg); R$ 2,20/kg (acima de 5 kg)
      * **Maçã:** R$ 1,80/kg (até 5 kg); R$ 1,50/kg (acima de 5 kg)

28. **Promoção de Carnes com Cupom Fiscal**
    O Hipermercado Tabajara tem uma promoção de carnes. Peça ao usuário o tipo e a quantidade (em kg) de carne. Se o pagamento for com o "Cartão Tabajara", conceda um desconto de 5%.

      * **File Duplo:** R$ 4,90/kg (até 5 kg); R$ 5,80/kg (acima de 5 kg)
      * **Alcatra:** R$ 5,90/kg (até 5 kg); R$ 6,80/kg (acima de 5 kg)
      * **Picanha:** R$ 6,90/kg (até 5 kg); R$ 7,80/kg (acima de 5 kg)

    Ao final, exiba um cupom fiscal detalhado com todas as informações da compra.
