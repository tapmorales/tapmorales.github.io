---
title: O que é uma função auto-invocável (IIFE)?
date: 2018-05-10 21:30:25
description: IIFE, ou Immediately-Invoked Function Expression, para que serve e quando devemos usá-la.
tags:
- javascript
---

Para entendermos o que é uma Expressão de função auto-invocável precisamos entender primeiro o que é uma expressão de função, também conhecida como function expression.

No javascript, uma function expression é escrita da seguinte forma:
{% codeblock lang:js %}
function myFunc(){ //mágica aqui };
{% endcodeblock %}

Sem novidades. Após criarmos a função, ela estará disponível no escopo que foi criada.

Vamos imaginar que temos um código javascript em nossa página que é responsável pelo menu. 

Como sabemos, poluir o escopo global é uma má prática pois podemos gerar colisões de nomes de funções e variáveis, o que poderia ser catastrófico para a nossa página ou aplicação. Para resolver isso, vou criar todo o meu código dentro de uma função e depois executá-la.

{% codeblock lang:js %}
menu.js
function init(){
  //variáveis locais
  //funções locais
  //não poluem o escopo global
}
init();
{% endcodeblock %}

Perfeito! dessa forma, a única função que vazou para o escopo global foi a init().

Agora vamos criar o javascript que irá gerenciar a validação de nosso formulário:

{% codeblock lang:js %}
form.js
function init(){
  //variáveis locais
  //funções locais
  //não poluem o escopo global
}
init();
{% endcodeblock %}

E nosso html importamos os dois javascripts.

{% codeblock lang:html %}
<script src="menu.js"></script>
<script src="form.js"></script>
{% endcodeblock %}

Percebeu o problema? Os dois arquivos possuem funções de mesmo nome que estão no escopo global e grandes problemas vão acontecer. Lembre-se: além de seus próprios códigos talvez você queira utilizar alguma biblioteca como o jquery, lodash ou momentjs. Já pensou se essas libs poluíssem o escopo global com funções de mesmo nome?

Para resolver, precisamos de alguma maneira criar um escopo local em cada um dos arquivos, sem mesmo vazar essa função init(). É aí que a mágica das IIFEs acontecem. (Também poderíamos usar ES Modules ou Webpack, mas isso é outra história).

Para que possamos criar uma função e já invocá-la ao mesmo tempo, vamos primeiro inserir essa função dentro de parênteses.

{% codeblock lang:js %}
( function (){ //mágica aqui  } )
{% endcodeblock %}

E em seguida executá-la

{% codeblock lang:js %}
( function (){ //mágica aqui  } )()
{% endcodeblock %}

Logo:

{% codeblock lang:js %}
menu.js
(function(){
  //variáveis locais
  //funções locais
  //não poluem o escopo global
})();

form.js
(function(){
  //variáveis locais
  //funções locais
  //não poluem o escopo global
})();
{% endcodeblock %}

Pronto, resolvemos o problema de colisão de nomes das funções init().

## Conclusão

Para terminar gostaria de ressaltar que as funções auto-invocáveis eram a única forma de modularizarmos nosso site ou aplicação em arquivos javascript menores, visando facilitar a manutenção desses códigos. Entretanto, com a chegada do ES Modules da ES6 isso não é tão verdade assim. O problema é que essa abordagem [ainda não tem um bom suporte](https://caniuse.com/#search=modules), e se você acha que utilizar uma biblioteca como webpack ou parcel é matar uma mosca com uma bala de canhão, pode sim continuar a fazer uso das IIFEs sem medo. 

Aproveito para fazer o meu jabá e dizer que o meu curso de <a href="https://www.udemy.com/javascript-completo-2018-do-iniciante-ao-mestre/?couponCode=PROSITE23">Javascript Completo</a> tem um desconto bacanão se você utilizar o cupom <a href="https://www.udemy.com/javascript-completo-2018-do-iniciante-ao-mestre/?couponCode=PROSITE23">PROSITE23</a>. 

Um abraço

