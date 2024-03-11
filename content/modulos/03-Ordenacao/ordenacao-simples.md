# 01 - Primeiros Algoritmos (simples) de ordenação

Nessa primeira atividade vamos entender um algoritmo simulando seu funcionamento. 

## Bubble Sort

```
BUBBLE_SORT(A)
    N ← TAMANHO(A)
    FEZ_TROCA ← VERDADEIRO

    ENQUANTO FEZ_TROCA FAÇA
        FEZ_TROCA ← FALSO
        PARA CADA I ← 0 ATÉ N-1 FAÇA
            SE A[I] > A[I+1] ENTÃO
                TROQUE OS VALORES DE A[I] E A[I+1]
                FEZ_TROCA ← VERDADEIRO
            FIM
        FIM
    FIM
```

Vamos primeiro começar simulando a primeira passagem no loop `ENQUANTO`. 

!!! exercise long id_bubble_simula0
    Simule a primeira iteração do loop `ENQUANTO` para `A = [  3, 4, 2 , 5, 77, 8, 12 ]`. Coloque abaixo o valor final de `A` e tente explicar o que aconteceu.

    !!! answer
        Ao fim você deve `A = [ 3, 2, 4, 5, 8, 12, 77 ]`


!!! exercise long id_bubble_simula1
    Simule a primeira iteração do loop `ENQUANTO` para `A = [  8, 7, 6, 5, 4, 3, 2, 1 ]`. Coloque abaixo o valor final de `A` e tente explicar o que aconteceu.

    !!! answer
        Ao fim você deve `A = [  7, 6, 5, 4, 3, 2, 1, 8 ]`


!!! exercise long id_bubble_simula2
    Simule a primeira iteração do loop `ENQUANTO` para `A = [  10, 20, 30, 40, 50, 60, 70, 80 ]`. Coloque abaixo o valor final de `A` e tente explicar o que aconteceu.

    !!! answer
        Ao fim você deve `A = [  10, 20, 30, 40, 50, 60, 70, 80 ]`


Agora vamos ver o algoritmo funcionando por inteiro.

!!! exercise long id_bubble_simula_tudo0
    Simule toda a execução do algoritmo para `A = [  3, 4, 2 , 5, 77, 8, 12 ]`. Coloque abaixo o valor final de `A` para cada vez que o loop `ENQUANTO` roda. 

    !!! answer
        1. `A = [ 3, 2, 4, 5, 8, 12, 77 ]`
        1. `A = [ 2, 3, 4, 5, 8, 12, 77 ]`
        1. `A = [ 2, 3, 4, 5, 8, 12, 77 ]`

        É necessária uma última passagem que checa se é possível trocar algum elemento. Por isso a última linha está duplicada. 




!!! exercise long id_bubble_simula_tudo1
    Simule toda a execução do algoritmo para `A = [  8, 7, 6, 5, 4, 3, 2, 1 ]`. Coloque abaixo o valor final de `A` para cada vez que o loop `ENQUANTO` roda. 
    !!! answer
        1. `A = [  7, 6, 5, 4, 3, 2, 1, 8 ]`
        1. `A = [  6, 5, 4, 3, 2, 1, 7, 8 ]`
        1. `A = [  5, 4, 3, 2, 1, 6, 7, 8 ]`
        1. `A = [  4, 3, 2, 1, 5, 6, 7, 8 ]`
        1. `A = [  3, 2, 1, 4, 5, 6, 7, 8 ]`
        1. `A = [  2, 1, 3, 4, 5, 6, 7, 8 ]`
        1. `A = [  1, 2, 3, 4, 5, 6, 7, 8 ]`
        1. `A = [  1, 2, 3, 4, 5, 6, 7, 8 ]`

        É necessária uma última passagem que checa se é possível trocar algum elemento. Por isso a última linha está duplicada. 
    

!!! exercise long id_bubble_simula_tudo2
    Simule toda a execução do algoritmo para `A = [  10, 20, 30, 40, 50, 60, 70, 80 ]`. Coloque abaixo o valor final de `A` para cada vez que o loop `ENQUANTO` roda. 

    !!! answer
        1. `A = [  10, 20, 30, 40, 50, 60, 70, 80 ]`

        Só roda uma vez, dado que já está ordenado.

Agora que simulamos uma vez, podemos ver um vídeo desse algoritmo funcionando para o array `[ 3 0 1 8 7 2 5 4 6 9 ]`

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Iv3vgjM8Pv4?si=gtTqR-MNNrGmJH-B" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


!!! exercise long id_bubble_explicacao
    Agora que você simulou o algoritmo para algumas entradas, consegue explicar **como** ele funciona e **por que** o array chega no fim ordenado? Escreva abaixo

    !!! answer
        Discutido em sala. Use a opção "Editar" para modificar suas anotações após a discussão. 

## Selection Sort

Vamos agora desenvolver um algoritmo a partir de uma ideia de alto nível:

1. Comece encontrando o menor elemento do array. Troque ele de posição com o elemento na posição `0`. 
2. Faça o mesmo para a posição `1`, mas procurando o mínimo agora a partir do elemento `1`. Troque esse elemento com o da posição `1`
3. Repita isso para todas as posições do array, sempre tomando cuidado para pegar o mínimo da porção à direita da posição atual.

Vamos agora simular essa ideia para entendê-la melhor. 

!!! exercise long id_selection_algo_caso1
    Simule a ideia acima para o array `A = [3, 5, 4, 2]`. Você deve colocar uma linha para cada iteração do algoritmo, ou seja, cada vez que é feita uma troca entre o elemento atual e o menor da porção que resta do array. Em cada linha escreva

    - os índices que são feitas a troca
    - o estado de `A` após a troca ser feita. 

    !!! answer
        A lista abaixo está ordenada pelo índice do elemento analisado

        0. O menor elemento de A é 2, então fazemos a troca entre o índice `0` e o índice `3`. `A = [2, 5, 4, 3]`
        1. O menor elemento de A (a partir do índice 1) é 3. É feita troca entre os índices `1` e `3`. `A = [2, 3, 4, 5]`
        2. O menor elemento de A (a partir do índice 2) é 4. É feita troca entre os índices `2` e `2`. `A = [2, 3, 4, 5]`

        Quando chegamos no índice `3` a porção restante de `A` só tem um elemento, então terminamos aqui. 



!!! exercise long id_selection_algo_caso2
    Simule a ideia acima para o array `A = [5, 6, 8, 11]`. Você deve colocar uma linha para cada iteração do algoritmo, ou seja, cada vez que é feita uma troca entre o elemento atual e o menor da porção que resta do array. Em cada linha escreva

    - os índices que são feitas a troca
    - o estado de `A` após a troca ser feita. 

    !!! answer
        A lista abaixo está ordenada pelo índice do elemento analisado

        0. O menor elemento de A é 5, então fazemos a troca entre o índice `0` e o índice `0`. `A = [5, 6, 8, 11]`
        1. O menor elemento de A (a partir do índice 1) é 6. É feita troca entre os índices `1` e `1`. `A = [5, 6, 8, 11]`
        2. O menor elemento de A (a partir do índice 2) é 8. É feita troca entre os índices `2` e `2`. `A = [5, 6, 8, 11]`

        Quando chegamos no índice `3` a porção restante de `A` só tem um elemento, então terminamos aqui. 



!!! exercise long id_selection_algo_caso3
    Simule a ideia acima para o array `A = [3, 7, 12, 0, -1, 4, 8]`. Você deve colocar uma linha para cada iteração do algoritmo, ou seja, cada vez que é feita uma troca entre o elemento atual e o menor da porção que resta do array. Em cada linha escreva

    - os índices que são feitas a troca
    - o estado de `A` após a troca ser feita. 

    !!! answer
        A lista abaixo está ordenada pelo índice do elemento analisado

        0. O menor elemento de A (a partir do índice 0) é -1. É feita troca entre os índices `0` e `4`. `A = [-1, 7, 12, 0, 3, 4, 8]`
        1. O menor elemento de A (a partir do índice 1) é 0. É feita troca entre os índices `1` e `3`. `A = [-1, 0, 12, 7, 3, 4, 8]`
        2. O menor elemento de A (a partir do índice 2) é 3. É feita troca entre os índices `2` e `4`. `A = [-1, 0, 3, 7, 12, 4, 8]`
        3. O menor elemento de A (a partir do índice 3) é 4. É feita troca entre os índices `3` e `5`. `A = [-1, 0, 3, 4, 12, 7, 8]`
        4. O menor elemento de A (a partir do índice 4) é 7. É feita troca entre os índices `4` e `5`. `A = [-1, 0, 3, 4, 7, 12, 8]`
        5. O menor elemento de A (a partir do índice 5) é 8. É feita troca entre os índices `5` e `6`. `A = [-1, 0, 3, 4, 7, 8, 12]`

        Quando chegamos no índice `6` a porção restante de `A` só tem um elemento, então terminamos aqui. 

Novamente, veja um vídeo da simulação para o array `[ 3 0 1 8 7 2 5 4 9 6 ]`

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/0-W8OEwLebQ?si=PN9Ro-0npBBedByK" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


Agora que já simulamos o algoritmo algumas vezes, vamos escrever o pseudo código dele.

!!! exercise long id_selection_algo_write
    Escreva abaixo o pseudo-código de `SELECTION_SORT(A)`. 

    !!! answer
        Discutido em sala. Use a opção "Editar" para modificar suas anotações após a discussão. 

## Considerações sobre eficiência 

Os algoritmos acima são bem diferentes entre si. 

!!! exercise long id_bubble_complexidade
    Responda às seguintes perguntas levando em conta o algoritmo `BUBBLE_SORT` da primeira seção. Para cada uma você deve escrever a resposta em termos do tamanho do `N` do array `A`.

    1. no pior caso, quantas vezes roda o loop `ENQUANTO`?
    2. e o loop interno, roda quantas vezes?

    Junte essas duas informações e diga, no pior caso, quantas operações são feitas pelo algoritmo. 
    
    **Dica**: tente contar quantas vezes a comparação `A[I] > A[I+1]` é executada. 

    !!! answer 
        Discutido em sala. Use a opção "Editar" para modificar suas anotações após a discussão. 


!!! exercise long id_selection_complexidade
    Responda às seguintes perguntas levando em conta o algoritmo `SELECTION_SORT` da segunda seção. Para cada uma você deve escrever a resposta em termos do tamanho do `N` do array `A`.

    1. quantas vezes é executado o processo de encontrar o menor valor do array?
    2. qual o custo, no pior caso, de encontrar o menor valor de uma porção do array?

    Junte essas duas informações e diga, no pior caso, quantas operações são feitas pelo algoritmo. 

    !!! answer 
        Discutido em sala. Use a opção "Editar" para modificar suas anotações após a discussão. 

!!! exercise long
    Mostre (usando a aula [01-02 Desempenho](/modulos/01-Busca-Array/desempenho)) que ambos algoritmos crescem de maneira equivalente.

    !!! answer
        Discutir no atendimento esse aqui ;)
