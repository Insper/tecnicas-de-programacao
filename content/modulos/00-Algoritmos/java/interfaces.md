# Interfaces

Uma interface em Java é um conjunto de métodos que definem parcialmente o comportamento de uma classe. Diferentemente de herança, os métodos de uma interface não tem implementação. Ou seja, *Interface* não define **como** essa classe implementa esses comportamentos, somente **quais são** os comportamentos. 

## Definindo uma interface

A definição de uma classe lembra muito uma classe Java. O exemplo abaixo mostra a sintaxe usada. Os métodos no exemplo não tem nenhum significado especial a não ser demonstrar como declará-los. 

```java
package br.edu.insper.tecprog.exemplos;

public interface InterfaceExemplo {
    public void metodo1(int a);
    public boolean isCompatible(Exemplo e);
}
```

## Implementando uma interface

Para implementar uma interface basta adicionar `implements XX` na declaração da classe. Cada classe só poder herdar de uma super classe, mas pode implementar diversas interfaces. 

```java
package br.edu.insper.tecprog.exemplos;

public class Exemplo implements InterfaceExemplo {

    public void metodo1(int a) {
        // algo aqui
    }
    public boolean isCompatible(Exemplo e) {
        return false;
    }

    // outros métodos vão aqui

}
```

Se houver algum método que não estiver implementado o código não compila. Iremos implementar várias interfaces nessa disciplina. Seu uso será principalmente para representar a *API pública* de objetos que vocês irão implementar. 