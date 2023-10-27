# Primeiras soluções

!!! pdf
    ![](../slides-inicio.pdf)

Vimos na parte expositiva que a mochila binária é um problema complexo e vamos tentar algumas soluções simples para sua resolução. Duas soluções razoáveis e úteis são

1. selecionar os objetos mais caros primeiro. Se houver empate, selecione o de menor índice primeiro.
2. selecionar os objetos mais leves primeiro. Se houver empate, selecione o de menor índice primeiro.

Em todos os algoritmos (e implementações deste módulo receberemos como argumentos:

1. `N` - número de objetos
1. `C` - capacidade máxima da nossa mochila
1. `V` - array com o valor de cada objeto
1. `P` - array com o peso de cada objeto

A saída de cada algoritmo será

1. `O` - array de `VERDADEIRO/FALSO` indicando se o objeto `I` foi selecionado
2. `VALOR_TOTAL`
3. `PESO_TOTAL`, que deverá ser menor que `C`

## Mais caro primeiro

A ideia desta heurística é não deixar nenhum objeto valioso para trás! Por isso vamos ser ganaciosos e pegar **primeiro os objetos mais caros**! Se um objeto valioso não couber passamos para os mais baratos e prosseguimos até examinar todos objetos.


!!! tip
    Repare que aqui usaremos a mesma ideia do *SLEXSORT*: ordenamos um array de índices com base no valor de outro array (peso ou valor).  

!!! exercise long
    Escreva abaixo um algoritmo em pseudo-código para implementar a heurística descrita acima. 

    !!! answer
        ```
        MAIS_CARO(N, C, V, P)

        IDS <- NOVO_ARRAY(N) TAL QUE IDS[I] = I
        O <- NOVO_ARRAY(N) INICIALIZADO COM FALSO

        ORDENA IDS DECRESCENTE USANDO COMO CHAVE O ARRAY V
        
        PESO_TOTAL <- 0
        VALOR_TOTAL <- 0

        PARA CADA I DE 0 ATÉ N-1 FAÇA
            SE P[IDS[I]] + PESO_TOTAL < C ENTÃO
                O[IDS[I]] = VERDADEIRO
                PESO_TOTAL <- PESO_TOTAL + P[IDS[I]] 
                VALOR_TOTAL <- VALOR_TOTAL + V[IDS[I]]
            FIM
        FIM

        DEVOLVA O
        ```

!!! progress 
    Continuar

No algoritmo acima o passo `ORDENAR IDS USANDO COMO CHAVE O ARRAY V` usa a ideia de **ordenação indireta**. Ao invés de ordenar `IDS` por seu valor, o faremos usando o valor de segundo array. Quando formos comparar os índices `I` e `J` de `IDS` faremos a comparação entre `V[IDS[I]` e `V[IDS[J]]`. Ou seja, no fim `IDS` contém os índices de elementos de `V` tal que a ordem desses elementos é (de)cresente. 

!!! tip
    Esse truque é muito útil quando precisamos ordenar uma lista de elementos mas não podemos mexer no array/lista que guarda esses elementos.

!!! exercise long
    Quantos passos são feitos neste algoritmo? Qual é a operação mais cara feita?

    !!! answer
        A operação mais cara é a ordenação, que faz uma quantidade de passos proporcional a $n\log n$.


## Mais leve primeiro

Vamos testar uma abordagem oposta: **quantidade agora é o foco**. Por isso vamos ser práticos e pegar **o maior número de objetos possível**! Começaremos agora pelos objetos mais leves e vamos torcer para que a quantidade grande de objetos selecionados resulte em uma mochila com alto valor.

!!! exercise long
    Escreva abaixo um algoritmo em pseudo-código para implementar a heurística descrita acima. 

    !!! answer
        ```
        MAIS_LEVE(N, C, V, P)

        IDS <- NOVO_ARRAY(N) TAL QUE IDS[I] = I
        O <- NOVO_ARRAY(N) INICIALIZADO COM FALSO

        ORDENA IDS CRESCENTE USANDO COMO CHAVE O ARRAY P
        
        PESO_TOTAL <- 0
        VALOR_TOTAL <- 0

        PARA CADA I DE 0 ATÉ N-1 FAÇA
            SE P[IDS[I]] + PESO_TOTAL < C ENTÃO
                O[IDS[I]] = VERDADEIRO
                PESO_TOTAL <- PESO_TOTAL + P[IDS[I]] 
                VALOR_TOTAL <- VALOR_TOTAL + V[IDS[I]]
            FIM
        FIM

        DEVOLVA O
        ```

!!! progress 
    Continuar

Você deve ter percebido que as mudanças foram mínimas! Isso ocorre pois só mudamos o critério de preenchimento da mochila. O algoritmo em sí é o mesmo.

## Analisando nossas soluções

!!! exercise long
    Crie uma entrada em que a heurística do mais valioso seja muito melhor que a do mais leve. Escreva abaixo as saídas de cada programa.

!!! exercise long
    Crie uma entrada em que a heurística do mais leve seja muito melhor que a do mais valioso. Escreva abaixo as saídas de cada programa.

!!! exercise long
    Com base nas suas respostas acima, em quais situações a heurística do mais valioso é melhor?

!!! exercise long
    Com base nas suas respostas acima, em quais situações a heurística do mais leve é melhor?

Agora que já entendemos melhor nossas soluções, siga para a implementação na [página da APS](aps.md)
