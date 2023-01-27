# APS

A tarefa para entrega deste módulo será implementar algumas estruturas de dados comuns. Todas elas já tem implementações equivalentes (e mais bem feitas) na biblioteca padrão de Java. Nosso objetivo aqui é ter um olhar aprofundado em como elas poderiam ser implementadas e o quanto nossa implementação se aproxima da referência da JVM.

## Lista

Nossa implementação de lista é definida usando a interface `InsperList`, que segue de perto a ADT [List](list.md) que estudamos na [Aula 01](arrays-e-listas.md). Segue um resumo das operações suportadas por este tipo.

- **Inserção**:
  - Em qualquer lugar com o método `insert`
- **Remoção**:
  - da primeira ocorrência de um elemento com o método `remove`
- **Acesso a elementos**:
  - Via índice usando o método `get` e `set`
  - Tamanho da lista com método o `size()`

Você deverá criar uma classe `InsperArrayList` que implementa a interface `InsperList` no local apontado no código da APS. 

!!! warning
    Sua implementação deverá usar *Generics* e ser feita usando um array simples (uma variável do tipo `Object[]`). Ou seja, sua implementação **não** pode usar ArrayList, LinkedList ou qualquer outra classe de armazenamento de dados da JVM.

A rubrica **Básico** leva em conta que a lista tem `capacidade=100` sempre.

### Avançado

Implemente o redimensionamento do `Array` nos métodos `insert` e `remove`. Seu vetor deve começar com capacidade `100` e dobrar de tamanho sempre que encher. Ao remover elementos, o `Array` deverá ter seu tamanho diminuido pela metade se o tamanho do vetor for menor que 25% da capacidade.

A maneira mais correta de indicar que um método falhou é lançar uma exceção. Os métodos `get`, `set`, `insert` e `remove` podem receber índices inválidos e/ou `null` em seus argumentos. Lance as execeções descritas nos comentários presentes na definição da interface `InsperList`.

## Conjunto

O tipo *conjunto* representa uma coleção de valores sem ordem nem repetição. É possível listar todos os elementos de um conjunto, assim como adicionar, remover e checar se um elemento específico pertence ao conjunto.

A descrição completa do tipo de dados está na interface `InsperSet`. Você deverá implementar uma classe `InsperListSet` no local apontado no código da APS. Sua implementação deverá usar um `InsperArrayList` para armazenar os dados.

### Avançado

As operações de união e interseção entre conjuntos são importantes em diversos problemas. A interface `InsperSetAvancado` descreve métodos para estas operações. Implemente essa interface na sua classe `InsperListSet`.

## Pilha

A estrutura Pilha é usada em diversas situações em que necessitamos armazenar elementos em ordem e percorrê-los na ordem oposta a que foram armazenados. Em inglês usa-se muito a sigla **LIFO**, que significa *Last In, First Out* (último a entrar, primeiro a sair). 

Suas principais operações são 

- adicionar no topo da pilha
- remover do topo da pilha
- verificar se a pilha está vazia

Implemente uma classe `InsperListStack` que obedece a interface `InsperStack` definida no código da APS. Você deve usar seu tipo `InsperArrayList` para armazenar os dados. 

### Avançado

Implemente o método `parentesesBalanceados` na classe `UsosStack` usando sua classe `InsperListStack`. A cada vez que um parêntese é aberto (usando os caracteres `(`, `[` ou `{`) você deve empilhá-lo. Quando um caractere de fechamento de parêntese for encontrado você deve compará-lo com o topo da pilha. Se forem correspondentes então continue. Se não forem retorne `false`

Ao final do texto a pilha deverá estar vazia.

## Fila

Filas são muito usadas em situações em que várias pessoas/programas desejam acessar um único recurso. Por exemplo, programas que desejam enviar/receber dados da internet entram em uma fila para terem acesso a placa de rede. Filas também são usadas em sistemas de compra de ingressos em shows. Em inglês usa-se muito a sigla **FIFO** - *First in, First out* (primeiro a entrar, primeiro a sair). Em geral não é desejável que uma fila tenha tamanho infinito. Por isso filas são criadas com um tamanho máximo de capacidade.

As principais operações de uma fila são 

- criar fila com tamanho máximo `N`
- entrar no fim da fila com `enqueue`
- sair do começo da fila com `dequeue`
- checar se a fila está cheia/vazia com `isFull`/`isEmpty`

Assim como nos outros tipos de dados, implemente a interface `InsperQueue` na classe indicada no código da APS usando o tipo `InsperList`. 

### Avançado

A maneira mais correta de indicar erros nos métodos `enqueue`/`dequeue` é que eles lancem exceções quando a fila estiver cheia/vazia. Implemente esta funcionalidade. 
