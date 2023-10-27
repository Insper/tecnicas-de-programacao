# Branch and Bound

!!! pdf
    ![](slides-branch-bound.pdf)

A ideia de algoritmos de **Branch and Bound** é evitar testar soluções que sabemos que vão ser ruins. A ideia básica é a seguinte:

**Sempre que chegarmos em um objeto, calculamos uma estimativa da solução com os objetos que ainda faltam. Se for melhor que a solução ótima atual continua. Senão devolve a solução ótima atual.**

A estimativa mencionada acima vai sempre **superestimar** o valor da solução atual. Ou seja, podemos errar o valor da solução atual para cima, **mas nunca para baixo**. Veremos duas maneiras de fazer isso neste handout.

## Bound 1: ignorar peso



## Bound 2: mochila fracionária

O algoritmo da mochila fracionário foi apresentado como

1. ordenar por "densidade" (valor / peso)
2. para cada objeto, se couber coloque-o inteiro
3. se não couber, coloque a maior fração possível


!!! exercise long
    Somente um objeto será incluído com valor fracionário. Essa afirmação é verdadeira ou falsa? Dê um contra-exemplo ou prove que é verdade

    !!! answer
        Será feito na lousa


!!! exercise long
    Seja $P_i o_i$ o peso do objeto com valor fracionário e $V_i o_i$ o valor que ele adiciona à mochila. É verdade a seguinte afirmação?

    **Se resolvermos uma mochila fracionária com os objetos $i+1, \dots, N$ e com capacidade $P_i o_i$, a solução ótima terá valor menor que $V_i o_i$.**

    !!! answer
        Será feito na lousa

!!! progress
    Continuar

Esse algoritmo é uma pequena modificação em relação às heurísticas, porém a afirmação acima nos ajuda muito! Ela nos diz duas coisas:

1. para a mochila fracionária, a solução é ótima
2. existe um valor superior para o problema da mochila e ele é rápido de calcular

Com isto em mente, podemos usar a mochila fracionária como um limitante superior para a mochila! Sempre que chegarmos em um objeto calculamos o valor da mochila fracionária com ele mais os restantes. Se for melhor que asolução ótima atual continua. Senão devolve a solução ótima atual. 

## Implementação 

Agora que entendemos o que cada bound faz, siga o guia na [página da APS](aps.md) para fazer as tarefas de implementação.
