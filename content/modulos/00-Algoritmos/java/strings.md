# Strings

Strings em Java possuem recursos muito parecidos com o que já usaram em Python. Veja alguns exemplos introdutórios abaixo.

```java
var s = "Bla bla bla";

// mostra no terminal
System.out.println("Valor de s: " + s);

// cópia de um trecho da String
var bla1 = s.substring(0, 3); // Bla
var bla3 = s.substring(8); // bla - vai até o fim da String se não passar o segundo

var lower = s.toLowerCase(s); // bla bla bla

// checa se é string vazia
s.isEmpty()

// checa se a string é só de espaços em branco
s.isBlank()
```

!!! warning
    Nunca use `==` para comparar Strings. O correto é sempre usar o método `equals()`. Isso na verdade vale para todos objetos em Java. 

Em Java a String é uma sequência de `char`, um objeto que representa um único caractere. Quando queremos representar um único caractere usando aspas simples (por exemplo, `'a'`).

```java
char c = 'a'; // só um caractere

// substitui toda ocorrência da letra 'a' por 'e'
var ble = s.replace('a', 'e');  // Ble ble ble
```

Algumas operações corriqueiras com strings são:

1. **Percorrer caracteres usando índice**:
    ```java
    for (int i = 0; i < s.length; i++) {
        char c = s.charAt(i);
        // faz algo com c aqui
    }
    ```

    - pode acessar vizinhos
    - tem índice e caractere ao mesmo tempo

2. **Processar por linhas**:
    ```java
    for (String line : s.split("\n")) {
        // usa line aqui
    }
    ```

3. **Separar por espaços em branco**:
    ```java
    for (String word : s.split("\s")) {
        // usa word aqui
    }
    ```


Java tem uma extensa documentação online. Todos os métodos de *String* podem ser vistos [neste link](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html).