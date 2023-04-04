# APS

Nesta APS iremos trabalhar com algoritmos simples para processamento de textos e buscas em textos. 

## Algoritmos simples em Strings

Iniciaremos esse módulo (re)implementando algoritmos simples para processar textos.

- sufixo
- prefixo
- indexOf - encontra o primeiro índice em uma string aparece em outra. Se não encontrar retorna -1
- lastIndexOf - igual o acima, mas encontra a última ocorrência
- replace - devolve uma cópia da string recebida substituindo a primeira ocorrência do termo pelo valor passado.
- replace - igual acima, mas substitui todas ocorrências

!!! warning
    Esses algoritmos são muito clássicos e podem ser tanto encontrados na internet quanto completados por ferramentas como *chatGPT* e *Github Copilot*. A ideia dessa APS é **não usar essas ferramentas**, já que estamos reimplementando essas coisas de propósito para aprender a trabalhar com strings. 

Implemente essas funções na classe `br.edu.insper.tecprog.aps04.StringUtils`. Em todas as funções você não pode usar os métodos da classe `String`, tendo em todos os casos que passar caractere a caractere nas strings usando um (ou mais)  `for`

## Buscando por padrões simples

Somente buscar termos em uma string pode não ser exatamente útil assim. Vamos agora criar pequenos programas que buscam por padrões em texto. Os seguintes programas devem ser feitos

- sumário - encontra todos os cabeçalhos de nível 1 em arquivos Markdown e retorna uma lista deles
- tiraTags - recebe uma string com código HTML e devolve somente o texto, sem tags HTML
- emailsInsper - recebe uma string e devolve uma lista com todos emails Insper dentro dessa string.
    - **Dica**: comece procurando por um caractere '@' e depois olhe para os lados esquerdo e direito desse caractere.


Assim como no item anterior, faremos todos os esses códigos processando a string caractere por caractere. **Não é permitido usar as funções de `String`**. Nestes exercícios também não devemos usar expressões regulares. Você pode, porém, usar suas implementações da classe `StringUtils` do exercício anterior.

## Expressões regulares (extra)

Fizemos os códigos acima usando algoritmos muito específicos para cada padrão buscado. Apesar disso ser interessante como exercício de algoritmos não é algo que gostaríamos de usar em softwares "de verdade". Uma maneira mais adequada de processar textos e encontrar correspondências com padrões é usar uma *Expressão Regular*. 

Uma *Expressão Regular* define um padrão a ser buscado em um texto usando caracteres especiais que representam grupos de caracteres. Por exemplo, a expressão "\d\d" buscará por todas ocorrências de dois dígitos um depois do outro. 

!!! tip
    [Esta tabela](https://docs.oracle.com/javase/tutorial/essential/regex/pre_char_classes.html#CHART) contém diversas classes de caracteres que podemos usar em expressões regulares. 

A tarefa neste item da APS será:

1. Ler o guia da Oracle sobre [expressões regulares em Java](https://www.oracle.com/technical-resources/articles/java/regex.html)
2. Usar o [regex101](https://regex101.com/) para testar algumas expressões usando as strings de teste dos exercícios da seção acima
3. Preencher `StringUtilsRE` com código para encontrar os padrões usando expressões regulares. Testes extras para essas funções estão disponíveis no arquivo de testes correspondente. 


