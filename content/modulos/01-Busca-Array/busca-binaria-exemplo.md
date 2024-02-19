# Busca binária (I)

Agora que vimos na aula expositiva a intuição da busca binária vamos focar em formalização como algoritmo. Retomando, a proposta foi usar a seguinte ideia:

`BUSCA_BINARIA_BUG(A)`

1. seleciona o elemento na posição exatamente no meio do vetor
2. se esse elemento for `0`, continua procurando na metade da da direita do vetor 
3. se esse elemento for `1`, continua procurando na metade da esquerda do vetor
4. repete esse procedimento até encontrar um elemento que é `1` e tem um vizinho que é `0`.

Vamos começar simulando essas ideias para entender melhor o algoritmo.

!!! exercise choice
    Dado o array `[0, 0, 0, 1, 0, 1]`, conseguimos aplicar a busca binária nele?

    - [ ] SIM
    - [ ] NÃO, pois ele tem número par de elementos. Logo não temos um elemento exatamente no meio.
    - [x] NÃO, pois ele não está ordenado

    !!! answer
        O fato do tamanho ser par não muda a ideia do algoritmo. Poderíamos usar tanto o elemento `0` como o `1` (ambos no meio do vetor) na divisão que teríamos o mesmo comportamento. Porém, como ele não está ordenado não podemos descartar metade dos valores. 

!!! cuidado
    Todos os intervalos nessa seção são abertos no fim. Ou seja, o intervalo `0-3` contém os índices `0,1,2`. 

!!! exercise long
    `A = [0, 0, 0, 0, 0, 1, 1]`

    Qual seria o índice que é usado para executar o passo 1 de nossa intuição de algoritmo? Após esse passo, qual seriam os índices da parte de `A` que não contém o valor procurado? E os índices da parte que contém o valor procurado?
    
    !!! answer
        A quebra será feita no índice `3` (com valor `A[3] = 0`). Como procuramos um `1` e `A[3] = 0`, sabemos o intervalo de índices `0` até `4` **não contém** `1`. 

        Logo, a parte que **pode conter** um `1` começa em `4` e vai até `TAMANHO(A) = 7`.

!!! exercise long
    Continuemos considerando o mesmo `A = [0, 0, 0, 0, 0, 1, 1]`, mas agora passamos a segunda iteração: simularemos o algoritmo no intervalo `4-7`.

    Qual seria o índice usado na comparação do passo 1? Qual o intervalo que será jogado fora? E o que será mantido para a próxima iteração? 

    !!! answer
        Será usado o índice `5` na comparação (`(4 + 7 - 1) / 2 = 5`). Dessa ver conseguimos jogar fora somente o índice `6` (intervalo `6-7`). Ainda manteremos no algoritmo o intervalo `4-6`. 

        Fazemos isso pois queremos, dentro das repetições, o elemento mais à esquerda. Logo, se o valor é encontrado descartamos tudo o que está à direita mas mantemos o índice atual. 

!!! exercise long
    Continuemos considerando o mesmo `A = [0, 0, 0, 0, 0, 1, 1]`, mas agora passamos a terceira iteração: simularemos o algoritmo no intervalo `4-6`.

    Qual seria o índice usado na comparação do passo 1? Qual o intervalo que será jogado fora? E o que será mantido para a próxima iteração? 

    !!! answer
        Será usado o índice `4` na comparação (`(4 + 6 - 1) / 2 = 4,5`). Como `A[4] != 1`, jogamos fora o intervalor `4-5` somente. Com isso, ficamos somente com um intervalo de um valor `5-6` no algoritmo. 
        
Chegamos ao fim do algoritmo: temos um intervalo que só contém um número! Ou ele é um `1` (o que buscamos) ou o valor não foi encontrado no vetor. 

## Formalizando a simulação

Simular é importante para verificarmos se entendemos como o algoritmo funciona. Vamos então examiná-lo por partes aqui. Em toda iteração temos

- um intervalo de índices que queremos analisar
- o índice da metade do intervalo

Uma maneira de ir construindo o algoritmo aos poucos é nomear esses conceitos. 

!!! exercise long 
    Escreva abaixo o valor das variáveis abaixo para cada iteração do algoritmo. Ou seja, releia as perguntas anteriores e, para cada uma, identifique na resposta as variáveis abaixo. 

    - `INICIO` - índice do primeiro elemento do intervalo
    - `FIM` - índice do último elemento dentro do intervalo
    - `MEIO`- índice do elemento na metade do intervalo


    !!! answer
        Iteração 1: 
        - `INICIO` - 0
        - `FIM` - 7
        - `MEIO`- 3

        Iteração 2: 
        - `INICIO` - 4
        - `FIM` - 7
        - `MEIO`- 5

        Iteração 3: 
        - `INICIO` - 4
        - `FIM` - 6
        - `MEIO`- 4
    
        Tecnicamente temos uma iteração 4 com um intervalo de um número só:
        - `INICIO` - 5
        - `FIM` - 6
        - `MEIO`- 5

!!! exercise long
    Escreva abaixo a expressão usada para calcular `MEIO`

    !!! answer
        `(INICIO + FIM - 1) / 2` arredondado para baixo

!!! exercise long
    Como vimos na simulação, o algoritmo acabou quando chegamos em um intervalo com um só elemento. Como você escreveria essa expressão usando as variáveis `INICIO` e `FIM`?

    !!! answer
        `INICIO = FIM - 1` representa um intervalo com um só elemento.

!!! exercise long
    Tente escrever o algoritmo para a busca binária abaixo. Iremos fazê-lo na lousa no fim do período de discussão.

    Quando acabarmos atualize sua resposta e escreva comentários que quiser abaixo. 
