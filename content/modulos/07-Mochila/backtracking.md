# Encontrando a melhor solução com Backtracking

!!! pdf
    ![](../slides-backtracking.pdf)


Neste roteiro iremos responder à pergunta 

> Dada uma configuração da mochila com as variáveis abaixo, conseguimos uma solução com valor maior que *X*?

1. `N` - número de objetos
1. `C` - capacidade máxima da nossa mochila
1. `V` - array com o valor de cada objeto
1. `P` - array com o peso de cada objeto

Vamos rever algumas características do nosso problema:

!!! exercise long
    Em uma mochila com 13 objetos, quantas são soluções possíveis?

    !!! answer
        São $2^13$ soluções possíveis. Note que dependendo das outras variáveis nem todas essas soluções são viáveis. Ou seja, dessas soluções uma porção pode ter peso maior que `C`.

A cada passo do algoritmo decidimos se selecionamos ou não o objeto atual. Se selecionamos, resolvemos um novo problema da mochila com capacidade menor (em função do objeto que acabamos de selecionar) e com somente os objetos restantes. Se não mantemos a capacidade e eliminamos o objeto atual da lista de objetos.

!!! exercise long
    Suponha que já escolhemos $i-1$ objetos e estamos decidindo se selecionamos o objeto $i$, de peso $10$ e valor $5$. Nossa mochila ainda tem $50$ de capacidade e o valor atual é $43$. Os objetos selecionados estão colocados em um array `O`.

    Se desejarmos **selecionar** o objeto $i$, como nossa solução parcial será modificada?

    !!! answer
        Precisamos setar `O[i] = VERDADEIRO`, diminuir a capacidade da mochila em $10$ (resultando em $40$ restantes) e aumentar o valore atual em $5$ (resultando em valor $48$).


!!! exercise long
    Suponha que já escolhemos $i-1$ objetos e estamos decidindo se selecionamos o objeto $i$, de peso $10$ e valor $5$. Nossa mochila ainda tem $50$ de capacidade e o valor atual é $43$. Os objetos selecionados estão colocados em um array `O`.

    Se desejarmos **não selecionar** o objeto $i$, como nossa solução parcial será modificada?

    !!! answer
        Precisamos somente setar `O[i] = FALSO`. Como o objeto não foi selecionado, capacidade e valor atual não se modificam.


    
!!! progress
    Continuar


Algoritmos de enumeração exaustiva necessitam de uma técnica chamada **Backtracking** para memorizar quais soluções já foram tentadas e quais ainda não foram. Essa técnica consiste em criar algoritmos recursivos que seguem um modelo mais ou menos fixo. Veja abaixo esse modelo:

```
BACKTRACKING(...., N, SP, I)
    SE I = N ENTÃO
        # AQUI SP JÁ É UMA SOLUÇÃO COMPLETA, ENTÃO PODEMOS DEVOLVÊ-LA
        DEVOLVA UMA CÓPIA DE SP
    FIM

    PARA CADA ESCOLHA POSSÍVEL NA ITERAÇÃO I FAÇA
        # O LOOP ACIMA JÁ CHECA SE AS ESCOLHAS RESPEITAM AS RESTRIÇÕES
        ADICIONE ESSA ESCOLHA EM SP

        BACKTRACKING(...., N, SP, I+1)

        REMOVA ESSA ESCOLHA DE SP

    FIM

    DEVOLVA A MELHOR SOLUÇÃO RETORNADA NO LOOP ACIMA
```

- `N` - tamanho do problema (e também o número máximo de chamadas recursivas que faremos, que é igual ao número de decisões que o algoritmo toma para construir uma solução)
- `SP` - solução parcial levando em conta somente as `I-1` primeiras iterações
- `I` - iteração atual do algoritmo
- o último passo do algoritmo requer que guardemos a melhor solução dentre as tentadas nas chamadas recursivas. **Não é necessário alocar um array para isso**.


O seu trabalho hoje será interpretar isso no contexto da *Mochila binária*.

!!! exercise long
    Adapte o modelo acima para resolver o problema da Mochila. Leve em conta os seguintes pontos
    
    - solução parcial compreende três coisas: `Op`, `Cp` e `Vp` contendo os objetos selecionados até o momento, seu peso total e valor total
    - `i` representa o objeto atual, que iremos selecionar ou não

    !!! answer
        Será feito na lousa depois de um tempo tentando aqui. Use o botão "Editar" para ajeitar sua solução depois disso. 

Acabou? Tente implementar seu algoritmo seguindo [as instruções na página da APS](aps.md).


