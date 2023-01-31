# APS

A tarefa para entrega deste módulo será implementar algumas estruturas de dados comuns. Todas elas já tem implementações equivalentes (e mais bem feitas) na biblioteca padrão de Java. Nosso objetivo aqui é ter um olhar aprofundado em como elas poderiam ser implementadas e o quanto nossa implementação se aproxima da referência da JVM.

## Lista

Nossa implementação de lista é definida usando a interface `InsperList`, que segue de perto a ADT [List](list.md) que estudamos na [Aula 01](arrays-e-listas.md). Segue um resumo das operações suportadas por este tipo.

- **Inserção**:
  - em qualquer lugar 
  - no fim
- **Remoção**:
  - da primeira ocorrência de um elemento 
  - de um índice
- **Acesso a elementos**:
  - via índice usando o método `get` e `set`
  - tamanho da lista com método o `size()`

Você deverá criar uma classe `InsperArrayList` que implementa a interface `InsperList` no local apontado no código da APS. 

!!! warning
    Sua implementação deverá usar *Generics* e ser feita usando um array simples (uma variável do tipo `Object[]`). Ou seja, sua implementação **não** pode usar ArrayList, LinkedList ou qualquer outra classe de armazenamento de dados da JVM.

Não se esqueça que você deverá implementar o redimensionamento do `Array` nos métodos `insert` e `remove`. Seu vetor deve começar com capacidade `8` e seguir o algoritmo estudado em aula. Ao remover elementos, o `Array` deverá ter seu tamanho diminuido pela metade se o tamanho do vetor for menor que 25% da capacidade.

## Dicionário (*Map*)

Nossa implementação de lista é definida usando a interface `InsperMap`, que segue de perto a ADT [Map](map.md). Você deverá implementar a classe `TwoListMap` seguindo os algoritmos que estudamos na [Aula 02](listas-e-dicionarios.md). Essa classe deverá seguir a interface `InsperMap`. 


!!! warning
    Sua implementação deverá usar variáveis do tipo `InsperList` para guardar as listas de chaves. Ou seja, sua implementação **não** pode usar ArrayList, LinkedList ou qualquer outra classe de armazenamento de dados da JVM.

## Exercícios

Vamos agora resolver dois exercícios práticos simples usando nossas novas Estruturas de Dados. Pode ser útil ver o guia de [String em Java](../00-Algoritmos/java/strings.md) antes de continuar.


!!! exercise 
    Uma das primeiras coisas que precisamos checar para ver se um programa Java é válido é se os parênteses estão balanceados. Ou seja, se todo `(`, `[` e `{` que é aberto é eventualmente fechado *respeitando a ordem de abertura*. Ou seja, `({)}` é inválido pois `)`fechou antes dos parênteses abertos após seu a abertura inicial correspondente. 

    Implemente o método `#!java boolean parentesesBalanceados(String codigo)` na classe `br.edu.insper.tecprog.aps01.Parenteses`. Você deverá obrigatoriamente usar um `InsperList`. A cada vez que um parêntese é aberto (usando os caracteres `(`, `[` ou `{`) você deve adicioná-lo ao fim da lista. Quando um caractere de fechamento de parêntese for encontrado você deve compará-lo com o último elemento. Se forem correspondentes então continue. Se não forem retorne `false`. Ao chegar no fim do texto a lista deverá estar vazia (já que se houver algo então existe um parênteses que não foi fechado).


!!! exercise
    Vamos fazer agora um contador de palavras em um texto. Dado um texto, seu programa deverá passar por cada palavra e contar o número de ocorrências. Seu trabalho será implementar o método `#!java InsperMap<String, Integer> contaPalavras(String texto)` da classe `br.edu.insper.tecprog.aps01.ContaPalavras`. 
