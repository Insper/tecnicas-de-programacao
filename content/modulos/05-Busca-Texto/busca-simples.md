# Busca em Strings

O problema básico da busca em strings é, dado um texto `T`, encontrar a primeira (ou todas) ocorrência de uma uma consulta `Q`. Apesar de simples, esse problema possui diversos algoritmos complexos e é um dos problemas fundamentais na área de algoritmos.


## Prefixos e sufixos

Vamos começar com algumas definições:

- Uma string `Q` de tamanho `N` é prefixo de uma string `S` se os primeiros `N` caracteres de `S` são iguais a `Q`
- Uma string `Q` de tamanho `N` é sufixo de uma string `S` se os últimos `N` caracteres de `S` são iguais a `Q`

Apesar dessas definições não serem complexas, elas já direcionam bem a criação de programas que implementem essse comportamento.

!!! exercise long
    Escreva um algoritmo `PREFIXO(S, Q)` que checa se Q é prefixo de `S`. Teste com as seguintes entradas:

    - `S="aa", Q="a"`
    - `S="abcaas sdfsd a", Q="abc"`
    - `S="a", Q="abc"`
    - `S="aabc", Q="abc"`

!!! exercise long
    Escreva um algoritmo `SUFIXO(S, Q)` que checa se Q é sufixo de `S`. Teste com as seguintes entradas:

    - `S="aa", Q="a"`
    - `S="abcaas sdfsd a", Q="abc"`
    - `S="a", Q="abc"`
    - `S="aabc", Q="abc"`

!!! exercise short
    Qual é a complexidade dos algoritmos `PREFIXO` e `SUFIXO` (em termos do tamanho `N` da entrada `Q`)?

    !!! answer
        Ele faz `N` operações, no máximo.

## Buscando termos

Vamos começar já escrevendo um algoritmo para esse problema!

!!! exercise long
    Escreva um algoritmo `BUSCA(S, Q)` que 

    - devolve -1 se `Q` não for encontrado em `S`
    - devolve o índice da primeira ocorrência de `Q` em `S`
    
    Uma ideia geral deste algoritmo é verificar se `Q` é um prefixo de `S` começando em todas as posições possíveis. Por exemplo, com `Q="Abc" e `S="a Abce 22"` temos que `Q` é um prefixo de `S` a partir do índice `2` de S.

    **Você não deve chamar o algoritmo `PREFIXO`, mas sim incorporá-lo em `BUSCA`.**


Acabou os algoritmos, agora vamos implementá-los na [parte 1 da APS](aps.md)
