# APS

Teremos dois tipos de tarefas esta semana:

- **implementações diretas**: são exercícios que trabalham diretamente com os algoritmos vistos nas expositivas e trabalhados nos handouts
- **problemas**: exercícios estilo maratona de programação que usam as ideias trabalhadas no módulo. É preciso "encontrar" como o tópico atual é usado e geralmente é necessário modificar um pouco o algoritmo visto em aula. 

| Nota | Nível                          |
| ---- | ------------------------------ |
| 50%  | Implementação direta           |
| 70%  | Problemas (sem testes grandes) |
| 100% | Problemas (com testes grandes) |


## Implementação direta

No nível básico iremos implementar vários algoritmos de ordenação em Arrays. Todos algoritmos serão testados com os mesmos arrays, então o desafio será realizar corretamente a implementação Java. Você deve preencher as 4 classes correspondentes aos algoritmos vistos em sala (bubble sort, selection sort, quick sort e merge sort) e testá-las usando os arquivos de teste correspondentes. 

## Problemas

!!! exercise 
    **Enunciado**: Given alphabet A and a list of words, sort the list according to the lexicographic order induced by A. Alphabet A consists of lowercase letters arbitrary chosen from the Latin alphabet. 

    **Exemplos**:

    ```
    # Entrada
    A = re
    words = ["ere", "rer", "re"]
    # Saída
    words = ["re", "rer", "ere"]

    # Entrada
    A = balujemy    
    words = ["bel", "luba", "lej", "bal", "leje"]
    # Saída
    words = ["bal", "bel", "luba", "lej", "leje"]
    ```

    -----

    Seu trabalho será fazer uma função `void sortByA(String A, String[] words)` que ordena a lista `words` de acordo com o alfabeto `A`. Este problema tem dois arquivos de testes: `SLEXSORT_small` e `SLEXSORT_large`. 
    
    Baseado em [SLEXSORT](https://www.spoj.com/problems/SLEXSORT/)