# Arrays

Quando representamos algoritmos o tipo mais básico de dados compostos que temos é o *Array*, que representa uma coleção de objetos do mesmo tipo contínua indexada por um número inteiro começando em `0`. Tem tamanho fixo. As seguintes operações estão disponíveis em um `Array`.

- `NOVO_ARRAY(N)` - cria array com capacidade `N>0`
- `TAMANHO(A)`- devolve o número de elementos do array
- `A[i]` - devolve o elemento de índice `i`. Se `i<0` ou `i>TAMANHO(A)` dá erro


Vejamos então como escrever essas operações com Pseudo-código e com Java:

=== "Pseudo código"

    ```
    # Cria array com 10 int
    ARR := NOVO_ARRAY(10)

    # Acessa elementos do array
    ARR[0] := 5
    ARR[1] := ARR[0] + 2;

    # tamanho do array. Nunca muda
    N := TAMANHO(ARR) # 10
    ```

=== "Java"

    ```java
    // Cria array com 10 int
    var arr = new int[10];

    // Acessa elementos do array
    arr[0] = 5;
    arr[1] = arr[0] + 2;

    // tamanho do array. Nunca muda
    var n = arr.length; // 10
    ```

A operação mais comum com um *array* é *percorrer o array, passando por todos os elementos*. Podemos fazer isso de duas maneiras:


1. **Percorrer usando índice**:
    
    === "Pseudo código"

        ```
        PARA CADA I=0 ATÉ TAMANHO(ARR) FAÇA
            # FAZ ALGO COM ARR[I] AQUI
        FIM
        ```

    === "Java"

        ```java
        for (int i = 0; i < arr.length; i++) {
            // faz algo com arr[i] aqui
        }
        ```

    - acesso via índice do elemento atual (variável `i`)
    - especialmente útil para acessar elementos vizinhos (via `i+1` ou `i-1`)

2. **Percorrer elemento a elemento**:
    
    === "Pseudo código"

        ```
        PARA CADA ITEM EM ARR FAÇA
            # FAZ ALGO COM ITEM AQUI
        FIM
        ```

    === "Java"

        ```java
        for (var item : arr) {
            // faz algo com item aqui
        }
        ```

    - só acessa o elemento atual
    - mais legível
