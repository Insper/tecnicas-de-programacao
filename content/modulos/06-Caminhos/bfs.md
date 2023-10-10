# Busca em Largura

Agora que já implementamos por completo a busca em profundidade (DFS) podemos dar um novo passo na resolução do labirinto: **encontrar a saída mais próxima**.

O algoritmo básico da DFS não se preocupa com o tamanho dos caminhos, apenas com existir um caminho. Ou seja, ele é muito útil quando queremos

- encontrar todas as casas acessíveis a partir de um certo lugar
- detectar ciclos: maneiras de sair de uma casa e voltar para ela

Isso vem da própria definição que usamos para criar nosso algoritmo recursivo, que não tinha nada sobre o comprimento de um caminho, apenas sobre a **existência** de um caminho.

Por isso a busca em largura vai colocar a distância como parte principal de seu funcionamento. Iremos explorar os caminhos em "ondas":

1. primeiro encontraremos todas casas acessíveis usando caminhos de tamanho máximo 1
2. em seguida, encontraremos todas as casas acessíveis usando caminhos de tamanho máximo 2
3. repetimos essa ideia, encontrando as casas acessíveis usando caminhos cada vez maiores. 

Um ponto importante aparece aqui: **saber as casas acessíveis usando caminhos de tamanho no máximo $n$ nos ajuda a encontrar todas as casas acessíveis usando caminhos de tamanho no máximo $n+1$!** Fazemos isso colocando as casas a serem visitadas em uma Fila.

## A fila

Usaremos uma ADT para fila com as seguintes opções:

- `NOVA_FILA()`
- `REMOVE_PRIMEIRO(F)` - devolve o primeiro elemento da fila e o remove
- `ADICIONA_NO_FIM(F, EL)` - adiciona um elemento no fim da fila
- `VAZIA(F)` - retorna `VERDADEIRO` se `F` estiver vazia


## Busca em Largura - alto nível

Na última aula fizemos simulações do funcionamento da busca em largura e criamos um pseudo código em alto nível na lousa. Vejamos as variáveis necessárias para seu funcionamento

- `LABIRINTO L`
- `FILA F` - guarda a ordem em que visitaremos as casas
- `DIST`- matriz que guarda a distância até a fonte. Tem valor -1 para casas não visitadas
- `fI, fJ` - posição da fonte
- `dI, dJ` - posição do destino

O algoritmo era parecido com o seguinte:

```
BFS(L, fI, fJ, dI, dJ, DIST, F)

ADICIONA_NO_FIM(F, (fI, fJ))
DIST[fI][fJ] = 0

ENQUANTO NÃO VAZIA(F) FAÇA
    cI, cJ <- REMOVE_PRIMEIRO(F)

    SE CHEGOU NO DESTINO ENTÃO
        PARE O LOOP
    FIM
    
    PARA CADA VIZINHO vI, vJ NÃO VISITADO FAÇA
        DIST[vI][vJ] = DIST[cI][cJ] + 1 # VISITOU 
        ADICIONA_NO_FIM(F, (vI, vJ))
    FIM
FIM

SE CHEGOU NO DESTINO ENTÃO
    USE A MATRIZ DIST PARA ENCONTRAR O TAMANHO DO CAMINHO
    RECRIE O CAMINHO "ANDANDO PARA TRÁS" NAS DISTÂNCIAS
FIM
```

Seu desafio será transformar esse pseudo código alto nível em uma implementação completa da busca em largura. Volte para o [enunciado da APS](aps.md) e use os testes para verificar sua implementação.
