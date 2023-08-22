# Array

Tipo de dados composto mais primitivo e representa uma coleção de objetos contínua indexada por um número inteiro começando em `0`. Tem tamanho fixo.

- `NOVO_ARRAY(N)` - cria array com capacidade `N>0`
- `TAMANHO(A)`- devolve o número de elementos do array
- `A[i]` - devolve o elemento de índice `i`. Se `i<0` ou `i>=TAMANHO(A)` dá erro
