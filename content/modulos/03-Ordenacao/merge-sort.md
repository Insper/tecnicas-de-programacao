# Merge Sort

Vamos olhar agora para a seguinte ideia:

1. divida o vetor em duas metades
2. ordene a metade da direita
3. ordene a metade da esquerda
4. combine as duas metades ordenadas tal que agora o vetor inteiro esteja ordenado

## Juntando arrays já ordenados (`MERGE`)

Os passos acima claramente tem a ideia de um algoritmo recursivo: primeiro fazemos a ordenação (independente) de duas metades e depois combinando esses resultados. Logo, o único passo que ainda não está especificado o suficiente é o passo `4`: combinar dois arrays ordenados em um único array ordenado.

Vamos começar tentando explicar como fazemos esse processo manualmente.

!!! exercise long 
    Vejamos um primeiro exemplo. Explique como você combinaria os elementos de `A1` e `A2` abaixo para produzir um array `A` ordenado. 
    
    - `A1 = [ 1 3 5 7 ]`
    - `A2 = [ 2 4 6 8 ]`

    A ideia aqui é tentar descrever o passo a passo que você faria mesmo que isso não funcione para todos os arrays possíveis

    !!! answer
        Uma resposta possível seria: "começamos com o primeiro elemento de A1 e vamos alternando pegar o próximo elemento de A2 e A1 até acabarem. A ordem de pegar os elementos fica "A1[0], A2[0], A1[1], A2[1], .....`.


!!! exercise long 
    Vejamos um primeiro exemplo. Explique como você combinaria os elementos de `A1` e `A2` abaixo para produzir um array `A` ordenado. 
    
    - `A1 = [ 1 2 3 5 ]`
    - `A2 = [ 4 6 8 ]`

    A ideia aqui é tentar descrever o passo a passo que você faria mesmo que isso não funcione para todos os arrays possíveis

    !!! answer
        Uma resposta possível seria: "Como os três primeiros de A1 são menores que o primeiro de A2, colocamos eles primeiro em A. Depois é só alternar entre A2[0], A1[3], A2[1] ...."


!!! exercise long 
    Vejamos um primeiro exemplo. Explique como você combinaria os elementos de `A1` e `A2` abaixo para produzir um array `A` ordenado. 
    
    - `A1 = [ 3 5 7 ]`
    - `A2 = [ 1 2 5 ]`

    A ideia aqui é tentar descrever o passo a passo que você faria mesmo que isso não funcione para todos os arrays possíveis

    !!! answer
        Uma resposta possível seria: "dessa vez começamos por A2, pegando os dois primeiros elementos. Então tomamos 3 de `A1` e tem empate: podemos pegar os dois 5 em qualquer ordem. Por fim, o `7` de `A1` é selecionado."


Agora que fizemos esse processo manualmente, vamos simular esse processo de maneira mais estruturada para um novo exemplo. Vamos determinar cada elemento de `A` no passo a passo, mostrando os valores intermediários de `A1` e `A2`. Usaremos as seguintes variáveis:

- `A` - array ordenado final, `TAMANHO(A) = TAMANHO(A1) + TAMANHO(A2)`
- `A1` e `A2` - sub arrays ordenados
- `K` - índice de `A` que será preenchido na iteração atual. Começa em `0`
- `I` - índice do menor elemento de `A1` que ainda não foi colocado em `A`. Começa em `0`
- `J` - índice do menor elemento de `A2` que ainda não foi colocado em `A`. Começa em `0`

Na sequência de exercícios abaixo, só clique "Progress" após responder **e entender a resposta correta**.

!!! exercise long
    
    - `A = [ VAZIO VAZIO VAZIO VAZIO VAZIO VAZIO VAZIO VAZIO ]` 
    - `A1 = [ 4 4 7 8 ]`
    - `A2 = [ 1 3 5 6 ]`
    - `K = 0`
    - `I = 0`
    - `J = 0`

    Qual será o elemento colocado em `A[K]`? Escreva abaixo os novos valores de `A, K, I, J`.

    !!! answer
        Colocamos `1` em `A`, pois ele é o menor elemento dentre `A1[I]` e `A2[J]`.

        - `A = [ 1 VAZIO VAZIO VAZIO VAZIO VAZIO VAZIO VAZIO ]` 
        - `A1 = [ 4 4 7 8 ]`
        - `A2 = [ 1 3 5 6 ]`
        - `K = 1`
        - `I = 0`
        - `J = 1`

!!! progress
    Continuar
    
!!! exercise long
    
    - `A = [ 1 VAZIO VAZIO VAZIO VAZIO VAZIO VAZIO VAZIO ]` 
    - `A1 = [ 4 4 7 8 ]`
    - `A2 = [ 1 3 5 6 ]`
    - `K = 1`
    - `I = 0`
    - `J = 1`


    Qual será o elemento colocado em `A[K]`? Escreva abaixo os novos valores de `A, K, I, J`.

    !!! answer
        Colocamos `3` em `A`, pois ele é o menor elemento dentre `A1[I=0]` e `A2[J=1]`.

        - `A = [ 1 3 VAZIO VAZIO VAZIO VAZIO VAZIO VAZIO ]` 
        - `A1 = [ 4 4 7 8 ]`
        - `A2 = [ 1 3 5 6 ]`
        - `K = 2`
        - `I = 0`
        - `J = 2`

!!! progress
    Continuar

!!! exercise long
    
    - `A = [ 1 3 VAZIO VAZIO VAZIO VAZIO VAZIO VAZIO ]` 
    - `A1 = [ 4 4 7 8 ]`
    - `A2 = [ 1 3 5 6 ]`
    - `K = 2`
    - `I = 0`
    - `J = 2`


    Qual será o elemento colocado em `A[K]`? Escreva abaixo os novos valores de `A, K, I, J`.

    !!! answer
        Colocamos `4` em `A`, pois ele é o menor elemento dentre `A1[I=0]` e `A2[J=2]`.

        - `A = [ 1 3 4 VAZIO VAZIO VAZIO VAZIO ]` 
        - `A1 = [ 4 4 7 8 ]`
        - `A2 = [ 1 3 5 6 ]`
        - `K = 3`
        - `I = 1`
        - `J = 2`



!!! progress
    Continuar

!!! exercise long

    - `A = [ 1 3 4 VAZIO VAZIO VAZIO VAZIO VAZIO ]` 
    - `A1 = [ 4 4 7 8 ]`
    - `A2 = [ 1 3 5 6 ]`
    - `K = 3`
    - `I = 1`
    - `J = 2`

    Qual será o elemento colocado em `A[K]`? Escreva abaixo os novos valores de `A, K, I, J`.

    !!! answer
        Colocamos `4` em `A`, pois ele é o menor elemento dentre `A1[I=1]` e `A2[J=2]`.

        - `A = [ 1 3 4 4 VAZIO VAZIO VAZIO VAZIO ]` 
        - `A1 = [ 4 4 7 8 ]`
        - `A2 = [ 1 3 5 6 ]`
        - `K = 4`
        - `I = 2`
        - `J = 2`



!!! progress
    Continuar

!!! exercise long

    - `A = [ 1 3 4 4 VAZIO VAZIO VAZIO VAZIO ]` 
    - `A1 = [ 4 4 7 8 ]`
    - `A2 = [ 1 3 5 6 ]`
    - `K = 4`
    - `I = 2`
    - `J = 2`

    Qual será o elemento colocado em `A[K]`? Escreva abaixo os novos valores de `A, K, I, J`.

    !!! answer
        Colocamos `5` em `A`, pois ele é o menor elemento dentre `A1[I=2]` e `A2[J=2]`.

        - `A = [ 1 3 4 4 5 VAZIO VAZIO VAZIO ]` 
        - `A1 = [ 4 4 7 8 ]`
        - `A2 = [ 1 3 5 6 ]`
        - `K = 5`
        - `I = 2`
        - `J = 3`



!!! progress
    Continuar

!!! exercise long

    - `A = [ 1 3 4 4 5 VAZIO VAZIO VAZIO ]` 
    - `A1 = [ 4 4 7 8 ]`
    - `A2 = [ 1 3 5 6 ]`
    - `K = 5`
    - `I = 2`
    - `J = 3`

    Qual será o elemento colocado em `A[K]`? Escreva abaixo os novos valores de `A, K, I, J`.

    !!! answer
        Colocamos `6` em `A`, pois ele é o menor elemento dentre `A1[I=2]` e `A2[J=3]`.

        - `A = [ 1 3 4 4 5 6 VAZIO VAZIO ]` 
        - `A1 = [ 4 4 7 8 ]`
        - `A2 = [ 1 3 5 6 ]`
        - `K = 6`
        - `I = 2`
        - `J = 4`



!!! progress
    Continuar

!!! exercise long

    - `A = [ 1 3 4 4 5 6 VAZIO VAZIO ]` 
    - `A1 = [ 4 4 7 8 ]`
    - `A2 = [ 1 3 5 6 ]`
    - `K = 6`
    - `I = 2`
    - `J = 4`

    Qual será o elemento colocado em `A[K]`? Escreva abaixo os novos valores de `A, K, I, J`.

    !!! answer
        Colocamos `7` em `A`, pois todos os elementos de `A2` já foram colocados.

        - `A = [ 1 3 4 4 5 6 7 VAZIO ]` 
        - `A1 = [ 4 4 7 8 ]`
        - `A2 = [ 1 3 5 6 ]`
        - `K = 7`
        - `I = 3`
        - `J = 4`


!!! progress
    Continuar

!!! exercise long

    - `A = [ 1 3 4 4 5 6 7 VAZIO ]` 
    - `A1 = [ 4 4 7 8 ]`
    - `A2 = [ 1 3 5 6 ]`
    - `K = 7`
    - `I = 3`
    - `J = 4`

    Qual será o elemento colocado em `A[K]`? Escreva abaixo os novos valores de `A, K, I, J`.

    !!! answer
        Colocamos `8` em `A`, pois todos os elementos de `A2` já foram colocados.

        - `A = [ 1 3 4 4 5 6 7 8 ]` 
        - `A1 = [ 4 4 7 8 ]`
        - `A2 = [ 1 3 5 6 ]`
        - `K = 8`
        - `I = 4`
        - `J = 4`


!!! progress
    Continuar

Acabamos a simulação quando chegamos ao fim de ambos `A1` e `A2`. Note algumas coisas importantes:

1. fizemos `N = TAMANHO(A)` iterações. Em cada uma decidimos qual elemento de `A1` ou `A2` iria na posição `K` de `A`
2. É sempre válido que `K = I + J`
3. Precisamos ter um array extra `A` para colocar o resultado mesclado.

Vamos agora sumarizar esse processo em um algoritmo "de verdade":

!!! exercise long
    Escreva abaixo um algoritmo `MERGE(ARR, INICIO, MEIO, FIM, AUX)` que mescla os subarrays ordenados entre `INICIO-MEIO` e `MEIO-FIM`. Você deve usar `AUX` para colocar o trecho completo ordenado e depois copiar isso de volta para `ARR`.

    Fazendo a correspondência com o exemplo acima, temos:

    - `A1` é `ARR[INICIO até MEIO]`
    - `A2` é `ARR[MEIO até FIM]`
    - `A` é `AUX`

    !!! answer
        Faremos esse junto em sala. Use o botão "Editar" para ajeitar sua resposta após a discussão.


## Algoritmo recursivo (Merge Sort)

Agora só falta formalizar o algoritmo inteiro. Vejamos:

!!! exercise long
    Use o algoritmo escrito na seção anterior no algoritmo `MERGE-SORT(A, INICIO, FIM, AUX)`. Não se esqueça de definir um caso base para a recursão.


    !!! answer 

        ```
        MERGE-SORT(A, INICIO, FIM, AUX)
            IF INICIO <= FIM - 1 ENTÃO RETORNE

            MEIO <- (INICIO + FIM) / 2
            MERGE-SORT(A, INICIO, MEIO, AUX)
            MERGE-SORT(A, MEIO, FIM, AUX)

            MERGE(A, INICIO, MEIO, FIM, AUX)
        ```

## Implementação 

Um pontos importante de uma implementação eficiente do MergeSort é gerenciar o array auxiliar `AUX`. 

!!! exercise short
    Qual é o tamanho máximo que `AUX` pode ter? 

    !!! answer
        `N = TAMANHO(A)`

!!! exercise short
    Poderíamos, por exemplo, criar um novo array `AUX` a cada chamada recursiva. Quantas vezes esse array seria criado?

    !!! answer
        `AUX` seria criado `N` vezes, equivalente ao número de nós em uma árvore de altura $log_2 N$. 

Leve em conta essas respostas ao implementar o MergeSort na APS03. 
