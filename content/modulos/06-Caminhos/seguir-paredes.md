# Algoritmo de Seguir Paredes


Nesse handout iremos formalizar duas grandes ideias:

- uma ADT para representar o labirinto
- como representar o algoritmo senso comum de sair do labirinto seguindo as paredes

## A ADT Labirinto

Um primeiro passo para definirmos nossos algoritmos é definir como o labirinto será representado para nosso código. Vamos considerar um labirinto com as seguintes operações nesta atividade.

- `NOVO_LABIRINTO(TEXT)` - recebe um texto no formato de labirinto definido abaixo e devolve o labirinto criado.
- `LIVRE(L, I, J)` - devolve `VERDADEIRO` se a posição na linha `I` coluna `J` não é parede
- `SAIDA(L, I, J)` - devolve `VERDADEIRO` se a posição na linha `I` coluna `J` é uma saída do labirinto (ou seja, se está na borda do labirinto e se está livre)
- `LARGURA(L), ALTURA(L)` - devolve a largura/altura do labirinto

Usaremos o seguinte formato de texto para a criação do labirinto

```
#####
#...#
###.#
```

- cada linha contém somente caracteres `'.'` (livre) ou `'#'` (parede)
- todas as linhas contém o mesmo número de caracteres

Iremos representar o labirinto como um array `boolean casas[][]` em que a posição `casas[i][j]` contém `true` se a casa é parede e `false` caso contrário. Veja o item da ADT na [APS](aps.md) deste módulo para uma descrição mais completa da implementação.

## Algoritmo de Seguir Paredes

Ao longo das próximas aulas iremos criar várias versões do algoritmo `ENCONTRA_SAIDA(L, I, J, CAMINHO)` onde

- `L` é um labirinto
- `I, J` é a posição inicial
- `CAMINHO` é um array que será preenchido com as posições do labirinto até a saída

A primeira ideia que estudaremos para a criação de um algoritmo é simples:

### para sair do labirinto basta colocar a mão direita na parede mais próxima e seguir sempre com essa mão na parede. Eventualmente chegamos na saída.

!!! exercise long
    Como você explicaria que esta ideia chega na saída de qualquer labirinto?

    !!! answer
        Essa ideia faz o contorno das paredes do labirinto, passando por todas as paredes tocáveis. Eventualmente chegamos na parede da casa da saída, se houver um caminho. 

!!! exercise long
    Acima argumentamos que é possível encontrar a saída de qualquer labirinto. É possível chegar em qualquer parte de um labirinto usando esse algoritmo?

    !!! answer
        Se o destino for uma casa isolada fora de uma parede não é possível chegar. Veja abaixo um exemplo, onde `x` é o destino

        ```
        #########
        #.......#
        #....x..#
        #.......#
        #########

        ```

Para implementar esse algoritmo precisamos definir algumas coisas:

- estado: quais variáveis representam o andamento do algoritmo. 
- critério de parada: quando decidimos que chegamos no fim? 

Uma boa maneira de entender esses pontos é simular a ideia em alguns cenários simples. Vamos lá


!!! exercise choice 
    No labirinto abaixo, qual será a próxima casa a ser seguida pela ideia acima? A posição anterior está marcada por `x`, a posição atual por `o` e queremos determinar a nova posição. 

    ```
    ######
    #.....
    #...##
    #..ox#
    #....#
    ######
    ```

    - [X] cima
    - [ ] baixo
    - [ ] direita
    - [ ] esquerda


!!! exercise choice 
    No labirinto abaixo, qual será a próxima casa a ser seguida pela ideia acima? A posição anterior está marcada por `x`, a posição atual por `o` e queremos determinar a nova posição. 

    ```
    ##########
    ....xo....
    ##########
    ```

    - [ ] cima
    - [ ] baixo
    - [x] direita
    - [ ] esquerda


!!! exercise choice 
    No labirinto abaixo, qual será a próxima casa a ser seguida pela ideia acima? A posição anterior está marcada por `x`, a posição atual por `o` e queremos determinar a nova posição. 

    ```
    ##########
    ...ox.....
    ##########
    ```

    - [ ] cima
    - [ ] baixo
    - [ ] direita
    - [x] esquerda

!!! progress
    Continuar

Agora já conseguimos observar algumas coisas:

1. a próxima posição parece depender da posição atual e da anterior
2. somente saber a posição atual não é suficiente para saber a próxima posição

Vamos agora continuar nossa exploração dessa ideia:

!!! exercise choice 
    No labirinto abaixo, em qual parede a mão direita está posicionada? A posição anterior está marcada por `x`, a posição atual por `o` e queremos determinar a nova posição. 

    ```
    ##########
    ...ox.....
    ##########
    ```

    - [x] parede de cima
    - [ ] parede de baixo

!!! exercise choice 
    No labirinto abaixo, em qual parede a mão direita está posicionada? A posição anterior está marcada por `x`, a posição atual por `o` e queremos determinar a nova posição. 

    ```
    ##########
    ....xo....
    ##########
    ```

    - [ ] parede de cima
    - [x] parede de baixo

Vamos agora para um caso difícil:

!!! exercise choice
    No labirinto abaixo, suponha que a mão está posicionada na parede da direita. Qual será o próximo passo do algoritmo?

    ```
    ##########
    #...#o#...
    #...#.#...
    #..##.#..#
    #..#..#..#
    #..#.#...#
    #..#.#...#
    #........#
    #........#
    ##########
    ```

    - [ ] Anda para baixo, mantém mão na mesma parede
    - [x] fica no mesmo lugar, mas muda mão para parede de cima
    - [ ] fica no mesmo lugar, mas muda mão para parede da esquerda

    !!! answer
        Nossa ideia diz que a mão direita deve passar por todas paredes e que sempre seguimos em frente. Logo, a opção *"Anda para baixo, mantém mão na mesma parede"* não pode ocorrer: foi invertido o sentido sem trocar a mão de parede. 

        A opção *"fica no mesmo lugar, mas muda mão para parede da esquerda"* pulou uma parede e mudou direto para a da esquerda.

        Gostaríamos de seguir reto, mas não é possível pois há uma parede na frente. Logo, devemos mudar a mão de parede, virando para a esquerda e colocando a mão na parede de cima. 

!!! progress 
    Continuar

!!! exercise long
    Vamos agora fechar a ideia de estado do algoritmo. Quais são as variáveis que representam o progresso atual de nosso algoritmo?

    !!! answer
        As posições `I,J` atuais mais a parede usada como referência para a mão direita. Podemos representar essa parede como uma direção dentre `CIMA, BAIXO, ESQUERDA, DIREITA`. 

!!! exercise long
    Agora temos que identificar o critério de parada: quando dizemos que o algoritmo termina? Coloque abaixo uma condição usando a ADT do labirinto.

    !!! answer
        Faça o exercício abaixo e revise sua resposta usando o botão "Editar"

!!! exercise long
    Qual seria uma condição de parada que resolve o seguinte caso? Considere que a posição inicial é marcada por `o` e que a parede de referência é a de baixo. 

    ```
    ##########
    #.#.#.#..#
    #...#.#..#
    #..##.#.##
    #.##..#..#
    #..#.#...#
    #..#.#.###
    ##.......#
    #...o....#
    ##########
    ```

    !!! answer
        Nos casos em que não há uma saída alcançável, precisamos verificar se voltamos ao ponto inicial com a mão na mesma parede. Ou seja, irá acontecer um loop infinito, pois o algoritmo progride sempre igual dado o mesmo estado inicial. 


!!! progress
    Continuar

Com essas simulações já é possível criar um algoritmo que implemente essa ideia. Faremos a seguinte sequência iterativa:

1. design de uma versão inicial do algoritmo
2. simulação de uma iteração com um exemplo de cenário
3. revisão do algoritmo, caso ocorram erros

!!! exercise long
    Crie um algoritmo `ENCONTRA_SAIDA_SEGUE_PAREDE(L, I, J, CAMINHO)` usando a ideia que exploramos nas simulações deste roteiro. Se existe caminho o algoritmo deve devolver `VERDADEIRO`.

    !!! answer 
        Esse é parte da APS ;)

!!! exercise long
    Simule seu algoritmo com o seguinte labirinto. Considere que `o` representa a posição inicial.

    ```
    ##########
    ....o.....
    ..........
    ##########
    ```

    !!! answer
        O caminho será o abaixo. Considere que os números representam a ordem do caminho. O algoritmo devolve `VERDADEIRO`

        ```
        ##########
        4321o.....
        ..........
        ##########
        ```

!!! exercise long
    Simule seu algoritmo com o seguinte labirinto. Considere que `o` representa a posição inicial.

    ```
    ##########
    ...#......
    .....o#...
    ##########
    ```

    !!! answer
        O caminho será o abaixo. Considere que os números representam a ordem do caminho. O algoritmo devolve `VERDADEIRO`

        ```
        ##########
        ...#.123..
        .....o#456
        ##########
        ```


!!! exercise long
    Simule seu algoritmo com o seguinte labirinto. Considere que `o` representa a posição inicial.

    ```
    ##########
    ...#.#....
    ....o.#...
    ##########
    ```

    !!! answer
        O caminho será o abaixo. Considere que os números representam a ordem do caminho. O algoritmo devolve `VERDADEIRO`. Como passamos duas vezes no ponto inicial colocamos o número 2 abaixo de `o` exemplo abaixo.

        ```
        ##########
        ...#.#....
        6543o1#...
            2
        ##########
        ```



Agora é hora de partir para implementação. Veja o item deste algoritmo na [APS](aps.md) deste módulo para uma descrição mais completa da implementação.
