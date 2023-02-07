# Algoritmos com dados compostos

Até o momento todos nosso algoritmos usavam dados "simples": cada variável guarda somente um valor. Agora vamos desenvolver algoritmos com dados compostos: cada variável guarda uma coleção de valores. Os tipos compostos mais básicos são o *Array* e *Strings*.

#{% include "content/modulos/00-Algoritmos/java/arrays.md" %}

Vamos agora usar esses novos conceitos em exercícios de Arrays.

### Entregador mais próximo

Para desenvolver um aplicativo de entrega de comida, é útil saber qual entregador está mais próximo do restaurante. Faça uma função que recebe as coordenadas *x, y* de um restaurante, uma lista de coordenadas *x* e uma lista de coordenadas *y* de entregadores. Sua função deve devolver o índice do entregador mais próximo do restaurante.

**Observação 1:** a distância de um ponto $(x_1, y_1)$ a outro ponto $(x_2, y_2)$ é dada por $\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$.

!!! exercise long id_algoritmo_array_entregadores_entrada
    Qual são os dados de entrada? Escreva seus nomes e tipos na ordem que seriam recebidos. 

    !!! answer
        - `FRACIONÁRIOS X e Y` - coordenadas do restaurante
        - `ARRAY de FRACIONÁRIOS XE` - lista de coordenadas x dos entregadores
        - `ARRAY de FRACIONÁRIOS YE` - lista de coordenadas y dos entregadores

        A posição de um entregador `I` é `(XE[i], YE[i])`

!!! exercise long id_algoritmo_array_entregadores_saida
    Qual são os dados de saída? Escreva seus nomes e tipos, indicando se são retorno de função ou `PRINT`.

    !!! answer
        O programa devolve um `INTEIRO` com o índice do entregador mais próximo.

!!! exercise long id_algoritmo_array_entregadores_algoritmo
    Agora escreva abaixo um pseudo-código (no modelo acima) que resolva o exercício acima. Chame seu algoritmo de `ENTREGADOR_MAIS_PROXIMO`. Você pode supor que existe uma função `DIST(X1, Y1, X2, Y2)` que calcula a distância entre dois pontos. 

    !!! answer
        ```
        ENTREGADOR_MAIS_PROXIMO(X, Y, XE, YE)
            MAIS_PROXIMO ← 0
            DIST_MAIS_PROXIMO ← DIST(X, Y, XE[0], YE[0])

            PARA CADA I=1 ATÉ N FAÇA
                DIST ← DIST(X, Y, XE[i], YE[i])
                SE DIST < DIST_MAIS_PROXIMO ENTÃO
                    DIST_MAIS_PROXIMO ← DIST
                    MAIS_PROXIMO ← I
                FIM 
            FIM

            DEVOLVE MAIS_PROXIMO
        ```

!!! exercise self id_algoritmo_array_entregadores_java
    Vamos agora implementar esse algoritmo em Java. Preencha o esqueleto na classe `br.edu.insper.tecprog.aps0.EntregadorMaisProximo`, implemente o algoritmo acima e rode os testes.

    **Lembrete**: você precisará criar a função `DIST` em Java também, já que ela não existe nativamente. Ela não precisa ser necessariamente uma função, mas o cálculo precisa ser feito em algum lugar. 


### Diferença de listas

Faça uma função que recebe 2 listas de inteiros e retorna uma nova lista com os elementos da primeira lista que não estão na segunda lista.

!!! exercise long id_algoritmo_array_diff_listas_entrada
    Qual são os dados de entrada? Escreva seus nomes e tipos na ordem que seriam recebidos. 

    !!! answer
        - `ARRAY de INTEIRO A1`
        - `ARRAY de INTEIRO A2`

!!! exercise long id_algoritmo_array_diff_listas_saida
    Qual são os dados de saída? Escreva seus nomes e tipos, indicando se são retorno de função ou `PRINT`.

    !!! answer
        O programa devolve um `ARRAY de INTEIRO` com os valores que estão na primeira lista e não estão na segunda.

!!! exercise long id_algoritmo_array_diff_listas_algoritmo
    Agora escreva abaixo um pseudo-código (no modelo acima) que resolva o exercício acima. Chame seu algoritmo de `DIFF_LISTAS`. 

    **Dica**: 
    - arrays precisam ser criados com tamanho fixo, mas esse tamanho pode ser definido dentro do programa
    - tente primeiro contar quantos elementos de A1 não estão em A2

    !!! answer
        ```
        DIFF_LISTAS(A1, A2)
            COUNT_DIFF ← 0

            PARA CADA I=0 ATÉ TAMANHO(A1) FAÇA
                ESTA_EM_A2 = Falso
                PARA CADA J=0 ATÉ TAMANHO(A2) FAÇA
                    SE A1[I] = A2[J] ENTÃO
                        ESTA_EM_A2 = Verdadeiro
                    FIM
                FIM
                SE NÃO ESTA_EM_A2 ENTÃO
                    COUNT_DIFF ← COUNT_DIFF + 1
                FIM
            FIM

            ARR_DIFF = NOVO_ARRAY(COUNT_DIFF)
            COUNT ← 0

            PARA CADA I=0 ATÉ TAMANHO(A1) FAÇA
                ESTA_EM_A2 = Falso
                PARA CADA J=0 ATÉ TAMANHO(A2) FAÇA
                    SE A1[I] = A2[J] ENTÃO
                        ESTA_EM_A2 = Verdadeiro
                    FIM
                FIM
                SE NÃO ESTA_EM_A2 ENTÃO
                    ARR_DIFF[COUNT] = A1[I]
                    COUNT ← COUNT + 1
                FIM
            FIM


            DEVOLVE ARR_DIFF
        ```

!!! exercise self id_algoritmo_array_diff_listas_java
    Vamos agora implementar esse algoritmo em Java. Preencha o esqueleto na classe `br.edu.insper.tecprog.aps0.DiffListas`, implemente o algoritmo acima e rode os testes.


### Valor da nota fiscal

Faça uma função que recebe duas listas com informações de uma nota fiscal e devolve o preço total da nota. A nota fiscal é representada pelas duas listas, uma com preços de produtos e outra com a respectiva quantidade de itens comprados daquele produto. Você pode assumir que só é possível comprar quantidades inteiras de um produto. 

!!! exercise long id_algoritmo_array_valor_nota_entrada
    Qual são os dados de entrada? Escreva seus nomes e tipos na ordem que seriam recebidos. 

    !!! answer
        - `ARRAY de FRACIONÁRIO P` - contém os preços unitários de cada produto comprado.
        - `ARRAY de INTEIRO Q` - contém as quantidades de cada produto comprado. 

!!! exercise long id_algoritmo_array_valor_nota_saida
    Qual são os dados de saída? Escreva seus nomes e tipos, indicando se são retorno de função ou `PRINT`.

    !!! answer
        O programa devolve um `FRACIONÁRIO` com o valor final da nota.

!!! exercise long id_algoritmo_array_valor_nota_algoritmo
    Agora escreva abaixo um pseudo-código (no modelo acima) que resolva o exercício acima. Chame seu algoritmo de `VALOR_DA_NOTA`. 

    !!! answer
        ```
        VALOR_DA_NOTA(P, Q)
            VALOR_TOTAL ← 0

            PARA CADA I=0 ATÉ TAMANHO(P) FAÇA
                VALOR_TOTAL ← VALOR_TOTAL + P[I] * Q[I]
            FIM

            DEVOLVE VALOR_TOTAL
        ```

!!! exercise self id_algoritmo_array_valor_nota_java
    Vamos agora implementar esse algoritmo em Java. Preencha o esqueleto na classe `br.edu.insper.tecprog.aps0.ValorDaNota`, implemente o algoritmo acima e rode os testes.


#{% include "content/modulos/00-Algoritmos/java/strings.md" %}

Vamos agora praticar com alguns exercícios. 

### Palavras iguais

De acordo com o Novo Acordo Ortográfico da Língua Portuguesa, usa-se o hífen em compostos que têm palavras iguais ou quase iguais, sem elementos de ligação. Faça uma função que recebe uma string e devolve `#!java true` se ela for composta por duas palavras iguais ou `#!java false`, caso contrário.

Por exemplo, sua função deve devolver `#!java true` para as seguintes entradas: `#!java "pega-pega"`, `#!java "cri-cri"`, `#!java "zum-zum.`

Alguns exemplos para os quais sua função deve devolver `#!java false` são: `#!java "zigue-zague"`, `#!java "pingue-ongue"`, `#!"java "abobrinha"`.


!!! exercise long id_algoritmo_string_palavras_iguais_entrada
    Qual são os dados de entrada? Escreva seus nomes e tipos na ordem que seriam recebidos. 

    !!! answer
        - `STRING S` - palavra a ser processada

!!! exercise long id_algoritmo_string_palavras_iguais_saida
    Qual são os dados de saída? Escreva seus nomes e tipos, indicando se são retorno de função ou `PRINT`.

    !!! answer
        O programa devolve 
        
        - Verdadeiro se a `S` for formada por duas palavras iguais separadas por hífen
        - Falso caso contrário

!!! exercise long id_algoritmo_string_palavras_iguais_algoritmo
    Agora escreva abaixo um pseudo-código (no modelo acima) que resolva o exercício acima. Chame seu algoritmo de `PALAVRAS_IGUAIS`. 

    !!! answer
        ```
        PALAVRAS_IGUAIS(S)
            PARTES ← DIVIDE(S, "-")

            SE TAMANHO(PARTES) != 2 ENTÃO
                DEVOLVA FALSO
            FIM

            DEVOLVE PARTES[0] = PARTES[1]
        ```

!!! exercise self id_algoritmo_string_palavras_iguais_java
    Vamos agora implementar esse algoritmo em Java. Preencha o esqueleto na classe `br.edu.insper.tecprog.aps0.PalavrasIguais`, implemente o algoritmo acima e rode os testes.

### Lista celulares

O departamento de marketing da sua empresa está interessado em obter apenas os números de telefone celular, separando-os dos telefones fixos. Para simplificar esta operação serão considerados números de celular apenas aqueles que, após o código de área, iniciarem com o dígito adicional 9.

Você recebeu a tarefa de obter uma lista com os números de celular, sem o código de área. Entretanto, o cadastro de telefones do departamento de marketing não está padronizado e existem números seguindo 3 formatos distintos:

1. Números completos (13 ou 14 caracteres), incluindo o código do país (+55) e o código de área (ex: 11);
2. Número contendo apenas o código de área (10 ou 11 caracteres);
3. Número sem código de área (8 ou 9 caracteres).

Faça uma função que recebe uma lista de números de telefone e retorna uma lista contendo apenas os telefones celulares. Cada telefone da lista de entrada (recebida como argumento da sua função) pode estar em qualquer um dos 3 formatos acima. Os telefones da lista de saída (retornada pela sua função) devem conter apenas os dígitos do telefone, removendo o código do país e código de área se for necessário.

!!! exercise long id_algoritmo_string_celular_entrada
    Qual são os dados de entrada? Escreva seus nomes e tipos na ordem que seriam recebidos.

    !!! answer
        - `ARRAY de STRING T` - lista de telefones a serem processados

!!! exercise long id_algoritmo_string_celular_saida
    Qual são os dados de saída? Escreva seus nomes e tipos, indicando se são retorno de função ou `PRINT`.

    !!! answer
        O programa devolve um `ARRAY de STRING` contendo somente os números de celular sem código de área.

!!! exercise long id_algoritmo_string_celular_algoritmo
    Agora escreva abaixo um pseudo-código (no modelo acima) que resolva o exercício acima. Chame seu algoritmo de `CELULARES`.

    !!! answer
        ```
        CELULARES(T)
            COUNT_CELULARES ← 0

            PARA CADA ITEM EM T FAÇA
                DIGITO1 ← VAZIO
                SE TAMANHO(ITEM) = 14 ENTÃO
                    DIGITO1 ← ITEM[5]
                    SE DIGITO1 = "9" ENTÃO
                        COUNT_CELULARES ← COUNT_CELULARES + 1
                    FIM
                FIM
                SE TAMANHO(ITEM) = 11 ENTÃO
                    DIGITO1 ← ITEM[2]
                    SE DIGITO1 = "9" ENTÃO
                        COUNT_CELULARES ← COUNT_CELULARES + 1
                    FIM
                FIM

                SE TAMANHO(ITEM) = 9 ENTÃO
                    DIGITO1 ← ITEM[0]
                    SE DIGITO1 = "9" ENTÃO
                        COUNT_CELULARES ← COUNT_CELULARES + 1
                    FIM
                FIM
            FIM

            LISTA_CELULAR ← NOVO_ARRAY(COUNT_CELULARES)
            NUM_CELULARES ← 0
            PARA CADA ITEM EM T FAÇA
                DIGITO1 ← VAZIO
                SE TAMANHO(ITEM) = 14 ENTÃO
                    DIGITO1 ← ITEM[5]
                    SE DIGITO1 = "9" ENTÃO
                        LISTA_CELULAR[NUM_CELULARES] ← SUBSTRING(ITEM, 5)
                        NUM_CELULARES ← NUM_CELULARES + 1
                    FIM
                FIM
                SE TAMANHO(ITEM) = 11 ENTÃO
                    DIGITO1 ← ITEM[2]
                    SE DIGITO1 = "9" ENTÃO
                        LISTA_CELULAR[NUM_CELULARES] ← SUBSTRING(ITEM, 2)
                        NUM_CELULARES ← NUM_CELULARES + 1
                    FIM
                FIM

                SE TAMANHO(ITEM) = 9 ENTÃO
                    DIGITO1 ← ITEM[0]
                    SE DIGITO1 = "9" ENTÃO
                        LISTA_CELULAR[NUM_CELULARES] ← ITEM
                        NUM_CELULARES ← NUM_CELULARES + 1
                    FIM
                FIM
            FIM

            DEVOLVE LISTA_CELULAR
        ```

!!! exercise self id_algoritmo_string_celular_java
    Vamos agora implementar esse algoritmo em Java. Preencha o esqueleto na classe `br.edu.insper.tecprog.aps0.FiltraCelulares`, implemente o algoritmo acima e rode os testes.

## Extras

### Diferença de listas (II)

Nosso algoritmo ficou um bocado grande. Vamos tentar deixá-lo mais fácil de ler. 

!!! exercise long id_algoritmo_array_diff_listas_algoritmo_extra1
    Reescreva o algoritmo da resposta anterior supondo que existe um algoritmo `ARRAY_CONTEM(EL, ARR)` que checa se `ARR` contém o elemento `EL`. 

!!! exercise long id_algoritmo_array_diff_listas_algoritmo_extra2
    Escreva o algoritmo `ARRAY_CONTEM(EL, ARR)` no espaço abaixo. Não se esqueça de especificá-lo completamente incluindo os tipos de entrada e saída.

### Valor da nota fiscal (II)

O programa atual só aceita quantidades inteiras de produtos. 

!!! exercise long id_algoritmo_array_valor_nota_extra
    Qual seriam as modificações necessárias para que sua implementação aceite produtos vendidos por quilo?

### Lista celulares (II)

Nosso algoritmo ficou grande e repetitivo.

!!! exercise long id_algoritmo_string_celular_extra
    Divida o algoritmo acima em funções de modo a diminuir a quantidade de repetição de código.
