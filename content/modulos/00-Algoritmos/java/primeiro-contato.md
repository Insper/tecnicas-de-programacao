# Primeiro contato

Vamos aprender a ler o básico de código Java antes de iniciarmos os exercícios. Não é exatamente complicado, mas tem muito mais código que um programa básico em Python e isso às vezes assusta quem está começando. Vamos lá:

## A função `main`

```java
public class ClasseExemplo {
    public static void main (String args[]) {
        // aqui vai o código que é executado ao rodar o programa. 
    }
}
```

Muitos desses elementos já foram vistos em Python, só que agora tem um nome novo e explícito em Java.

1. `public class` define a criação de uma nova classe. Dentro de um arquivo podem ter várias classes, mas só uma dela pode ser `public`, que significa que ela é acessível para classes escritas em outros arquivos.
2. Em Java definimos escopo com `{ }`. Ou seja, tudo o que está entre as chaves que começam na linha 1 é parte da classe `ClasseExemplo`.
3. O código na função `main` é executado ao rodar o programa. 

## Argumentos de função e variáveis

Em Java temos uma caraterística muito importante: toda variável, argumento de função e valor de retorno de função deve ter seu tipo escrito *explicitamente* no código. 

| Tipo da variável | Nome do tipo em Java | Exemplo de declaração          |
| ---------------- | -------------------- | ------------------------------ |
| Inteiro          | `int`                | `#!java int valor = 5;`        |
| Fracionário      | `float`              | `#!java float preco = 0.1;`    |
| Texto            | `String`             | `#!java String nome = "Igor";` |
| Booleano         | `boolean`            | `#!java boolean cond = false;` |

## Implementando uma função

Todos os nossos primeiros exercícios se resumirão a implementar uma única função em Java. Em geral eles seguirão o seguinte esqueleto, que já estará preenchido no código de suporte. 

```java
package br.edu.insper.tecprog.exemplos;

public class NomeDoExercicio {
    public static tipoRetorno funcao(tipo1 arg1, tipo2 arg2) {
        // faz algo aqui
    }
}
```

- Na primeira linha definimos um "pacote" em java. Isso equivale (em termos beeeem simplificados) à pasta em que o arquivo se encontra no projeto. Ou seja, o arquivo acima se chamaria `NomeDoExercicio.java` e estaria dentro da pasta `br/edu/insper/tecprog/exemplos/`.

