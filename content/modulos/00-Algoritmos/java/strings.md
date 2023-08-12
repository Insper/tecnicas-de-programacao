# Strings

Strings em Java possuem recursos muito parecidos com o que já conhecemos de Python. Veja alguns exemplos introdutórios abaixo.

=== "Pseudo código" 
    ```
    S ← "Bla bla bla"

    # mostra no terminal
    PRINT("Valor de s:" + S)

    # cópia de trechos da string
    bla1 ← SUBSTRING(S, 0, 3) # Bla
    bla3 ← SUBSTRING(S, 8) # Vai até o fim se não passar o segundo

    LOWER ← LOWERCASE(S)

    # checa se a string é vazia
    v ← EH_VAZIO(S)

    # checa se a string é só de espaços em branco
    v ← SO_ESPACOS(S)
    
    # checa se duas strings são iguais
    igual ← S = bla1
    ```

=== "Java"
    ```java
    String s = "Bla bla bla";

    // mostra no terminal
    System.out.println("Valor de s: " + s);

    // cópia de um trecho da String
    String bla1 = s.substring(0, 3); // Bla
    String bla3 = s.substring(8); // bla - vai até o fim da String se não passar o segundo

    String lower = s.toLowerCase(); // bla bla bla

    // checa se é string vazia
    s.isEmpty();

    // checa se a string é só de espaços em branco
    s.isBlank();

    // checa se duas strings são iguais
    boolean igual = s.equals(bla1);
    ```

!!! warning
    Nunca use `==` para comparar Strings. O correto é sempre usar o método `equals()`. Isso na verdade vale para todos objetos em Java. 

Em Pseudo código vamos tratar `String` sempre como um array, porém na implementação em Java existem algumas diferenças importantes.

### String vs Char

Em Java a String é uma sequência de `char`, um objeto que representa um único caractere. Quando queremos representar um único caractere usando aspas simples (por exemplo, `'a'`). Quando queremos uma sequência de `char` sempre usamos aspas duplas (por exemplo, `"texto"`)

```java
char c = 'a'; // só um caractere

// substitui toda ocorrência da letra 'a' por 'e'
String ble = s.replace('a', 'e');  // Ble ble ble
```

!!! exercise choice id_java_char_string_equals
    A expressão `'a' == "a"` é avaliada como 

    - [ ] `true`
    - [X] `false`

    !!! answer
        Uma string de tamanho 1 (com um só caractere) é diferente de do caractere sozinho em si. A expressão continuaria `false` se tentássemos algo do tipo `"a".equals('a')`, já que nesse caso os tipos são diferentes. 

Algumas operações corriqueiras com strings são:

1. **Percorrer caracteres usando índice**:

    === "Pseudo código"
        ```
        PARA CADA I=0 ATÉ TAMANHO(S) FAÇA
            # FAZ ALGO COM S[I] AQUI
        FIM
        ```
    === "Java"
        ```java
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            // faz algo com c aqui
        }
        ```

    - pode acessar vizinhos
    - tem índice e caractere ao mesmo tempo

2. **Processar por linhas**:

    === "Pseudo código"
        ```
        PARA CADA LINE EM DIVIDE(S, "\n") FAÇA
            # FAZ ALGO COM LINE AQUI
        FIM
        ```
    === "Java"
        ```java
        for (String line : s.split("\n")) {
            // usa line aqui
        }
        ```

3. **Separar por espaços em branco**:

    === "Pseudo código"
        ```
        PARA CADA ITEM EM DIVIDE(S, "\s") FAÇA
            # FAZ ALGO COM ITEM AQUI
        FIM
        ```
    === "Java"

        ```java
        for (String word : s.split("\\s")) {
            // usa word aqui
        }
        ```

A operação `DIVIDE(S, P)` divide uma string pelo padrão `P`, retornando um `ARRAY` de `String` com as partes de `S`. Padrões comuns são `"\n"` (linhas) e `"\s"` (espaços).

Java tem uma extensa documentação online. Todos os métodos de *String* podem ser vistos [neste link](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html).