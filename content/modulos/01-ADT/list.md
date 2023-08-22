# List

O Tipo de dados `List` é uma coleção de valores indexados por um inteiro não negativo (maior ou igual a zero) sem espaços vazios. Essa coleção pode aumentar ou diminuir de tamanho e suporta as seguintes operações:

- `NOVA_LISTA()` - cria nova lista vazia
- `TAMANHO(L)`- devolve o número de elementos da lista
- `L[i]` - devolve o elemento de índice `i`. Se `i<0` ou `i>TAMANHO(A)` dá erro
- `INSERE(L, V, i)` - insere o valor `V` na lista `L` na posição `i`. Os elementos a partir da posição `i` são "empurrados" para a direita. Essa operação incrementa o tamanho da lista.
- `REMOVE(L, V)` - remove a primeira ocorrência de `V` da lista. Se `V` não estiver presente não faz nada. Os elementos a partir do índice da primeira ocorrência de `V` são "puxados" para a esquerda. Essa operação decrementa o tamanho da lista.
