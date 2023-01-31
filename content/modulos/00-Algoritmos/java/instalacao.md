# Instalação (Java)

A instalação de Java não é muito diferente do que vocês já fizeram com Python. Nessa disciplina vocês podem usar as ferramentas que quiserem para desenvolver. Este guia aponta direções para um setup básico que funcione em qualquer sistema.

## Ferramentas básicas

Vamos precisar de um kit de desenvolvimento de Java para começar. Instale os seguintes softwares.

- Windows e macOS:
    1. [Eclipse adoptium](https://adoptium.net/) - usar Latest Release (jdk-17)
    2. [Maven](https://maven.apache.org/install.html) - seguir instruções e confirmar que tanto `%JAVA_HOME%` quanto `%PATH%` estão corretos.
- Linux: instalar via gerenciador de pacotes. No Ubuntu os pacotes necessários são `openjdk-17-jdk maven`.

Teste se tudo está correto abrindo um terminal e rodando os dois comandos abaixo.

```
java --version
mvn -v
```

### Hello Java!

Salve o conteúdo abaixo em um arquivo `HelloJava.java`. Para executá-lo rode `java HelloJava.java` e veja se a mensagem aparece.

```java

public class HelloJava {
    public static void main (String args[]) {
        System.out.println("Hello Java :)");
    }
}
```

## IDEs e Editores de Texto

Qualquer ferramenta com suporte a projetos Maven vai ser suficiente nesta disciplina. Seguem algumas sugestões.

!!! important
    Não daremos suporte específico a configuração das ferramentas abaixo. Claro que tentaremos ajudar no setup, mas isso não fará parte das atividades de aula.

- [VSCode](https://code.visualstudio.com/docs/languages/java) - se já seguiu o guia acima, usar o pacote de extensões recomendadas
- [Eclipse](https://www.eclipse.org/downloads/) - muito tradicional e conhecida no mercado
- [IntelliJ Idea](https://www.jetbrains.com/idea/download) - a versão Free/Community é suficiente para esta disciplina

Cada editor tem sua configuração específica, mas para facilitar estamos usando um gerenciador de compilação e projeto (Maven) muito popular e com excelente suporte de ferramentas.


