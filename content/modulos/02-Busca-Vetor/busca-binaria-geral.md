# Busca binária (II)

Uma parte importante do nosso algoritmo de busca binária é que ele parece se autoreferenciar. Veja abaixo:

`BUSCA_BINARIA_BUG(A)`

1. seleciona o elemento na posição exatamente no meio do vetor
2. se esse elemento for `0`, continua procurando na metade da da direita do vetor 
3. se esse elemento for `1`, continua procurando na metade da esquerda do vetor
4. repete esse procedimento até encontrar um elemento que é `1` e tem um vizinho que é `0`.


Quando dizemos **repita esse procedimento** em uma parte específica do array estamos fazendo uma referência circular: nosso algoritmo usa ele mesmo para processar a metade do array que contém o elemento procurado. Essa estratégia de escrita de soluções é chamada de **recursão** em computação. 

Um **algoritmo recursivo** faz uma ou mais chamadas a si mesmo. Ou seja, existe em seu design a ideia de que o algoritmo (inteiro) se repete múltiplas vezes. De uma certa maneira, **recursão é uma técnica que representa a ideia de repetição**, mas diferente de loops estamos repetindo o algoritmo inteiro para resolver um subproblema. 


## Um primeiro algoritmo recursivo

Vamos começar com um exemplo um pouco artificial de algoritmo recursivo: a busca em array de frente para trás. 

!!! warning
    Não existe vantagem em trabalhar com um algoritmo recursivo para este problema. Ele é usado como exemplo pois é familiar para vocês e simples o suficiente. Iremos ver outros algoritmos recursivos no semestre. 
    
Podemos escrever a busca como a seguinte ideia:

1. ou o elemento procurado é o primeiro elemento
2. ou ele está no restante do array.

Ou seja, se encontrei ele no índice `0` então deu certo. Se não procuro no resto do vetor. **Aqui temos uma repetição do algoritmo, mas para uma parte diferente dos dados!**. Vamos estruturar um pouco mais: nosso algoritmo se chamará `BUSCA_RECURSIVA`, onde `A` é um array e `V` é o valor buscado. 

1. se `A[0] = V` DEVOLVA 0
2. senão faça a busca no vetor começando do índice `1`.

Note que agora faríamos o seguinte:

1. se `A[1] = V` DEVOLVA 1
2. senão faça a busca no vetor começando do índice `2`.

E assim por diante até acabar o array `A`. Note que não especificamos o que fazer neste caso. Vamos então adicionar uma condição extra: se chegar no fim do array `DEVOLVA 0`. Essa condição é chamada de **base da recursão** pois define quando o programa para de chamar a si mesmo.

Veremos agora uma versão mais formalizada: `BUSCA_RECURSIVA(A, V, INDICE)`. Sempre começamos com `INDICE=0` e executamos os seguintes passos:

```
BUSCA_RECURSIVA(A, V, INDICE)
    SE INDICE = TAMANHO(A) - 1 ENTÃO 
        DEVOLVA 0
    FIM

    SE A[INDICE] = V ENTÃO 
        DEVOLVA 1
    FIM

    DEVOLVA BUSCA_RECURSIVA(A, V, INDICE + 1)
```

## Busca binária recursiva

Podemos usar essa mesma para a busca binária! Vejamos:

`BUSCA_BINARIA_BUG(A)`

1. seleciona o elemento na posição exatamente no meio do vetor
2. se esse elemento for `0`, continua procurando na metade da da direita do vetor 
3. se esse elemento for `1`, continua procurando na metade da esquerda do vetor
4. repete esse procedimento até encontrar um elemento que é `1` e tem um vizinho que é `0`.

Ao invés de usarmos um loop como fizemos na [atividade anterior](busca-binaria-exemplo.md), que ia até que `INICIO = FIM-1`, agora podemos fazer os passos `2` e `3` chamando a própria busca binária novamente. 

Redefinimos o algoritmo então recebendo `INICIO` e `FIM` para ser `BUSCA_BINARIA_REC(A, V, INICIO, FIM)` e ao fazermos então, nos passos 2 e 3, as chamadas recursivas mudamos o intervalo `INICIO-FIM` analisado. 

!!! exercise long
    Tente fazer uma versão recursiva da busca binária abaixo.

    !!! answer
        Isso será feito em aula na lousa. Use o botão "Editar" para fazer anotações após a discussão. 