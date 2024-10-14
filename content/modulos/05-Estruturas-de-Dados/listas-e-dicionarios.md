# Aula 03 - Dicionários

Quando começamos a chegar no fim de DevLife usamos cada vez mais Dicionários em nosso código. Os usamos para representar coleções de pares *chave->valor* em que para cada *chave* existe exatamente um valor. Como era possível compor dicionários dentro de dicionários dentro de dicionários (e por aí vai) conseguíamos usá-los para representar hierarquias complexas. O tipo `Map` representa de maneira abstrata esse tipo de estrutura de dados.

## O tipo `Map`


Um `Map` é uma mapeamento **chave $\rightarrow$ valor** em que cada chave pode estar a associada a um único valor. Note que um valor pode estar associado a várias chaves, mas cada chave só possui um valor. As seguintes operações são suportadas:

- `NOVO_MAP()` - cria um novo `Map`
- `SET(M, K, V)` - associa o valor `V` à chave `K`. Se a chave `K` já existir substitui o valor.
- `GET(M, K)` - devolve o valor associado a chave `K`. Se não houver retorna `VAZIO`
- `REMOVE(M, K)` - remove o par com chave `K`. Se não houver não faz nada.
- `TAMANHO(M)` - devolve o número de chaves que possuem um valor associado


Neste roteiro desenvolveremos juntos os algoritmos necessários para implementar uma **versão simplificada** do `Map` usando duas `List`.

## Construindo em cima de outras ADT

Uma das grandes vantagens de definir (e usar) *ADTs* é que podemos construir algoritimos em mais alto nível. Podemos dizer, simplesmente, que vamos usar uma variável do tipo `Array` e/ou `List` e apontar para quais operações são suportadas. Isso nos ajuda a manter os algoritmos compactos e a dar enfoque nas ideias mais importantes para o problema que queremos resolver.

!!! tip
    *ADTs* são conhecimento básico em Computação. Não precisamos repetir, toda vez, o código para implementar o tipo `List`. Basta dizer que está usando esse tipo.

A implementação mais simples `Map` é usando duas listas:

- `KEYS(M)` é um `List` contendo uma lista de todas as chaves do `Map` `M`
- `VALUES(M)` é um `List` contendo uma lista de todas os valores do `Map` `M`

!!! exercise long id_map_ideia_indices
    Considere os seguintes pares chave-valor:

    - "pastel de queijo" = 2
    - "pastel de carne" = 1
    - "pastel de soja" = 5

    Como você usaria as duas listas acima (`KEYS(M)` e `VALUES(M)`) para armazená-los? Escreva o conteúdo das listas na forma

    ```
    - KEYS(M) = [conteúdo aqui ]
    - VALUES(M) = [ conteúdo aqui ]
    ```

    !!! answer
        Uma maneira fácil de fazer isto é

        - `KEYS(M)` = `[ "pastel de queijo", "pastel de carne", "pastel de soja" ]`
        - `VALUES(M)` = `[ 2, 1, 5 ]`

        A ordem aqui não importa, desde que sejamos consistentes e mantenhamos a equivalência de índices para que as chaves e valores continuem "casadas".

!!! exercise long
    Vamos continuar com o exemplo acima.

    1. Map 1:
        - `KEYS(M)` = `[ "pastel de queijo", "pastel de carne", "pastel de soja" ]`
        - `VALUES(M)` = `[ 2, 1, 5 ]`
    2. Map 2:
        - `KEYS(M)` = `[ "pastel de queijo", "pastel de soja", "pastel de carne" ]`
        - `VALUES(M)` = `[ 2, 5, 1 ]`

    Os dois `Map` acima são iguais? Ou seja, eles representam as mesmas associações chave-valor? Justifique.

    !!! answer
        Eles são iguais! O conjunto de chaves de ambos é igual e para toda chave o valor devolvido é o mesmo. Para um `Map` a ordem não importa, somente a presença da chave e o valor associado a ela.


!!! exercise long id_resumo_ideia_map
    Dada as respostas dos exercícios anteriores, como você resumiria a ideia de usar duas listas para implementar o `Map`?

    !!! answer
        Próxima seção ;)

!!! progress
    Continuar

Vamos usar as seguintes convenções a partir de agora

- `M_K = KEYS(M)`
- `M_V = VALUES(M)`

A ideia central é **Dada uma associação chave-valor `(K, V)`, se guardamos a chave `K` no índice `i` de `M_K` guardaremos o valor `V` no mesmo índice `i` em `M_V`**. 

De maneira mais formal, seja $M$ um `Map`, $N=$`TAMANHO(M_K)` e $(K, V)$ uma associação chave valor presente em `M`, então


$$
(K, V) \in M \Leftrightarrow \exists 0 \leq i < N \;\;\text{ tal que }\;\; M_K[i] = K,\; M_V[i] = V
$$

Vamos agora desenvolver alguns algoritmos simples para nos familiarizarmos com essa dupla de listas.

!!! exercise long id_map_indexOf
    Um algoritmo muito útil (e frequentemente disponível) é o `indexOf`, que devolve o índice da primeira ocorrência de um valor em uma lista.

    * **Entrada**
        - `List` `L`
        - valor `VAL`
    * **Saída**:
        - se a lista tem o valor, retorna o índice da primeira ocorrência
        - -1 caso contrário

    Escreva o algoritmo `indexOf(L, VAL)` em pseudo-código

    !!! answer
        ```
        indexOf(L, VAL)

        PARA i=0 até TAMANHO(L) FAÇA
            SE L[i] = VAL FAÇA
                RETORNE i
            FIM
        FIM

        RETORNE -1
        ```

!!! exercise long id_get_usando_indexOf
    Vamos agora trabalhar com as duas listas em conjunto. Use o algoritmo `indexOf` feito acima para implementar a operação `GET` do `Map`:

    - `GET(M, K)` - devolve o valor associado a chave `K`. Se não houver retorna `VAZIO`

    !!! answer
        Lousa

!!! exercise long id_set_map
    A operação `SET(M, K, V)`

    - faz uma nova associação chave-valor se a chave já existir, esquecendo a antiga
    - adiciona um novo par chave-valor caso contrário

    Escreve um algoritmo que implemente essa operação. Você pode usar todos os algoritmos que já desenvolveu até aqui, incluindo as operações do tipo `List`.

    !!! answer
        Lousa

As operações `REMOVE` e `TAMANHO` são variações dos que já foram construídos nessa aula. Para registrar, escreva-os abaixo.

!!! exercise long id_map_remove
    Escreva abaixo o algoritmo para `REMOVE(M, K)`.


!!! exercise long id_map_tamanho
    Escreva abaixo o algoritmo para `TAMANHO(M)`.

Agora acesse o PrairieLearn e implemente esse algoritmos no exercício prático. 
