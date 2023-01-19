# Aula 01 - arrays e Listas

O tipo `Array` que discutimos na apresentação inicial representa a maneira mais básica de se armazenar dados em linguagens de programação. Ele é, basicamente, uma região de memória em que colocamos um objeto após o outro, em sequência. Como o computador compartilha a memória com diversos programas, precisamos dizer com antecedência o quanto de memória usaremos. Por isso, o `Array` tem tamanho fixo.

Gerenciar esse tamanho fixo do array dá trabalho e várias linguagens oferecem implementações do tipo `List`, que permite inserir e remover elementos. Veja alguns exemplos disso abaixo.

- `list` de Python
- `ArrayList` de Java
- `std::vector` de C++

!!! tip
    Uma descrição completa do tipo `List` pode ser vista [aqui](list.md)

Vamos agora iniciar a implementação de uma *Estrutura de Dados* que implemente o tipo `List` usando o tipo `Array`. Nosso objetivo aqui será

1. compreender a implementação das operações do tipo `List`
2. utilizar um Tipo de Dados mais simples (`Array`) para implementar outro tipo mais complexo (`Lista`)

!!! tip
    * Um *Tipo de Dados* somente define quais operações existem e quais são suas entradas e saídas.
    * Uma *Estrutura de Dados (ED)* descreve também algoritimos para cada uma das operações suportadas.

    Dessa maneira, podemos pensar na *ED* como uma descrição detalhada (em termos de algoritmos) de como uma *ADT* poderia ser implementada.


!!! important
    Existem várias *EDs* diferentes que podem implementar a mesma *ADT* e uma mesma *ED* pode implementar várias *ADTs* diferentes.

## Vetor dinâmico

O vetor dinâmico é uma *ED* que permite implementar as operações do tipo `List` usando um `Array`. Na discussão no início da aula o professor apresentou a ideia de *capacidade* e *tamanho* de uma lista. Vamos revisar esses conceitos nas próximas perguntas.

!!! exercise long id_adt_lista_capacidade_tamanho_relembrar
    Resuma o que você lembra no campo abaixo.

    !!! answer
        Nossa *ED* vetor dinâmico tem três atributos:

        - `Array` *A* para guardar os dados
        - *capacidade*: número máximo de elementos que podem ser guardados *A*. Sempre igual a `TAMANHO(A)`
        - *tamanho*: número de elementos efetivamente guardados em *A*.


!!! exercise choice id_adt_lista_capacidade_tamanho_relacao
    Em relação a capacidade e tamanho, é correto afirmar que sempre `capacidade <= tamanho`?

    - [ ] SIM
    - [X] NÃO

    !!! answer
        Dado que a capacidade é o número **máximo** de elementos que podem ser guardados no `Array`, a afirmação é falsa. O contrário é que é verdade: `tamanho <= capacidade`.

        Pense no *tamanho* como o número de elementos não vazios do `Array`, enquanto a capacidade é `TAMANHO(Array)`.

!!! exercise choice id_adt_lista_capacidade_tamanho_insercao
    Em um dado momento nosso vetor dinâmico tem `capacidade=8` e `tamanho=5`. Após a inserção de um novo elemento, quais serão os valores dessas duas quantidades?

    - [X] capacidade=8, tamanho=6
    - [ ] capacidade=9, tamanho=5
    - [ ] capacidade=8, tamanho=5
    - [ ] capacidade=9, tamanho=6

    !!! answer
        Como ainda tem espaço em nosso `Array`, somente o tamanho aumenta.


!!! exercise choice id_adt_lista_capacidade_tamanho_remocao
    Em um dado momento nosso vetor dinâmico tem `capacidade=8` e `tamanho=7`. Após a remoção de um elemento, quais serão os valores dessas duas quantidades?

    - [X] capacidade=8, tamanho=6
    - [ ] capacidade=7, tamanho=6
    - [ ] capacidade=8, tamanho=7
    - [ ] capacidade=7, tamanho=7

    !!! answer
        Neste caso, como o `Array`que usamos em nosso vetor está quase cheio (6/8 posições ocupadas) a capacidade se mantém. Assim como na inserção, a remoção sempre mexe no tamanho do vetor.

!!! progress
    Continuar

As operações mais interessantes do vetor são `INSERE` e `REMOVE`. Vamos trabalhar nelas agora.

### Inserção

exercícios para simular

pede algoritmo para jogar todos para o lado?

apresenta o completo na respsota do exercício

### Remoção



### Redimensionamento

pede par simular e pede para modificar o algoritmo dado anteriormente



