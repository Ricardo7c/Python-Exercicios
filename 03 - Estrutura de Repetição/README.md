## Estruturas de Repetição (Loops)

-----

### Exercícios de Validação e Iteração Básica

1.  **Validação de Nota**
    Peça uma nota de 0 a 10. Se o valor for inválido, mostre uma mensagem de erro e continue pedindo até que o usuário insira uma nota válida.

2.  **Validação de Usuário e Senha**
    Leia um nome de usuário e uma senha. Não aceite a senha igual ao nome do usuário. Se forem iguais, mostre uma mensagem de erro e repita a solicitação.

3.  **Validação de Informações Pessoais**
    Leia e valide as seguintes informações, pedindo novamente se a validação falhar:

      * **Nome:** deve ter mais de 3 caracteres.
      * **Idade:** deve estar entre 0 e 150.
      * **Salário:** deve ser maior que zero.
      * **Sexo:** 'f' ou 'm'.
      * **Estado Civil:** 's', 'c', 'v' ou 'd'.

4.  **Crescimento Populacional**
    Calcule o número de anos necessários para que a população do país A (80.000 habitantes, 3% de crescimento) ultrapasse ou iguale a população do país B (200.000 habitantes, 1,5% de crescimento).

5.  **Crescimento Populacional (Flexível)**
    Modifique o exercício anterior para que o usuário possa informar as populações e as taxas de crescimento iniciais. Valide a entrada dos dados e permita que a operação seja repetida.

6.  **Impressão de Números**

      * Imprima os números de 1 a 20, um abaixo do outro.
      * Depois, modifique o programa para imprimi-los um ao lado do outro.

7.  **Maior de 5 Números**
    Leia 5 números e informe qual é o maior deles.

8.  **Soma e Média de 5 Números**
    Leia 5 números, calcule e informe a soma e a média deles.

9.  **Números Ímpares**
    Imprima na tela apenas os números ímpares entre 1 e 50.

10. **Intervalo entre Números**
    Receba dois números inteiros e imprima todos os números inteiros que estão entre eles.

11. **Soma do Intervalo**
    Altere o programa anterior para que ele também mostre a soma dos números do intervalo.

12. **Gerador de Tabuada**
    Desenvolva um gerador de tabuada para um número de 1 a 10. A saída deve ser como no exemplo:

    ```
    Tabuada de 5:
    5 x 1 = 5
    5 x 2 = 10
    ...
    5 x 10 = 50
    ```

13. **Cálculo de Potência**
    Peça a base e o expoente. Calcule a potência sem usar a função de potência da linguagem.

14. **Contador de Pares e Ímpares**
    Peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.

15. **Série de Fibonacci (até o n-ésimo termo)**
    Gere a série de Fibonacci até o n-ésimo termo.
    (`1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...`)

16. **Série de Fibonacci (até 500)**
    Gere a série de Fibonacci até que o valor do termo seja maior que 500.
    (`0, 1, 1, 2, 3, 5, ...`)

17. **Cálculo de Fatorial**
    Calcule o fatorial de um número inteiro fornecido pelo usuário.
    Ex.: `5! = 5 * 4 * 3 * 2 * 1 = 120`

18. **Análise de Conjunto de Números**
    Dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

19. **Análise de Conjunto de Números (com Limite)**
    Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

20. **Cálculo de Fatorial (com Loop)**
    Altere o programa do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o número a inteiros positivos e menores que 16.

21. **Verificador de Número Primo**
    Peça um número inteiro e determine se ele é ou não um número primo.

22. **Verificador de Número Primo (Detalhado)**
    Altere o programa anterior para que, caso o número não seja primo, ele informe por quais números ele é divisível.

23. **Gerador de Números Primos**
    Mostre todos os números primos entre 1 e N (N é um número fornecido pelo usuário). O programa também deve mostrar o número de divisões executadas.

24. **Média Aritmética de N Notas**
    Calcule e mostre a média aritmética de N notas.

25. **Classificação de Turma por Idade**
    Peça a idade de N pessoas. Ao final, verifique se a média de idade da turma está entre:

      * 0 e 25 (turma jovem)
      * 26 e 60 (turma adulta)
      * maior que 60 (turma idosa)

26. **Contagem de Votos**
    Em uma eleição com três candidatos, peça o número total de eleitores. Para cada eleitor, peça o voto e, ao final, mostre o número de votos de cada candidato.

27. **Média de Alunos por Turma**
    Calcule a média de alunos por turma. Peça a quantidade de turmas e a quantidade de alunos para cada uma (não pode ter mais de 40 alunos por turma).

28. **Análise de Coleção de CDs**
    Calcule o valor total investido em uma coleção de CDs e o valor médio gasto em cada um. O usuário deve informar a quantidade de CDs e o valor de cada um.

29. **Tabela de Preços (Loja de 1,99)**
    Crie uma tabela de preços para uma loja, com itens de 1 a 50, onde cada item custa R$ 1,99.

    ```
    Lojas Quase Dois - Tabela de preços
    1 - R$ 1.99
    2 - R$ 3.98
    ...
    50 - R$ 99.50
    ```

30. **Tabela de Preços (Panificadora)**
    Com base no preço de um pão, crie uma tabela de preços de 1 a 50 pães. O preço do pão é informado pelo usuário.

31. **Caixa Registradora**
    Implemente uma caixa registradora rudimentar. O programa deve receber os preços das mercadorias (um valor 0 indica o final da compra). Em seguida, mostre o total, pergunte o valor recebido e calcule o troco. O programa deve voltar ao ponto inicial para a próxima compra.

32. **Fatorial Detalhado**
    Calcule o fatorial de um número inteiro fornecido pelo usuário. A saída deve mostrar o cálculo completo.
    Exemplo: `5! = 5 . 4 . 3 . 2 . 1 = 120`

33. **Análise de Temperaturas**
    Leia um conjunto indeterminado de temperaturas. Ao final, informe a menor, a maior e a média das temperaturas.

34. **Verificador de Número Primo**
    Peça um número inteiro e determine se ele é ou não um número primo.

35. **Gerador de Lista de Primos**
    Gere uma lista de todos os números primos entre 1 e um número inteiro fornecido pelo usuário.

36. **Tabuada Personalizada**
    Faça a tabuada de um número, com o início e o fim do intervalo definidos pelo usuário. Verifique se o valor final não é menor que o inicial.

37. **Análise de Dados de Academia**
    Crie um programa que colete o código, altura e peso de clientes de uma academia (a entrada termina quando o código for 0). Ao final, mostre o cliente mais alto, o mais baixo, o mais gordo e o mais magro, além da média de altura e peso da turma.

38. **Reajuste Salarial Anual**
    Um funcionário foi contratado em 1995 com salário inicial de R$ 1.000,00. Em 1996, ele recebeu um aumento de 1,5%. A partir de 1997, o aumento é o dobro do percentual do ano anterior. Calcule o salário atual desse funcionário. Depois, modifique o programa para que o usuário possa informar o salário inicial.

39. **Análise de Altura de Alunos**
    Leia dez conjuntos de dois valores (número do aluno e altura). Encontre e mostre o aluno mais alto e o mais baixo, com suas respectivas alturas.

40. **Estatística de Acidentes de Trânsito**
    Coletar dados de 5 cidades (código, número de veículos, número de acidentes com vítimas). Deseja-se saber:

      * O maior e menor índice de acidentes e a qual cidade pertencem.
      * A média de veículos nas cinco cidades.
      * A média de acidentes em cidades com menos de 2.000 veículos.

41. **Cálculo de Dívida**
    Receba o valor de uma dívida e mostre uma tabela de parcelamento com juros.

      * 1 parcela: 0% de juros
      * 3 parcelas: 10%
      * 6 parcelas: 15%
      * 9 parcelas: 20%
      * 12 parcelas: 25%

42. **Contador de Intervalos**
    Leia uma quantidade indeterminada de números positivos (a entrada termina com um número negativo). Conte quantos deles estão nos intervalos: [0-25], [26-50], [51-75] e [76-100].

43. **Sistema de Pedidos de Lanchonete**
    Implemente um sistema de pedidos. Peça o código e a quantidade de cada item. Calcule e mostre o valor por item e o total do pedido. A entrada de dados termina quando o cliente informar o encerramento.

    | Código | Especificação | Preço |
    | :---: | :---: | :---: |
    | 100 | Cachorro Quente | R$ 1,20 |
    | 101 | Bauru Simples | R$ 1,30 |
    | 102 | Bauru com Ovo | R$ 1,50 |
    | 103 | Hambúrguer | R$ 1,20 |
    | 104 | Cheeseburguer | R$ 1,30 |
    | 105 | Refrigerante | R$ 1,00 |

44. **Análise de Votação**
    Em uma eleição com 4 candidatos, colete os votos (códigos de 1 a 4 para candidatos, 5 para nulo, 6 para branco, 0 para finalizar). Calcule e mostre:

      * Total de votos para cada candidato.
      * Total de votos nulos.
      * Total de votos em branco.
      * Percentual de votos nulos sobre o total de votos.
      * Percentual de votos em branco sobre o total de votos.

45. **Sistema de Notas de Prova**
    Um programa para verificar a nota de alunos em uma prova com 10 questões. O programa deve pedir as respostas de cada aluno, comparar com um gabarito fixo e calcular a nota (1 ponto por acerto). Depois de cada aluno, pergunte se outro aluno vai usar o sistema. Ao final, informe:

      * Maior e menor nota.
      * Total de alunos.
      * Média das notas da turma.
        **Gabarito:** `A, B, C, D, E, E, D, C, B, A`
        *Incremento opcional:* Permita que o professor digite o gabarito.

46. **Ginasta e Notas de Salto**
    Em uma competição de ginástica, cada atleta tem 5 saltos. O programa deve receber o nome do atleta e as 5 distâncias. Elimine o melhor e o pior resultado e calcule a média dos 3 restantes. O programa deve parar quando o nome do atleta não for informado.

47. **Notas de Ginástica**
    Em uma competição de ginástica, um atleta recebe 7 notas de jurados. O programa deve receber o nome do ginasta e as 7 notas. Remova a melhor e a pior nota e calcule a média das 5 restantes.

48. **Número Invertido**
    Peça um número inteiro positivo e mostre-o invertido.
    Ex.: `12376489` =\> `98467321`

49. **Série S = 1/1 + 2/3 + 3/5 + ...**
    Mostre os N termos da série `S = 1/1 + 2/3 + 3/5 + 4/7 + ... + n/m` e imprima a soma final.

50. **Série Harmônica H = 1 + 1/2 + 1/3 + ...**
    Calcule o valor da série harmônica `H = 1 + 1/2 + 1/3 + ... + 1/N` com N termos.

51. **Série S = 1/1 + 2/3 + 3/5 + ...**
    (Repetição) Mostre os N termos da série `S = 1/1 + 2/3 + 3/5 + 4/7 + ... + n/m` e imprima a soma final.
