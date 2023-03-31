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
