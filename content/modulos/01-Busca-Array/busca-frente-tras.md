# Buscas básicas

Já fizemos busca por valores em um Array quando implementamos o [Map](../01-ADT/map.md). Vamos então criar dois algoritmos para resolver esse problema em específico: buscar o primeiro `1` em vetores com o abaixo.

![](array-bug-1.png)

## Começando do início

Temos a tendência de começar a percorrer um `Array` pelo índice `0`. Vamos explorar a busca 

!!! exercise long
    Escreva um algoritmo `ENCONTRA_BUG(A)` que encontra o índice do primeiro commit com problema. Você deve iniciar a busca pelo índice 0.

    !!! answer
        ```
        ENCONTRA_BUG(A)

            I := 0
            ENQUANTO A[I] != 1 E I < TAMANHO(A) FAÇA
                I := I + 1
            FIM

            DEVOLVA I
        ```



## Começando do fim

Uma solução igualmente válida é começar pelo fim do `Array`. Não há nada que torne essa escolha melhor ou pior do que a anterior, então iremos fazê-la também. 

!!! tip
    Em algoritmos é comum explorar várias ideias para resolver o mesmo problema, mesmo que elas sejam equivalentes ou que não existe uma razão particular para escolher uma ou outra.

!!! exercise long
    Escreva um algoritmo `ENCONTRA_BUG_FIM(A)` que encontra o índice do primeiro commit com problema. Você deve iniciar a busca pelo índice `TAMANHO(A) - 1` e buscar por um valor `0`.

    !!! answer
        ```
        ENCONTRA_BUG_FIM(A)

            I := TAMANHO(A) - 1
            ENQUANTO A[I] != 0 E I >= 0 FAÇA
                I := I - 1
            FIM

            DEVOLVA I+1
        ```


!!! exercise long 
    Por conta das características do nosso problema o algoritmo pode ser um pouco mais simples que a busca anterior. O que você notou de diferente em relação ao `INDEXOF` feito na atividade do *Map*?

    !!! answer
        Discutido em sala. Use o botão `editar` para adicionar seu resumo da discussão após ela acontecer. 
