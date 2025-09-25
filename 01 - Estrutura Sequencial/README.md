### Estrutura Sequencial

1.  **"Alô, Mundo\!"**
    Crie um programa que exiba a mensagem "Alô mundo" na tela.

2.  **Exibindo um Número**
    Peça um número ao usuário e imprima a mensagem "O número informado foi [número]".

3.  **Soma de Dois Números**
    Solicite dois números e imprima a soma deles.

4.  **Cálculo de Média**
    Peça as 4 notas bimestrais e mostre a média.

5.  **Conversor de Metros para Centímetros**
    Crie um programa que converta uma medida em metros para centímetros.

6.  **Cálculo da Área de um Círculo**
    Peça o raio de um círculo, calcule e mostre sua área.

7.  **Área do Quadrado e seu Dobro**
    Calcule a área de um quadrado e, em seguida, mostre o dobro dessa área para o usuário.

8.  **Cálculo de Salário Mensal**
    Pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário.

-----

### Exercícios de Conversão e Lógica

9.  **Conversor de Fahrenheit para Celsius**
    Peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    `C = 5 * ((F-32) / 9)`

10. **Conversor de Celsius para Fahrenheit**
    Peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

11. **Operações com Três Números**
    Peça 2 números inteiros e 1 número real. Calcule e mostre:

      * O produto do dobro do primeiro com metade do segundo.
      * A soma do triplo do primeiro com o terceiro.
      * O terceiro elevado ao cubo.

12. **Cálculo de Peso Ideal (Homem)**
    Com base na altura de uma pessoa, construa um algoritmo que calcule seu peso ideal usando a fórmula:
    `(72.7 * altura) - 58`

13. **Cálculo de Peso Ideal (Homem e Mulher)**
    Com a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal usando as seguintes fórmulas:

      * Para homens: `(72.7 * h) - 58`
      * Para mulheres: `(62.1 * h) - 44.7`

-----

### Exercícios com Condicionais e Cálculos Detalhados

14. **João Papo-de-Pescador**
    Crie um programa para calcular a multa de João, que deve pagar R$ 4,00 por quilo de peixe que exceder o limite de 50 quilos. O programa deve:

      * Ler o peso total de peixes.
      * Calcular o excesso de peso.
      * Calcular o valor da multa.
      * Imprimir o excesso e a multa, com as mensagens adequadas.

15. **Folha de Pagamento**
    Crie um programa que calcule o salário líquido de um funcionário, aplicando os seguintes descontos:

      * **Imposto de Renda (IR):** 11%
      * **INSS:** 8%
      * **Sindicato:** 5%
        O programa deve pedir o valor que o funcionário ganha por hora e o número de horas trabalhadas no mês. No final, exiba o salário bruto, o valor pago para cada desconto e o salário líquido.

    Exemplo de saída:

    ```
    + Salário Bruto : R$ [valor]
    - IR (11%) : R$ [valor]
    - INSS (8%) : R$ [valor]
    - Sindicato ( 5%) : R$ [valor]
    = Salário Líquido : R$ [valor]
    ```

-----

### Exercícios com Lógica de Negócios e Arredondamento

16. **Loja de Tintas - Versão 1**
    Faça um programa para uma loja de tintas. O programa deve pedir o tamanho da área a ser pintada em metros quadrados. Considere:

      * A cobertura da tinta é de 1 litro para cada 3 metros quadrados.
      * A tinta é vendida em latas de 18 litros, que custam R$ 80,00.
        Informe ao usuário a quantidade de latas a serem compradas e o preço total.

17. **Loja de Tintas - Versão 2**
    Faça um programa para uma loja de tintas. Peça o tamanho da área a ser pintada em metros quadrados. Considere:

      * A cobertura da tinta é de 1 litro para cada 6 metros quadrados.
      * A tinta é vendida em latas de 18 litros (R$ 80,00) ou galões de 3,6 litros (R$ 25,00).
        Informe ao usuário as quantidades e preços em 3 cenários:

    <!-- end list -->

    1.  Comprando apenas latas de 18 litros.
    2.  Comprando apenas galões de 3,6 litros.
    3.  Misturando latas e galões para minimizar o desperdício, com 10% de folga e arredondando para cima.

18. **Cálculo de Tempo de Download**
    Crie um programa que peça o tamanho de um arquivo (em MB) e a velocidade da Internet (em Mbps). Calcule e mostre o tempo aproximado de download em minutos.
