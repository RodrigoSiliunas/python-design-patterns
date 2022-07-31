## Singleton

Singleton é um (anti-)padrão de projeto de software (do inglês Design Pattern). Este padrão garante a existência de apenas uma instância de uma classe, mantendo um ponto global de acesso ao seu objeto.

Nota linguística: O termo vem do significado em inglês para um conjunto (entidade matemática) que contenha apenas um elemento.

Alguns projetos necessitam que algumas classes tenham apenas uma instância. Por exemplo, em uma aplicação que precisa de uma infraestrutura de log de dados, pode-se implementar uma classe no padrão singleton. Desta forma existe apenas um objeto responsável pelo log em toda a aplicação que é acessível unicamente através da classe singleton.

### Onde Usar

Quando você necessita de somente uma instância da classe, por exemplo, a conexão com banco de dados, vamos supor que você terá que chamar diversas vezes a conexão com o banco de dados em um código na mesma execução, se você instanciar toda vez a classe de banco, haverá grande perda de desempenho, assim usando o padrão singleton, é garantida que nesta execução será instânciada a classe somente uma vez. Lembrando que este pattern é considerado por muitos desenvolvedores um antipattern, então, cuidado onde for utilizá-lo.

### Como fazer a implementação do Singleton

> 1. Deixar o construtor privado, pois assim ninguém deve conseguir instanciar a classe, apenas o próprio Singleton.
> 2. Criar um atributo privado e estático do mesmo tipo da classe (instance). Algumas linguagens não tipadas não irão precisar do tipo, caso do PHP, por exemplo.
> 3. Método getInstance() é o principal ponto da classe. Ele verifica se a variável instance já foi iniciada, caso não tenha sido, ele faz sua criação pela primeira e única vez.
> 4. Para fazer a conexão, devemos chamar o getInstance da seguinte forma: ClasseSingleton.getInstance().

_Fonte_: _(Wikipedia)[https://pt.wikipedia.org/wiki/Singleton]_