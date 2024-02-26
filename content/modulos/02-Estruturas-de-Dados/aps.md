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

Vamos agora resolver dois exercícios práticos simples usando nossas novas Estruturas de Dados. Pode ser útil rever o guia de [Strings](../00-Algoritmos/java/strings.md) antes de continuar.

!!! exercise
    O departamento de marketing da sua empresa está interessado em obter apenas os números de telefone celular, separando-os dos telefones fixos. Para simplificar esta operação serão considerados números de celular apenas aqueles que, após o código de área, iniciarem com o dígito adicional 9.

    Você recebeu a tarefa de obter uma lista com os números de celular, sem o código de área. Entretanto, o cadastro de telefones do departamento de marketing não está padronizado e existem números seguindo 3 formatos distintos:

    1. Números completos (13 ou 14 caracteres), incluindo o código do país (+55) e o código de área (ex: 11);
    2. Número contendo apenas o código de área (10 ou 11 caracteres);
    3. Número sem código de área (8 ou 9 caracteres).

    Faça uma função que recebe uma lista de números de telefone e retorna uma lista contendo apenas os telefones celulares. Cada telefone da lista de entrada (recebida como argumento da sua função) pode estar em qualquer um dos 3 formatos acima. Os telefones da lista de saída (retornada pela sua função) devem conter apenas os dígitos do telefone, removendo o código do país e código de área se for necessário.

    **Refaça seu algoritmo anterior usando o tipo `InsperList`**



!!! exercise 
    Uma das primeiras coisas que precisamos checar para ver se um programa Java é válido é se os parênteses estão balanceados. Ou seja, se todo `(`, `[` e `{` que é aberto é eventualmente fechado *respeitando a ordem de abertura*. Ou seja, `({)}` é inválido pois `)`fechou antes dos parênteses abertos após seu a abertura inicial correspondente. 

    Implemente o método `#!java boolean parentesesBalanceados(String codigo)` na classe `br.edu.insper.tecprog.aps01.Parenteses`. Você deverá obrigatoriamente usar um `InsperList`. A cada vez que um parêntese é aberto (usando os caracteres `(`, `[` ou `{`) você deve adicioná-lo ao fim da lista. Quando um caractere de fechamento de parêntese for encontrado você deve compará-lo com o último elemento. Se forem correspondentes então continue. Se não forem retorne `false`. Ao chegar no fim do texto a lista deverá estar vazia (já que se houver algo então existe um parênteses que não foi fechado).


!!! exercise
    Vamos fazer agora um contador de palavras em um texto. Dado um texto, seu programa deverá passar por cada palavra e contar o número de ocorrências. Seu trabalho será implementar o método `#!java InsperMap<String, Integer> contaPalavras(String texto)` da classe `br.edu.insper.tecprog.aps01.ContaPalavras`. 
