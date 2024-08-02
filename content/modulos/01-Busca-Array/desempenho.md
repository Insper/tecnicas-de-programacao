# 03 - Comparando desempenho de algoritmos

<center>
<embed width="500" height="400" src="../slides-desempenho.html"></embed>
</center>

## Parte 0 - anotando os algoritmos 

!!! exercise long
    Anote abaixo o algoritmo da `BUSCA_SEQUENCIAL` desenvolvido na lousa

!!! exercise long
    Anote abaixo o algoritmo da `BUSCA_BINARIA` desenvolvido na lousa

## Parte 1 - comparando as buscas

Como visto na aula, usamos limites para descobrir se o número de operações de um algoritmo cresce mais rapidamente que outro. Isto ocorre se

$$
\lim_{n\rightarrow +\infty} \frac{f(n)}{g(n)} = +\infty
$$

!!! exercise long
    Encontre uma entrada de tamanho `10` que faça os algoritmos acima fazerem o máximo de operações possível (ou seja, rodarem o **pior caso**)

    !!! answer
        Em questões desse tipo é importante dar um exemplo concreto. Por exemplo

        - `ARR := [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]`
        - `VALOR := 10`        

        De maneira mais geral, qualquer`ARR` com tamanho 5 e ordenado funciona. Basta atribuir a `VALOR`  um número maior que o último elemento de `ARR`.

Agora vamos tentar contar o número de operações que são feitas para esses algoritmos.

!!! exercise long
    Anote abaixo o número de operações feitas para a entrada acima.


!!! exercise long
    Generalize esse resultado para depender do tamanho $N$ de `ARR`.

    !!! answer
        A busca sequencial faz $N$ operações.

        A busca binária faz $\log_2 N$ operações.
        

Agora finalmente vamos calcular o limite. 

!!! exercise long
    Calcule o limite $\lim_{n\rightarrow +\infty} \frac{n}{\log_2(n)}$. 

    **Dica**: use a [Regra de L'Hôpital](https://en.wikipedia.org/wiki/L%27H%C3%B4pital%27s_rule).

    !!! answer
        Na lousa ;)

## Parte 2 - mais prática

Vamos agora comparar os dois algoritmos acima com o seguinte algoritmo. O array `ARR` está ordenado já.

```
BUSCA_PULA2(ARR, VALOR)

I := 0
N := TAMANHO(A)

ENQUANTO I < N FAÇA
  SE A[I] = VALOR ENTÃO 
    DEVOLVA VERDADEIRO
  FIM

  SE I > 0 E A[I] > VALOR ENTÃO
    DEVOLVA A[I-1] = VALOR
  FIM   

  N := N + 2
FIM

DEVOLVA N > 0 E A[N-1] = VALOR
# CASO N SEJA ÍMPAR
```


!!! exercise long
    Qual seria uma entrada de tamanho $N=5$ para o algoritmo acima que resulta em seu pior caso? Escreva os valores de `ARR` e `VALOR`

    !!! answer
        Em questões desse tipo é importante dar um exemplo concreto. Por exemplo

        - `ARR := [1, 2, 3, 4, 5]`
        - `VALOR := 10`        

        De maneira mais geral, qualquer`ARR` com tamanho 5 e ordenado funciona. Basta atribuir a `VALOR`  um número maior que o último elemento de `ARR`.

!!! exercise long
    Seja $N$ o tamanho de `ARR`, qual é o número de operações feitas no pior caso?

    !!! answer
        São 3 comparações dentro do loop, que pode rodar no máximo $\frac{N}{2}$vezes e uma atribuição. Temos ainda 2 operações na última linha. O total fica então $4 \frac{N}{2} + 2 = 2N+2 = 2(N+1)$

!!! exercise long
    Compare `BUSCA_PULA2` com a `BUSCA_SEQUENCIAL` usando as definições de limite vistas na sala. 

    !!! answer  
        Ambos são equivalentes, diferindo somente por fatores constantes.

!!! exercise long
     Compare `BUSCA_PULA2` com a `BUSCA_BINARIA` usando as definições de limite vistas na sala. 

    !!! answer  
        Assim como a `BUSCA_SEQUENCIAL`, a `BUSCA_PULA2` cresce mais rápido que a `BUSCA_BINARIA`
    
!!! done "Finalizando"
    Esse exercício tem uma conclusão importante: **a contagem de operações não precisa ser incrivelmente precisa**. Ao fazer a divisão e usar L'Hôpital pequenas diferenças são ignoradas, fazendo com que só levemos em conta partes que dependem do tamanho $N$ da entrada.
    
