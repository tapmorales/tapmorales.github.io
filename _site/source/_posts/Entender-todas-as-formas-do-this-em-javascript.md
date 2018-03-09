---
title: Entender todas as formas do this em javascript
date: 2018-03-07 11:40:25
tags:
- javascript
---
Quando estamos aprendendo Javascript uma das coisas mais complicadas para entender (pelo menos foi para mim) é a natureza dinâmica do escopo do "this".

Eu sempre ficava na dúvida se aquele this que eu estava escrevendo no código representava o que eu queria que representasse. E isso me fez escrever muitos consoles.log() e colocar vários breakpoints no meu código que hoje se tornaram desnecessários na maior parte das vezes.

O meu intuito com este artigo é elucidar as várias formas que o this se apresenta e mostrar alguns padrões de escrita no código que refletem diretamente no valor que será armazenado em this. 

Antes de responder o que o "this" está referenciando, precisamos responder várias questões previamente, a saber:

<ul>
	<li>Estamos no escopo global?</li>
	<li>Há presença da diretiva "use strict"?</li>
	<li>Como a função foi executada? Normal? Com call() ou apply()?</li>
	<li>Quando a função foi implementada, foi usado o bind()?</li>
	<li>A função está atrelada a algum evento?</li>
	<li>A função é literal ou arrow function?</li>
	<li>A função está dentro de um objeto literal?</li>
	<li>A função está dentro de um objeto criado a partir de uma função construtora ou classe?</li>
</ul>

Note que os itens acima não são excludentes, ou seja, o fato de responder positivamente para uma das perguntas não significa que não pode ser intercambiada com outra resposta positiva, como por exemplo, escrevi "this" dentro de uma função construtora que foi criada dentro de uma IIFE contendo a diretiva "use strict".

E ai? Estamos prontos para entender que raios este "this" representa? Então vamos começar.

## This no escopo global
O lugar mais fácil para entender o this é estando no escopo global ou ainda dentro de uma IIFE que foi executada pelo - advinha - escopo global. Nesses casos, o "this" representa o próprio escopo global que, no caso do javascript estar sendo interpretado por um browser, é o objeto window. Já se você estiver desenvolvendo para para o node o objeto "pai de todos" chama-se global. 

{% codeblock lang:js %}
console.log(this); //window

(function(){
  console.log(this); //window
})();
{% endcodeblock %}

Obs 1: Ao longo deste artigo vou me referir várias vezes ao objeto global, mas enteda que este é o objeto acima de todos que, no caso do browser é o window e no caso do node chama-se simplesmente global. Não confunda "objeto global" com o "global" do node, ok?
Obs 2: Vou supor que você está testando os códigos no console do browser, portanto, o seu objeto global é o window.

O objeto global é onde ficam todas as variáveis e funções que são acessíveis por toda a aplicação. É por isso que alert('uma coisa') ou window.alert('outra coisa') são comandos válidos. Uma observação importante: as variáveis que ficam no objeto global são aquelas definidas com a palavra <code>var</code>. O mesmo não vale para <code>let</code> e <code> const</code>. Obrigado <a href="https://medium.com/@felquis/javascript-o-global-object-e-o-this-ceda36059cff">@felquis</a>


Até aqui creio que não haja nenhuma novidade. A grande questão é quando usamos a diretiva <code>"use strict"</code> dentro de uma função, pois isso muda completamente o que o "this" representa:

{% codeblock lang:js %}console.log(this); //window

(function(){
  "use strict";
  console.log(this); //undefined
})();
{% endcodeblock %}

A diretiva "use strict" foi acrescentada na javascript para resolver algumas falhas da linguagem. Mais a frente veremos onde a sua ausência pode gerar problemas, mas por hora, vamos entender que dentro de uma função, seja auto-invocável ou não, a presença do "use strict" faz com que o "this" assuma o valor <code>undefined</code>.

Um outro ponto que temos que prestar atenção é a partir de quem foi executada determinada função. Veja mais um exemplo:

{% codeblock lang:js %}var obj = {
  minhaFunc: function(){
    console.log(this);
  }
}

function minhaFunc(){
  console.log(this);
}

obj.minhaFunc(); //obj

minhaFunc(); //window

{% endcodeblock %}

Repare que está claro quando olhamos para a implementação da função quem é o this. Então vamos obscurecer um pouco as coisas.

Atenção: O motivo de eu estar utilizando o "var" e não o "let" para criar algumas variáveis é que se você copiar e colar o código no console para testar, você não conseguirá criar duas variáveis com mesmo nome se usar o "let". Utilizando o "var" pode copiar e colar a vontade para testar a saída no console.

Voltando ao código: 
{% codeblock lang:js %}
var obj = {
  minhaFunc2: minhaFunc
}

function minhaFunc(){
  console.log(this);
}

obj.minhaFunc2(); //obj

minhaFunc(); //window
{% endcodeblock %}

Repare que agora atrelamos a <b>mesma</b> função <code>minhaFunc()</code> como método do objeto, ou seja, temos agora <b>uma única função</b> e  portando, apenas um <code>console.log(this)</code>. Mas isso não impede que a natureza dinâmica do this venha brilhar aos nossos olhos. A lição aprendida aqui é que não importa COMO você escreveu a função literal. O que importa é QUEM chamou esta função. Isso porque o escopo de funções literais é dinâmico. O mesmo "this" pode representar o window ou qualquer outro objeto, tudo depende de quem executou a função.

## Mas dá pra mudar o this?

Funções são objetos com a incrível capacidade de serem executados. A forma mais comum de executar uma função é esta que acabou de passar pela sua cabeça:

{% codeblock lang:js %}
minhaFunc();
{% endcodeblock %}

Só isso. Basta abrir e fechar parenteses que a mágica acontece.

Mas não existe só uma maneira de executarmos uma função. Também podemos fazer assim:

{% codeblock lang:js %}minhaFunc.call(this) 

minhaFunc.apply(this)
{% endcodeblock %}

Já vamos ver a diferença entre eles. Por hora, entenda qualquer um dos dois como uma maneira de executar uma função informando programaticamente quem deve ser o "this". Veja:

{% codeblock lang:js %}minhaFunc(); //window
minhaFunc.call(obj); //obj
minhaFunc.apply(obj); //obj
{% endcodeblock %}

Ou seja, eu consigo passar por parâmetro quem deve ser o this dentro da função. Nesse momento você pode estar se perguntando: Mas e se <code>minhaFunc()</code> espera receber parâmetros? E é aí que reside a diferença entre o call() e o apply(). Este recebe como segundo parâmetro um array de argumentos. Aquele recebe os demais argumentos logo depois do this. É mais fácil ver com um exemplo:

{% codeblock lang:js %}//executa a função minhaFunc mudando o escopo do this e passando por parâmetro três valores: true, "ola mundo", 10
minhaFunc(obj, true, "ola mundo", 10);

//executa a função minhaFunc mudando o escopo do this e passando por parâmetro três valores: true, "ola mundo", 10, mas desta vez dentro de um array
minhaFunc(obj, [true, "ola mundo", 10]);
{% endcodeblock %}

Tanto call() quanto apply() são primos muito próximos. A única diferença é COMO passar os argumento para a função sendo executada.

Se você reparar bem nos exemplos acima, o responsável por informar quem deve ser o "this" é quem está executando a função. Mas também é possível alterarmos o "this" no momento da implementação da função. Veja mais este exemplo:

{% codeblock lang:js %}function minhaFunc(){
  console.log(this);
}

var minhaFuncComBind = minhaFunc.bind(obj);

minhaFuncComBind(); //obj
{% endcodeblock %}

Repare que exceto pelo nome da função que possui a palavra Bind por motivos didáticos, quem utiliza a função não tem como saber qual será o contexto do this. Veja um exemplo mais obscuro:

{% codeblock lang:js %}function minhaFunc(){
  console.log(this);
}

var minhaFunc2 = minhaFunc.bind(obj);

minhaFunc2(); //obj
{% endcodeblock %}

Perceba que o <code>bind()</code> muda o contexto do this na implementação da função (tomando emprestado outra função: minhaFunc), mas essa implementação pode ficar escondida de quem está usando a função.

Um uso muito comum para o bind() é nos ouvistes de eventos. Veja:

{% codeblock lang:js %}function minhaFunc(){
  console.log(this);
}

$elemento.addEventListener("click", minhaFunc);
{% endcodeblock %}

No exemplo acima o this por padrão é o dono do evento, ou seja, o elemento o qual foi atrelado o evento. Faça um teste e veja que ao clicar no elemento este é mostrado no console. Para testar rapidamente, escreva no console: 

{% codeblock lang:js %}document.addEventListener("click", minhaFunc);{% endcodeblock %}

Entretanto, o que será mostrado no console se alterarmos ligeiramente nosso código inserindo o bind na jogada?

{% codeblock lang:js %}function minhaFunc(){
  console.log(this);
}

$elemento.addEventListener("click", minhaFunc.bind(obj));
{% endcodeblock %}

Agora o próprio objeto é mostrado no console (ou qualquer outro elemento que tiver sido passado por parâmentro para o bind, até mesmo uma string funcionaria, mesmo que seja um exemplo com pouquíssima aplicação prática).

Pensando um pouco mais em tudo que vimos até agora, o que será mostrado no console no exemplo abaixo

{% codeblock lang:js %}function minhaFunc(){
  console.log(this);
}

$elemento.addEventListener("click", minhaFunc.bind(this));
{% endcodeblock %}

Perceba que o this do exemplo acima que foi passado por parâmetro no bind() está fora da função atrelada, portanto, esse this, que é dinâmico, pode representar o window (se no escopo global, sem a diretiva "use strict" ou undefined se no escopo global com a diretiva "use strict").

Mas será que existe alguma maneira de mudarmos o escopo dinâmico do "this"? em outras palavras, podemos impedir que o this sofra variações dependendo do contexto em que foi executado?

## O escopo léxico das arrows functions

No EcmaScript2015 (antigamente chamado de ES6) foi introduzido o conceito de Arrow function. A princípio pode parecer somente uma maneira mais enxuta de escrever funções (e é mesmo), mas também é uma maneira de deixarmos o this com escopo léxico, ou seja, não mais dinâmico como acontece com as nossas funções literais.

Vamos ao código:
{% codeblock lang:js %}function minhaFunc(){
  console.log(this);
}

$elemento.addEventListener("click", function(){
  console.log(this); //mostrará $elemento
})

$elemento.addEventListener("click",() =>{
  console.log(this); //mostrará window
});
{% endcodeblock %}

Ou seja, ao criar suas arrows functions o this será representado pelo valor que ele tinha no momento da implementação da função (escopo léxico) e não mais no momento da invocação (escopo dinâmico).

Isso significa que você não deve usar as arrow functions só pra se sentir mais moderno. Use-as sabendo desse efeito. 

Se você precisar que dentro de funcões atreladas a eventos o "this" seja o próprio elemento que disparou tal evento, você deverá usar as boas e velhas funções literais.

Contudo, quero mostrar dois exemplos em que arrow functions são especialmente úteis:

{% codeblock lang:js %}let obj = {
  arr: [1,2,3],
  count: 0
}

obj.foo = function(){
  this.arr.forEach( (item) => {this.count++; console.log( this); } );
}

obj.foo() // mostra o obj tres vezes. com seus valores de count atualizados.
{% endcodeblock %}

Isso significa que o this dentro de uma arrow function pode ser acessado mesmo dentro de um forEach. Se você usasse uma literal, veria que o this iria representar o window, e não mais o objeto o qual foi definida a função

{% codeblock lang:js %}let obj = {
  arr: [1,2,3],
  count: 0
}

obj.foo = function(){
  this.arr.forEach( function(){
    console.log(this); //window
  });
}
{% endcodeblock %}


Se não fosse pelas arrow functions você teria que criar uma variavel adicional (normalmente _self ou _this) e acessá-la dentro do clousure, mas isso é outra historia.

Para encerrar, vou explicar o que acontece quando usamos o this dentro de uma função que foi invocada com o operador new, aka, função construtora ou classe. Veja o código

{% codeblock lang:js %}function MeuConstruct(){
    this.ts = +new Date(),
    this.foo = "bar",
    this.mostraThis = function(){
        console.log(this)
    }
}

class MeuConstructNovo {
    constructor(){
        this.ts = +new Date();
        this.foo = "bar";
        this.mostraThis = function(){
            console.log(this)
        }
    }
}

let obj1 = new MeuConstruct();
obj1.mostraThis() // Objeto do tipo MeuConstruct.

let obj2 = new MeuConstructNovo();
obj2.mostraThis() // Objeto do tipo MeuConstruct.
{% endcodeblock %}

No exemplo acima, ao criarmos um objeto novo com o operador new, o javascript criou um objeto vazio e atribuiu as propriedades e métodos à esse objeto recém-criado através da palavra this, ou seja, este this aponta para o objeto criado.

Um fato curioso é que, se alguém atribuir a uma variável qualquer a função MeuConstruct SEM utilizar o operador new, o this de dentro da função irá representar o objeto window, o que pode gerar uma série de problemas imprevisíveis. Para impedir que isso aconteça temos que usar a diretiva "use strict".

{% codeblock lang:js %}function MeuConstruct(){
    "use strict";
    this.ts = +new Date(),
    this.foo = "bar",
    this.mostraThis = function(){
        console.log(this)
    }
}

let obj1 = new MeuConstruct(); // funfa e o this aponta para o objeto obj1

let obj2 = MeuConstruct(); // dispara um erro no console porque o this é undefined
{% endcodeblock %}
O mesmo não acontece se você utilizar a palavra reservada class para criar suas classes. Se você tentar atribuir uma classe a uma variável sem utilizar o operador new um erro será apresentado no console. 

Espero ter sanado possíveis dúvidas quanto ao que representa o this dentro das mais diversas situações. Fique a vontade para dar sua opinião e me avise se eu escrevi alguma besteira.

Aproveito para fazer o meu jabá e dizer que o meu curso de <a href="https://www.udemy.com/javascript-completo-2018-do-iniciante-ao-mestre/?couponCode=PROMOSITE20">Javascript Completo</a> tem um desconto bacanão se você utilizar o cupom <a href="https://www.udemy.com/javascript-completo-2018-do-iniciante-ao-mestre/?couponCode=PROMOSITE20">PROMOSITE20</a>. 

Um abraço

