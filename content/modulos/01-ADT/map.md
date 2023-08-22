# Map

Um `Map` é uma mapeamento **chave $\rightarrow$ valor** em que cada chave pode estar a associada a um único valor. Note que um valor pode estar associado a várias chaves, mas cada chave só possui um valor. As seguintes operações são suportadas:

- `NOVO_MAP()` - cria um novo `Map`
- `SET(M, K, V)` - associa o valor `V` à chave `K`. Se a chave `K` já existir substitui o valor.
- `GET(M, K)` - devolve o valor associado a chave `K`. Se não houver retorna `VAZIO`
- `REMOVE(M, K)` - remove o par com chave `K`. Se não houver não faz nada.
- `TAMANHO(M)` - devolve o número de chaves que possuem um valor associado
