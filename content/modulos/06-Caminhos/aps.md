# APS

Neste módulo iremos implementar vários algoritmos para encontrar a saída de um labirinto. Em cada aula examinaremos um novo algoritmo. 

## Implementando a ADT `LABIRINTO`

Examine os arquivos `br.edu.insper.tecprog.aps05.Labirinto.java` e `br.edu.insper.tecprog.aps05.Posicao.java`. Implemente os métodos faltantes e verifique o funcionamento correto usandos os testes de unidade.

## Seguir Paredes

Implemente o algoritmo de seguir paredes no arquivo `br.edu.insper.tecprog.aps05.Paredes.java`. Utilize os testes para verificar o funcionamento do algoritmo.

!!! important
    Não se esqueça de olhar os labirintos dos testes e simular seu programa com eles. Alguns podem apresentar situações que não estão nos handouts.

## Busca em Profundidade

Agora vamos implementar a busca em profundidade clássica, que visa encontrar um caminho entre duas casas no labirinto. Por enquanto não estamos procurando a saída do labirinto (ainda). Para isso será necessário modificar `br.edu.insper.tecprog.aps05.DFS`. Os testes disponíveis não são detalhados, então não se esqueça de simular sua implementação usando os exemplos do handout. 

Com a DFS encontrando caminhos, vamos então adaptá-la para encontrar a saída do Labirinto! Preenche o arquivo `br.edu.insper.tecprog.aps05.DFSSaida.java` e rode os testes. As modificações para encontrar a saída a partir da DFS "clássica" de encontrar caminhos são pequenas, porém representam bem o tipo de entendimento que queremos ter desses algoritmos clássicos. 