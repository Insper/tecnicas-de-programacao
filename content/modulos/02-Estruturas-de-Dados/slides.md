# Técnicas de Programação

## Tipos abstratos de dados

------

# Algoritmo: sequência de passos (finita) para resolver um problema

------

# Busca por termos em um projeto

### Ctrl+Shift+F no VSCode
### Fuzzy matching

----------

# Soluções com Array?

-------------

# Algoritmos

Precisamos armazenar dados. Até agora sabemos usar os seguintes recursos em Java e Python

- listas, dicionários para dados "puros"
- classes para dados + comportamentos

------

# Quantas operações são feitas? 

E se o código usar `ArrayList` ou `HashMap`?

1. não conhecemos como list/dict/ArrayList/TreeMap funcionam
2. APIs diferentes dificultam saber exatamente o que queremos dizer

## `list.append` ou `ArrayList.add` não são passos **bem definidos**

----

# Tipo Abstrato de Dados

Nomear uma estrutura para armazenamento de dados e definir

- conjunto de operações válidas
- restrições na lógica dessas operações

## Implementação pode ocorrer em qualquer linguagem

----------

# Estrutura de Dados

- esquema de armazenamento de dados na memória 
- algoritmos para implementar todas as operações de uma *ADT*
- *complexidade computacional* de cada operação (notação $\mathcal{O}$)

----------

# Array

Tipo de dados mais primitivo e representa uma coleção de objetos contínua indexada por um número inteiro começando em `0`. Tem tamanho fixo.

- `NOVO_ARRAY(N)` - cria array com capacidade `N>0`
- `TAMANHO(A)`- devolve o número de elementos do array
- `A[i]` - devolve o elemento de índice `i`. Se `i<0` ou `i>=TAMANHO(A)` dá erro

----

# Exemplo

- **Entrada**: Array `A`, inteiro `V`
- **Saída**:
    - `Verdadeiro` se o array contém o elemento `V`
    - `Falso` caso contrário

```
PARA i = 0 ATÉ TAMANHO(A) FAÇA
    SE A[i] = valor ENTÃO
        RETORNE Verdadeiro
    FIM
FIM

RETORNE Falso
```

-----

# Desempenho

- Acesso a elemento indexado: $\mathcal{O}(1)$ (tempo constante)
- Checar se elemento está presente: 
    - Se ordenado: $\mathcal{O}(\log_2 n)$ (linear)
    - Caso contrário :$\mathcal{O}(n)$ (linear)
- Inserção/remoção: não é possível

onde $n=TAMANHO(A)$.

---------

# E para implementar?

- Em Python, o tipo `list` pode ser usado para representar um array
- Em Java temos o tipo `Array` "de verdade", mas poderíamos usar um `ArrayList` inicializado com valor `0`, por exemplo.

## Todas essas opções respeitam os comportamentos definidos na ADT `Array`

------------

# Módulo *Estruturas de dados*

- Arrays e Listas 
- Tabelas de Hash e Dicionários
