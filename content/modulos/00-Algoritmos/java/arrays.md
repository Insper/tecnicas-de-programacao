# Arrays

Em Java o tipo de dado "composto" (que representa uma coleção de dados) mais básico é o *Array*. Esse tipo lembra muito o `list` de Python, com a diferença que tem tamanho fixo. Veja os exemplos de código abaixo para conhecer o funcionamento desse tipo.

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

    ```java
    for (int i = 0; i < arr.length; i++) {
        // faz algo com arr[i] aqui
    }
    ```

    - acesso via índice do elemento atual (variável `i`)
    - especialmente útil para acessar elementos vizinhos (via `i+1` ou `i-1`)

2. **Percorrer elemento a elemento**:

    ```java
    for (var item : arr) {
        // faz algo com item aqui
    }
    ```

    - só acessa o elemento atual
    - mais legível
