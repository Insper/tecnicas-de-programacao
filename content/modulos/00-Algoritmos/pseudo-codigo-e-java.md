# Primeiros algoritmos

Neste roteiro iremos criar nossos primeiros algoritmos em Pseudo-Código e explorar sua "tradução" para Java. Conforme o roteiro avança haverá leituras (curtas) recomendadas sobre sintaxe e semântica de Java.

!!! warning
    São requisitos para esta aula ser capaz de rodar códigos em Java. Os seguintes roteiros já devem estar cumpridos

    - [Instalação](java/instalacao.md)
    - [Primeiro contato](java/primeiro-contato.md)

    Além disso, iremos criar vários programas simples em Java neste roteiro. Crie uma pasta *aulas1e2* e use-a para todos os programas deste roteiro.

Agora que já temos um primeiro contato com Java, iremos escrever

## O esqueleto de um algoritmo

Todo algoritmo é formado pelo seguinte "esqueleto":

--------

* **Entrada**:
    - lista de parâmetros do algoritmo, incluindo tipos
    - incluir também leitura de dados usando `LER_<TIPO>`.
    - Inteiro `I` (parâmetro)
    - String `S1` (parâmetro)
* **Saída**:
    - resumo da saída do algoritmo, incluindo possíveis `PRINT`
    - pode conter mais de um item se ajudar a entender saídas que são condicionais
    - devolve X caso A
    - devolve Y caso contrário

```
NOME_DO_ALGORITMO(I, S1)

# Atribuições e operações matemáticas
MAIS_UM = I + 1

# Saída de texto
PRINT(MAIS_UM)

# Entrada de dados
NOVO_INT = LER_INTEIRO()
NOVO_FLOAT = LER_FRACIONARIO()
NOVO_TEXTO = LER_TEXTO()
```

--------

Vamos aplicar esse formato para dois problemas simples e já implementá-los em Java.

!!! exercise long id_algoritmo_bobo1
    sdklfjsdl

!!! exercise self id_algoritmo_bobo1_java
    Crie um arquivo Java novo seguindo o [esqueleto Java](java/primeiros-passos.md) e implemente o algoritmo acima no `main`.

    !!! answer
        Verifique se seu programa funciona usando as mesmas entradas/saídas do exercício anterior. Lembre-se de testá-lo usando as intruções do [guia de Instalação](java/instalacao.md).


!!! progress
    Continuar



!!! exercise long id_algoritmo_bobo2
    sdklfjsdl


!!! progress
    Continuar

Agora que temos dois algoritmos simples para trabalhar, vamos transformá-los em programas *Java* completos.



## Condicionais


## Loops


##



## Texto



## Arrays



