# Quick sort

!!! pdf
    ![](../slides.pdf)

Neste atividade vamos explorar o algoritmo *Quick sort*, que é definido pela seguinte ideia em alto nível:

1. escolha um elemento do vetor (pode ser o primeiro). Vamos chamar ele de **pivô**
2. coloque o **pivô** no lugar certo em termos de ordenação.
    - índice `i` tal que todo $A[j] \leq A[i], j < i$
    - índice `i` tal que todo $A[j] > A[i], j > i$
3. ordene a parte à esquerda de `i`
4. ordene a parte à direita de `i`

## Recursão e o algoritmo `QUICK_SORT`

Vamos começar lendo essa descrição e notando uma coisa: parece que temos um algoritmo **Recursivo**! Os passos *3* e *4* são, essencialmente, aplicar ordenação em subarrays à esquerda e à direita do elemento **pivô**. 

!!! exercise long id_quick_base
    Vimos anteriormente que todo algoritmo recursivo tem uma **base**, que é o caso mais simples que sabemos a resposta e não precisamos rechamar o algoritmo. Qual você imagina que seria o caso base para ordenação?

    !!! answer
        Aqui podemos ter duas respostas igualmente válidas:

        1. base ser só o array de um elemento. Como ele só tem um elemento sempre está ordenado. 
        2. base ser composta de dois casos
            - um elemento sozinho, como na anterior
            - dois elementos: aqui podemos simplesmente trocar se o primeiro for maior que o segundo


!!! exercise long id_quick_vezes_divisao_melhor_caso
    Neste exercício vamos assumir que o **pivô** divide o array em dois pedaços exatamente iguais toda vez. Nesse caso, para um array de tamanho `N=32`, quantas vezes precisamos dividir o array em dois pedaços até chegar na base? Em outras palavras, quantas vezes precisamos dividir o veto até chegar em um array de tamanho `1` (ou `2`, dependendo da sua resposta acima)?

    !!! answer
        Se você usou `1` como base, sua resposta será `5`. Se foi `2` seria `4`. Não importa muito o valor aqui, mas sim que é algo parecido com $\log_2 N$. 

!!! tip 
    Você deve estar vendo que não estamos sendo muito precisos em nossas contas. Isso ocorre pois comparamos eficiência de algoritmos para `N` muito grande. Nesses casos, se for $\log_2 N$ ou $\log_2 N - 1$ ou até $5 \times \log_2 N$ não faz muita diferença. O valor de $N$ (para $N$ grande) domina todas essas pequenas flutuações. Nas próximas disciplinas de algoritmos iremos escrever isso formalmente.

!!! exercise long id_quick_vezes_divisao_pior_caso
    Neste exercício vamos assumir que o **pivô** divide o array da pior maneira possível: ele é sempre o menor elemento e fica então com um subarray esquerdo de tamanho `0` e um subarray direito de tamanho `N-1`. Nesse caso, quantas vezes iremos dividir o array até chegar no caso base? 

    !!! answer
        Como não há nenhuma divisão propriamente dita, precisamos selecionar algo próximo de `N` pivôs até chegar no array de tamanho `1` ou `2`.

Nosso algoritmo se chamará `QUICK_SORT(A, INICIO, FIM)`. Ele ordena o trecho que vai de `INICIO` até `FIM` (exclusivo, ou seja, o último elemento do intervalo é `A[FIM-1]`). Os passos *3* e *4* consistem em, basicamente, rechamar `QUICK_SORT` em subarrays definidos pelo resultado dos passos *1* e *2*. A base do algoritmo também na foi definida: se `INICIO = FIM -1` (subarray de tamanho `1`) então o algoritmo só retorna e não faz nada. 


## O pivô nos passos 1 e 2


Os passos *1* e *2* parecem concentrar grande parte da lógica do algoritmo. Eles consistem em **particionar** o array em torno de um elemento **pivô**. Supondo que **pivô** tenha sido movido para a posição `I`, teremos duas partes:

1. uma parte esquerda no intervalo `INICIO` até `I`
2. uma parte direita no intervalo `I+1` até `FIM`

Note que, como o pivô já está na posição correta, ele não entra em nenhum das duas partes. Resta então pensar em como fazer essa partição de modo que, se o lugar certo do pivô é a posição `I`,

- `A[I] >= A[J]` se `I > J`
- `A[I] < A[J]` se `I < J`

Chamaremos os passos *1* e *2* de `PARTICIONA(A, INICIO, FIM)`. Vamos então tentar simular a seguinte ideia para estes passos:

1. escolha o pivô como o elemento `A[INICIO]`
2. vamos usar a variável `LUGAR_PIVO = INICIO` para marcar lugar atual do pivô no subarray `INICIO-FIM`
3. começamos então a percorrer o subarray, usando `J = INICIO+1` até `FIM` para marcar o elemento atual
    1. se o valor do elemento atual for **maior** que o do pivô, não faça nada
    2. se o valor do elemento atual for **menor** que o do pivô, aumente um em `LUGAR_PIVO` e troque o elemento atual com `LUGAR_PIVO`
4. troque o pivô com o elemento em `LUGAR_PIVO`

Como anteriormente, vamos simular esse algoritmo para entender melhor seu funcionamento. 

!!! exercise long id_quick_particiona1
    Simule a ideia do particiona para o seguinte array `A = [ 6 3 1 2 7 5 4 8 ]`. 
    
    - na primeira linha coloque o valor de `A[INICIO]` e `LUGAR_PIVO`.
    - escreva cada iteração do passo 3 em uma linha, indicando o valor de `J` e `LUGAR_PIVO` e escrevendo **maior** ou **menor** conforme os valores do pivô e do elemento atual. Também coloque o array atual se ele for modificado
    - ao fim mostre o valor de `LUGAR_PIVO` e o estado atual de `A`

    !!! answer
        - `LUGAR_PIVO = 0, INICIO = 0, A[INICIO] = 6`
        - `J = 1` -> **menor**, `LUGAR_PIVO = 1, A = [ 6 3 1 2 7 5 4 8 ]`
        - `J = 2` -> **menor**, `LUGAR_PIVO = 2, A = [ 6 3 1 2 7 5 4 8 ]`
        - `J = 3` -> **menor**, `LUGAR_PIVO = 3, A = [ 6 3 1 2 7 5 4 8 ]`
        - `J = 4` -> **maior**, `LUGAR_PIVO = 3, A = [ 6 3 1 2 7 5 4 8 ]`
        - `J = 5` -> **menor**, `LUGAR_PIVO = 4, A = [ 6 3 1 2 5 7 4 8 ]`
        - `J = 6` -> **menor**, `LUGAR_PIVO = 5, A = [ 6 3 1 2 5 4 7 8 ]`
        - `J = 7` -> **maior**, `LUGAR_PIVO = 5, A = [ 6 3 1 2 5 4 7 8 ]`
        - Final: `LUGAR_PIVO = 5, A = [ 4 3 1 2 5 6 7 8 ]`


!!! exercise long id_quick_particiona2
    Simule a ideia do particiona para o seguinte array `A = [ -2 1 2 3 466 2 ]`. 
    
    - na primeira linha coloque o valor de `A[INICIO]` e `LUGAR_PIVO`.
    - escreva cada iteração do passo 3 em uma linha, indicando o valor de `J` e `LUGAR_PIVO` e escrevendo **maior** ou **menor** conforme os valores do pivô e do elemento atual. Também coloque o array atual se ele for modificado
    - ao fim mostre o valor de `LUGAR_PIVO` e o estado atual de `A`

    !!! answer
        - `LUGAR_PIVO = 0, INICIO = 0, A[INICIO] = -2`
        - `J = 1` -> **maior**, `LUGAR_PIVO = 0, A = [ -2 1 2 3 466 2 ]`
        - `J = 2` -> **maior**, `LUGAR_PIVO = 0, A = [ -2 1 2 3 466 2 ]`
        - `J = 3` -> **maior**, `LUGAR_PIVO = 0, A = [ -2 1 2 3 466 2 ]`
        - `J = 4` -> **maior**, `LUGAR_PIVO = 0, A = [ -2 1 2 3 466 2 ]`
        - `J = 5` -> **maior**, `LUGAR_PIVO = 0, A = [ -2 1 2 3 466 2 ]`
        - Final: `LUGAR_PIVO = 0, A = [ -2 1 2 3 466 2 ]`


!!! exercise long id_quick_particiona3
    Simule a ideia do particiona para o seguinte array `A = [ 500 1 2 3 466 2 ]`. 
    
    - na primeira linha coloque o valor de `A[INICIO]` e `LUGAR_PIVO`.
    - escreva cada iteração do passo 3 em uma linha, indicando o valor de `J` e `LUGAR_PIVO` e escrevendo **maior** ou **menor** conforme os valores do pivô e do elemento atual. Também coloque o array atual se ele for modificado
    - ao fim mostre o valor de `LUGAR_PIVO` e o estado atual de `A`

    !!! answer
        - `LUGAR_PIVO = 0, INICIO = 0, A[INICIO] = 500`
        - `J = 1` -> **menor**, `LUGAR_PIVO = 1, A = [ 500 1 2 3 466 2 ]`
        - `J = 2` -> **menor**, `LUGAR_PIVO = 2, A = [ 500 1 2 3 466 2 ]`
        - `J = 3` -> **menor**, `LUGAR_PIVO = 3, A = [ 500 1 2 3 466 2 ]`
        - `J = 4` -> **menor**, `LUGAR_PIVO = 4, A = [ 500 1 2 3 466 2 ]`
        - `J = 5` -> **menor**, `LUGAR_PIVO = 5, A = [ 500 1 2 3 466 2 ]`
        - Final: `LUGAR_PIVO = 5, A = [ 2 1 2 3 466 500 ]`

!!! exercise long id_quick_particiona_algo
    Agora escreva aqui seu algoritmo `PARTICIONA` baseado nas simulações acima. 

    !!! answer
        Discutido em sala. Use a opção "Editar" para modificar suas anotações após a discussão. 


# Juntando tudo

Vamos agora juntar tudo o que fizemos.

!!! exercise long id_quick_sort_algo
    Agora escreva aqui seu algoritmo `QUICK_SORT` baseado nas simulações acima. Use o seguinte esqueleto:

    ```
    QUICK_SORT(A, INICIO, FIM)
        # Escreva abaixo a base do algoritmo (casos com subarray de tamanho 1 e 2)

        # Escreva abaixo a chamada para PARTICIONA
        
        # Escreva abaixo os passos 3 e 4

    ```

    !!! answer
        Discutido em sala. Use a opção "Editar" para modificar suas anotações após a discussão. 
 


!!! tip
    Teste seu algoritmo recursivo com as seguintes entradas:

    - `A = [ 1 ]`
    - `A = [ 2 1 ]`
    - `A = [ 1 2 3 ]`
    - `A = [ 500 1 2 3 466 2 ]`
    - `A = [ 6 3 1 2 7 5 4 8 ]`