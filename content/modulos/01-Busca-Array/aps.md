# APS

Teremos dois tipos de tarefas esta semana:

- **implementações diretas**: são exercícios que trabalham diretamente com os algoritmos vistos nas expositivas e trabalhados nos handouts
- **problemas**: exercícios estilo maratona de programação que usam as ideias trabalhadas no módulo. É preciso "encontrar" como o tópico atual é usado e geralmente é necessário modificar um pouco o algoritmo visto em aula. 

| Nota | Nível                |
| ---- | -------------------- |
| 70%  | Implementação direta |
| 30%  | Problemas            |

## Implementação direta

No nível básico teremos duas tarefas que modificam o arquivo `br.edu.insper.tecprog.BinarySearchIter.java`. Elas contém as ideias básicas já exploradas neste módulo. 

!!! exercise 
    Saber se um array está ordenado é importante para podermos aplicar a busca binária. Complete a função `#!java boolean ordenado(InsperList l)` para checar se a `l` está ordenado. 
    
!!! exercise 
    Vamos agora implementar a busca binária (iterativa). Complete a função `#! int buscaBinaria(int value)` para retornar o índice do elemento `value` ou `-1` se ele não for encontrado. Se houver repetição, retorne o índice do elemento mais à esquerda. 
    
!!! exercise 
    Na [leitura sobre recursão](busca-binaria-geral.md) explicamos como escrever algoritmos que usam a si mesmos. Escreva uma versão recursiva da busca binária. Você deve colocá-la no arquivo `br.edu.insper.tecprog.BinarySearchRec.java`.

## Problemas

Os seguintes exercícios foram baseados em problemas de maratona de programação 

!!! exercise
    **Enunciado**: Lumberjack Mirko needs to chop down `M` metres of wood. It is an easy job for him since he has a nifty new woodcutting machine that can take down forests like wildfire. However, Mirko is only allowed to cut a single row of trees.

    Mirko's machine works as follows: Mirko sets a height parameter `H` (in metres), and the machine raises a giant sawblade to that height and cuts off all tree parts higher than `H` (of course, trees not higher than H meters remain intact). Mirko then takes the parts that were cut off. For example, if the tree row contains trees with heights of 20, 15, 10, and 17 metres, and Mirko raises his sawblade to 15 metres, the remaining tree heights after cutting will be 15, 15, 10, and 15 metres, respectively, while Mirko will take 5 metres off the first tree and 2 metres off the fourth tree (7 metres of wood in total).

    Mirko is ecologically minded, so he doesn't want to cut off more wood than necessary. That's why he wants to set his sawblade as high as possible. Help Mirko find the maximum integer height of the sawblade that still allows him to cut off at least `M` metres of wood.
    
    **Exemplos**:

    ```
    # Entrada
    M=7, trees=[20 15 10 17]
    # Saída
    15

    # Entrada
    M=20, trees=[4 42 40 26 46]
    # Saída
    36
    ```

    -----

    Seu trabalho será criar uma função `#!java long sawbladeHeight(int[] trees, int M)` que recebe a altura das árvores e o número `M` de metros de madeira necessário e devolve a menor altura que permite cortar ao menos `M` metros de madeira. Você pode supor que `trees` está ordenado e que a soma de todas as alturas é sempre maior que `M`. Edite o arquivo `br.edu.insper.tecprog.Eko.java`.

    Baseado em [EKO](https://www.spoj.com/problems/EKO/en/)

