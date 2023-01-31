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
    * Um *Tipo de Dados* somente define quais operações existem e quais são suas entradas e saídas. Ou seja, aqui definimos **o quê** deve ser feito. 
    * Uma *Estrutura de Dados (ED)* descreve também algoritimos para cada uma das operações suportadas. Ou seja, aqui temos também **como** cada operação deve ser realizada.

    Dessa maneira, podemos pensar na *ED* como uma descrição detalhada (em termos de algoritmos) de como uma *ADT* poderia ser implementada.


!!! important
    Existem várias *EDs* diferentes que podem implementar a mesma *ADT* e uma mesma *ED* pode implementar várias *ADTs* diferentes.

## Vetor dinâmico

O vetor dinâmico é uma *ED* que permite implementar as operações do tipo `List` usando um `Array`. Vamos iniciar relembrando os conceitos que acabamos de discutir.

!!! important
    Como o vetor dinâmico implementa toda a ADT `List`, nesse guia iremos usar a letra `L` quando nos referirmos a um vetor dinâmico.

!!! exercise long id_adt_lista_capacidade_tamanho_relembrar
    Quais são os atributos que o vetor dinâmico possui? Para que servem?

    !!! answer
        Nossa *ED* vetor dinâmico tem três atributos.

        - `Array` *A* para guardar os dados
        - *capacidade*: número máximo de elementos que podem ser guardados *A*. Sempre igual a `TAMANHO(A)`
        - *tamanho*: número de elementos efetivamente guardados em *A*. Sempre igual a `TAMANHO(L)`.


As operações mais interessantes do vetor são `INSERE` e `REMOVE`. Vamos trabalhar nelas agora.

!!! important
    Dado que usaremos um `Array` para implementar `List`, teremos sempre um tamanho máximo fixo para nossos dados. Nessas próximas seções vamos sempre supor que existem espaços vazios disponíveis para inserir mais dados.

### Inserção

Vamos primeiro rever a descrição de ˋINSEREˋ:

!!! note "Definição"
    insere o valor `V` na lista `L` na posição `i`. Os elementos a partir da posição `i` são "empurrados" para a direita. Essa operação incrementa o tamanho da lista.

O primeiro passo do algoritmo é "empurrar" todos elementos para a direita. Vamos inicialmente supor que a lista `L` tem espaço para colocar o elemento `V` na posição `i`. Ou seja, é verdade que `TAMANHO(L) + 1 < capacidade = TAMANHO(A)`.

!!! exercise long id_algoritmo_desloca_array
    Vamos rascunhar uma primeira versão desse algoritmo. Assim como nos nossos outros exercícios, deixaremos bem definido o nome da função e seus argumentos: `DESLOCA_DIREITA(L, N, i)`. 

    * Entrada: 
        * Lista `L`
        * ˋN=TAMANHO(L)ˋ
        * `i` é a posição que será liberada
    * Saída:
        * `L` é modificado diretamente. a função não retorna nada. O valor `L[i]` não importa, então manteremos ele igual.
        
    !!! answer
        Teste seu algoritmo com as seguintes entradas. Estamos supondo que `L` já tem um elemento vazio disponível no fim. 
        
        - 
        ```
        Entrada: L = [], i=0
        Saída: L = []
        ```
        - 
        ```
        Entrada: L = [1], i=0
        Saída: L = [1, 1]
        ```
        - 
        ```
        Entrada: L = [1], i=1
        Saída: L = [1]
        ```
        - 
        ```
        Entrada: L = [1, 2, 3], i=0
        Saída: L = [1, 1, 2, 3]
        ```
        - 
        ```
        Entrada: L = [1, 2, 3], i=1
        Saída: L = [1, 2, 2, 3]
        ```

!!! progress
    Continuar


O algoritmo é bem simples: começamos no elemento `N` e descemos até a posição `i+1` copiando o valor do índice anterior. Note que atribuímos a `L[N]`, o que significa que `TAMANHO(L)=N+1`.

```
DESLOCA_DIREITA(L, N, i)

PARA j=N ATÉ i+1 FAÇA
    L[j] = L[j-1]
FIM
```
        
Com essa rotina podemos implementar facilmente a inserção.

!!! exercise long id_lista_insercao_algo
    Escreva o algoritmo de inserção abaixo. Você deve usar a função `DESLOCA_DIREITA` criada acima. Não vamos mexer na `capacidade` de `A`, somente no `tamanho` de `L`.
    
    !!! answer
    
        ```
        INSERE(L, V, i)
        
        Incrementa TAMANHO(L)
        N = TAMANHO(L)
        
        DESLOCA_DIREITA(L, N, i)
        L[i] = V
        ```

Note que a etapa de tradução do algoritmo acima para Java não é exatamente trivial e depende de um monte de outras definições. Trabalharemos isso na [APS deste módulo](aps.md)

### Remoção

O algoritmo de remoção é muito parecido com a inserção, mas agora faz o deslocamento à esquerda. Note que novamente não vamos mexer na `capacidade` de `A`, somente no `tamanho` de `L`.

!!! exercise long id_algo_desloca_esquera
    Escreva o algoritmo `DESLOCA_ESQUERDA` que receba as entradas abaixo. 
    
    * Entrada: 
        * Lista `L`
        * ˋN=TAMANHO(L)ˋ
        * `i` é a posição que será liberada
    * Saída:
        * `L` é modificado diretamente. a função não retorna nada.
    
    Teste seu algoritmo com os seguintes parâmetros.
    
    - 
    ```
    Entrada: L = [], i=0
    Saída: L = []
    ```
    - 
    ```
    Entrada: L = [1], i=0
    Saída: L = []
    ```
    - 
    ```
    Entrada: L = [1], i=1
    Saída: L = [1]
    ```
    - 
    ```
    Entrada: L = [1, 2, 3], i=0
    Saída: L = [2, 3]
    ```
    - 
    ```
    Entrada: L = [1, 2, 3], i=1
    Saída: L = [1, 3]
    ```


    !!! answer 
        Esse será feito na lousa. Aproveite para anotar o resultado.
        
!!! exercise long id_list_remove_algo
    Use a função acima para criar o algoritmo da operação `REMOVE(L, V)`.
   
    !!! answer
        ```
        REMOVE(L, V)
        
        N = TAMANHO(L)
        PARA i = 0 ATÉ N FAÇA
            SE L[i] = V ENTÃO
                DESLOCA_ESQUERDA(L, N, i)
                Decrementa TAMANHO(L)
                RETORNA
            FIM
        FIM
        ```
        
        Esse algoritmo tem duas partes importantes:
        
        1. encontrar um índice `i` tal que `L[i] = V`
        2. usar o `DESLOCA_ESQUERDA` para sobrescrever o elemento na posição `j` e diminuir o tamanho da lista.
    
### Redimensionamento

Vamos agora analizar a situação das variáveis `capacidade` e `tamanho` quando realizamos inserções e remoções.

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
        Neste caso, como o `Array` que usamos em nosso vetor está quase cheio (6/8 posições ocupadas) a capacidade se mantém. Assim como na inserção, a remoção sempre mexe no tamanho do vetor.

!!! progress
    Continuar

Agora que já relembramos os conceitos mais importantes, vamos modificar o algoritmo `INSERE` para permitir que a lista cresça de tamanho. Nossa estratégia será executar o seguintes passos **logo no início** de `INSERE`.

* Entrada:
    * `Lista L`
* Saída:

```
REDIMENSIONA_SE_PRECISAR(L)

A = Array com dados de L
N = TAMANHO(L)
C = TAMANHO(A)

SE C == N ENTÃO
    A_NOVO = NOVO_ARRAY(2 * N)
    PARA CADA i=0 ATÉ N FAÇA
        A_NOVO[i] = A[i]
    FIM

    Array de dados de L = A_NOVO
FIM
```

!!! exercise choice id_adt_lista_capacidade_tamanho_redimensiona1
    Em um dado momento nosso vetor dinâmico tem `capacidade=8` e `tamanho=8`. Após a inserção de um novo elemento, quais serão os valores dessas duas quantidades?

    - [X] capacidade=16, tamanho=9
    - [ ] capacidade=16, tamanho=8
    - [ ] capacidade=8, tamanho=9
    - [ ] capacidade=8, tamanho=8

    !!! answer
        O `Array` está cheio, então precisamos aumentá-lo. Nosso algoritmo acima dobra a capacidade do array de `L`. Logo, a nova capacidade de `L` é 16 enquanto o tamanho de `L` só aumenta 1 (que é o novo elemento inserido).


!!! exercise choice id_adt_lista_capacidade_tamanho_redimensiona2
    Em um dado momento nosso vetor dinâmico tem `capacidade=16` e `tamanho=15`. Após a inserção de um novo elemento, quais serão os valores dessas duas quantidades?

    - [X] capacidade=16, tamanho=16
    - [ ] capacidade=16, tamanho=15
    - [ ] capacidade=8, tamanho=16
    - [ ] capacidade=8, tamanho=15

    !!! answer
        A checagem de lista cheia ocorre no início de `INSERE`, mas o `Array` de dados de `Lista` só fica cheio ao fim de `INSERE`. Logo, não há redimensionamento.


A mesma estratégia pode ser usada na remoção, desta vez para diminuir a capacidade pela metade se o tamanho for menor que 1/4 da capacidade. A parte final desse guia será implementar essa lógica na [APS deste módulo](aps.md)



