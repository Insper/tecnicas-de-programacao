# Aula 02 - Dicionários

Quando começamos a chegar no fim de DevLife usamos cada vez mais Dicionários em nosso código. Os usamos para representar coleções de pares *chave->valor* em que para cada *chave* existe exatamente um valor. Como era possível compor dicionários dentro de dicionários dentro de dicionários (e por aí vai) conseguíamos usá-los para representar hierarquias complexas. O tipo `Map` representa de maneira abstrata esse tipo de estrutura de dados.

!!! warning
    Vale a pena revisar as [operações de dados](map.md) de um `Map` antes de prosseguir.

Neste roteiro desenvolveremos juntos os algoritmos necessários para implementar uma **versão simplificada** do `Map` usando duas `List`.

## Construindo em cima de outras ADT

Uma das grandes vantagens de definir (e usar) *ADT*s é que podemos construir algoritimos em mais alto nível. Podemos dizer, simplesmente, que vamos usar uma variável do tipo `Array` e/ou `List` e apontar para quais operações são suportadas. Isso nos ajuda a manter os algoritmos compactos e a dar enfoque nas ideias mais importantes para o problema que queremos resolver.

!!! tip
    *ADT*s são conhecimento básico em Computação. Não precisamos repetir, toda vez, o código para implementar o tipo `List`. Basta dizer que está usando esse tipo.

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
    - `KEYS(M)` = `[ conteúdo aqui ]`
    - `VALUES(M) = `[ conteúdo aqui ]`
    ```

    !!! answer
        Uma maneira fácil de fazer isto é

        - `KEYS(M)` = `[ "pastel de queijo", "pastel de carne", "pastel de soja" ]`
        - `VALUES(M) = `[ 2, 1, 5 ]`

!!! exercise long
    Vamos continuar com o exemplo acima.

    1. Map 1:
        - `KEYS(M)` = `[ "pastel de queijo", "pastel de carne", "pastel de soja" ]`
        - `VALUES(M) = `[ 2, 1, 5 ]`
    2. Map 2:
        - `KEYS(M)` = `[ "pastel de queijo", "pastel de soja", "pastel de carne" ]`
        - `VALUES(M) = `[ 2, 5, 1 ]`

    Os dois `Map` acima são iguais? Ou seja, eles representam as mesmas associações chave-valor? Justifique.

    !!! answer
        Eles são iguais! O conjunto de chaves de ambos é igual e para toda chave o valor devolvido é o mesmo.


!!! exercise long id_resumo_ideia_map
    Dada as respostas dos exercícios anteriores, como você resumiria a ideia de usar duas listas para implementar o `Map`?

    !!! answer
        Próxima seção ;)

!!! progress
    Continuar

Vamos usar as seguintes convenções a partir de agora

- `M_K = KEYS(M)`
- `M_V = VALUES(M)`

A ideia central é **Dada uma associação chave-valor `(K, V)`, se guardamos a chave `K` no índice `i` de `M_K` guardaremos o valor `V` no mesmo índice `i` em `M_V`**. Podemos colocar isso de maneira mais formal: **existe um índice `0 <= i < TAMANHO(M_K)` tal que `M_K[i] = K` e `M_V[i] = V`**.

Vamos agora desenvolver alguns algoritmos simples para nos familiarizarmos com essa dupla de listas.

!!! exercise long id_map_indexOf
    Um algoritmo muito útil (e frequentemente disponível) é o `indexOf`, que devolve o índice da primeira ocorrência de um valor em uma lista.

    * **Entrada**
        - `List` `L`
        - valor `V`
    * **Saída**:
        - se a lista tem o valor, retorna o índice da primeira ocorrência
        - -1 caso contrário

    Escreva o algoritmo `indexOf(L, V)` em pseudo-código

    !!! answer
        ```
        indexOf(L, V)

        PARA i=0 até TAMANHO(L) FAÇA
            SE L[i] = V FAÇA
                RETORNE i
            FIM
        FIM

        RETORNE -1
        ```

!!! exercise long id_get_usando_indexOf
    Vamos agora trabalhar com as duas listas em conjunto. Use o algoritmo `indexOf` feito acima para implementar a operação `GET` do `Map`:

    - `GET(M, K)` - devolve o valor associado a chave `K`. Se não houver retorna `VAZIO`

    !!! answer
        TODO: colocar resposta aqui

!!! exercise long id_set_map
    A operação `SET(M, K, V)`

    - faz uma nova associação chave-valor se a chave já existir, esquecendo a antiga
    - adiciona um novo par chave-valor caso contrário

    Escreve um algoritmo que implemente essa operação. Você pode usar todos os algoritmos que já desenvolveu até aqui, incluindo as operações do tipo `List`.

    !!! answer
        Esse vai na lousa ;)

As operações `REMOVE` e `TAMANHO` são variações dos que já foram construídos nessa aula. Para registrar, escreva-os abaixo.

!!! exercise long id_map_remove
    Escreva abaixo o algoritmo para `REMOVE(M, K)`.


!!! exercise long id_map_tamanho
    Escreva abaixo o algoritmo para `TAMANHO(M)`.

Agora o trabalho será transformar esses algoritmos em implementações `Java` na [APS desse módulo](aps.md)
