# APS

Neste módulo iremos implementar várias soluções para o problema da mochila binária. Nosso foco é eventualmente encontrar a melhor solução possível.

## Soluções simples

Vimos na primeira aula algoritmos que selecionam primeiro os objetos **mais caros** e os objetos **mais leves**. Iremos implementar ambos nessa seção. Você deverá editar os arquivos correspondentes no pacote `br.edu.insper.tecprog.aps06` e usar os testes para validar suas soluções.


!!! tip
    Você pode usar os métodos da classe [`Arrays`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Arrays.html) para facilitar sua vida. Em especial, busque como realizar **ordenação indireta** usando este módulo. 


## Solução ótima

Agora vamos implementar a solução ótima descrita em aula. Edite o arquivo correspondente no pacote `br.edu.insper.tecprog.aps06` e usar os testes para validar suas soluções.

## Branch and Bound

Os testes finais deste módulo estão nos arquivos `TestGrandeSemBound`, `TestGrandePeso` e `TestGrandeFracionaria`. O primeiro usa a mochila binária simples e servirá para ver o tamanho dos ganhos de cada bound.

Todos os testes devem passar para este item ser válido e devem respeitar os tempos limites de cada bound. As diferenças deverão ser significativas, com o bound usando a Mochila Fracionária tendo os melhores tempos. 
