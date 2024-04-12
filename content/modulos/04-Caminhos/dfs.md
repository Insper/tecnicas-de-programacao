# Aula 02 - Busca em Profundidade

Nossa primeira tentativa de resolver o Labirinto foi [seguir paredes com a mão direita](seguir-parede.md). Apesar de termos resultados positivos, algumas situações inesperadas aparecem.


!!! exercise long
    É possível resolver o seguinte labirinto com o algoritmo da aula passada?

    ```
    ##########
    #........#
    #........#
    #...###..#
    #....o...#
    #........#
    ..........
    ##########
    ```

    !!! answer
        Não dá certo! Ele fica girando na parede do centro e nunca checa na saída, mesmo ela existindo.

!!! exercise long
    Suponha agora que desejemos sair da casa `o`  e chegar na casa `X`. Isso é possível usando o algoritmo da aula passada?

    ```
    ##########
    #...##...#
    #.X..#...#
    #....#...#
    #....#...#
    #....#...#
    #....#...#
    #...###..#
    #....o...#
    ##########
    ```

    !!! answer
        O `X` não está colado em nenhuma parede, logo nunca conseguiremos chegar nele seguindo paredes. 

!!! progress
    Continuar

Podemos sintetizar os problemas acima em dois pontos:

- esse algoritmo é **muito específico para o problema tratado**. Ou seja, uma pequena modificação (encontrar saída vs ir até uma casa do labirinto) faz ele deixar de funcionar e não é simples modificá-lo para que funcione.
- existem suposições "escondidas" nesse algoritmo: ele funciona sempre que o labirinto for só de corredores. Quando existem espaços abertos ou com paredes desconectadas problemas podem ocorrer. 

Vamos então olhar uma generalização deste algoritmo: a busca em profundidade. Em cada posição, a busca em profundidade tenta visitar todas as casas vizinhas que ainda não foram visitadas. 

!!! important
    **Definição**: sejam duas casas `f`(fonte) e  `d`(destino), existe um caminho que vai de `f` até `d` se , e somente se, pelo menos uma das alternativas abaixo é verdade

    - existe um caminho entre a casa acima de `f` até `d`
    - existe um caminho entre a casa abaixo de `f` até `d`
    - existe um caminho entre a casa à esquerda de `f` até `d`
    - existe um caminho entre a casa à direita de `f` até `d`

As 4 condições podem ser resumidas em uma só: **existe um caminho entre um dos vizinhos de `f` até `d`**. Repare que essa ideia não funciona somente no labirinto, mas em qualquer situação em que tenhamos a ideia de nós que estão conectados a outros. Estudaremos essas estruturas e seus algoritmos no próximo semestre. 

!!! progress 
    Continuar


 O desenvolvimento de um algoritmo para a busca em profundidade vem direto da definição acima. Vamos tentar destrinchá-la abaixo. Nosso problema será: dado uma casa inicial `f`, existe caminho até uma casa destino `d`?

 Um algoritmo para este problema claramente seria recursivo, já que a definição apresentada acima foi apresentada dessa forma. Vamos então definir os seguintes pontos antes de montar esse algoritmo:

 1. estando em uma casa `C`, quais são as chamadas recursivas que posso fazer?
 1. qual seria a base da recursão? Ou seja 


!!! exercise choice
    No labirinto abaixo, queremos sair da casa `C` e chegar na casa `D`. Toda casa marcada com `.` nunca foi visitada, enquanto toda casa marcada com `x` já foi visitada. 

    ```
    ##########
    #........#
    #..D.....#
    #........#
    #........#
    #........#
    #........#
    #......Cx#
    #.....xxx#
    ##########
    ```

    Seriam feitas chamadas recursivas em quais vizinhos neste caso?

    - [x] cima e esquerda
    - [ ] cima, direita, baixo e esquerda
    - [ ] baixo e direita
    - [ ] nenhuma chamada seria feita

    !!! answer
        Somente serão feitas novas chamadas recursivas para os vizinhos não visitados. Casas marcadas com `x` já foram visitadas pelo nosso algoritmo e, portanto, não precisamos novamente iniciar um ramo de recursão para elas. 

        Uma sutileza de algoritmos recursivos é que se a casa está marcada por um `x` então ainda podemos não ter visitado todos seus vizinhos, mas com certeza já passamos por ela uma vez e iremos visitar em algum momento futuro.


!!! exercise choice
    No labirinto abaixo, queremos sair da casa `C` e chegar na casa `D`. Toda casa marcada com `.` nunca foi visitada, enquanto toda casa marcada com `x` já foi visitada. 

    ```
    ##########
    #......Cx#
    #..D...xx#
    #......xx#
    #......xx#
    #.....xxx#
    #.xxxxxxx#
    #.xxxxxxx#
    #.xxxxxxx#
    ##########
    ```

    Seriam feitas chamadas recursivas em quais vizinhos neste caso?

    - [x] somente esquerda
    - [ ] cima, direita, baixo e esquerda
    - [ ] somente cima e baixo
    - [ ] nenhuma chamada seria feita

    !!! answer
        Caso análogo ao anterior.




!!! exercise choice
    No labirinto abaixo, queremos sair da casa `C` e chegar na casa `D`. Toda casa marcada com `.` nunca foi visitada, enquanto toda casa marcada com `x` já foi visitada. 

    ```
    ##########
    #......xx#
    #..D...xx#
    #......xx#
    #xx....xx#
    #Cx...xxx#
    #xxxxxxxx#
    #xxxxxxxx#
    #xxxxxxxx#
    ##########
    ```

    Seriam feitas chamadas recursivas em quais vizinhos neste caso?

    - [ ] cima, baixo e direita
    - [ ] cima, direita, baixo e esquerda
    - [ ] somente cima e baixo
    - [x] nenhuma chamada seria feita

    !!! answer
        Se todos os vizinhos já foram visitados então acabamos o trabalho nesta casa! Não fazemos nenhuma chamada recursiva nesse caso. 

!!! progress
    Continuar

Vamos agora definir o critério de parada de nosso algoritmo. 

!!! exercise long
    Estando em uma casa `C`, em quais situações decidimos não fazer mais chamadas recursivas?

    !!! answer
        Já vimos que não fazemos mais chamadas recursivas quando todos os vizinhos já foram visitados. Temos uma condição extra: quando chegamos na casa destino `D`! Isto pode significar tanto que `C == D` quanto que algum outro ramo da recursão já alcançou `D` e não precisamos mais prosseguir.

!!! progress
    Continuar

Com isso já temos um bom guia de como criar uma busca em profundidade recursiva! Já temos 

1. a base da recursão, que são as condições em que paramos de fazer chamadas recursivas
2. as possíveis chamadas recursivas feitas em cada passo do algoritmo

Falta agora completarmos para descobrir como devolver resultados desse procedimento recursivo que estamos montando.Lembrando que o algoritmo criado retorna `VERDADEIRO` se existe caminho entre a fonte e o destino e `FALSO` caso contrário. Se houver caminho, ele é retornado na lista `CAMINHO`. 

!!! exercise long
    A partir do critério de parada que determinamos acima, em quais situações a chamada atual devolveria `VERDADEIRO`? Não se esqueça de considerar as chamadas recursivas em sua resposta.

    !!! answer
        Claramente a função retorna `VERDADEIRO` se chegamos no destino. Revisitando a definição da existência de caminhos, também notamos que essa função retorna `VERDADEIRO` se existe caminho entre algum de seus vizinhos e o destino.

!!! exercise long
    A partir do critério de parada que determinamos acima, em quais situações a chamada atual devolveria `FALSO`? Não se esqueça de considerar as chamadas recursivas em sua resposta.

    !!! answer
        Se não existir caminho entre TODOS os vizinhos que foram expandidos a partir dessa casa (ou seja, só os que não tinham sido visitados quando chegamos na casa atual pela primeira vez) então devemos devolver `FALSO` nesta chamada. 

!!! progress 
    Continuar


Vamos para o exercício final de hoje: escrever a busca em profundidade completa. O algoritmo em si é curto, mas precisamos definir algumas estruturas extras para nos auxiliar.

!!! exercise long
    Escreva abaixo o algoritmo recursivo `DFS`. Você pode usar os seguintes argumentos:

    1. `LABIRINTO L`
    2. `fI, fJ` - posição da fonte
    2. `dI, dJ` - posição do destino
    4. `CAMINHO` - lista para armazenar o caminho encontrado. Inclua a fonte e o destino no caminho
    5.  `VISITADO` - matriz de Posição que indica se um elemento já foi visitado. 

    !!! answer
        Será feito na última aula do módulo na lousa. A ideia é iterar aqui entre algoritmo, simulações e implementação. 


Agora que já estudamos uma versão inicial da busca em profundidade, vá para a tarefa de implementação no PrairieLearn
