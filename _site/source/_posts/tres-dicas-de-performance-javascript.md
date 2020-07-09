---
title: Três dicas de performance javascript
date: 2020-07-09 19:34:25
tags:
- frontend
- javascript
- performance
---

Neste post vamos aprender como evitar problemas de memory leaks em javascript no browser, evitando crashs indesejados.

*Memory leaks*, traduzido ao pé da letra significa vazamento de memória, o que, na prática significa que o Sistema operacional não está conseguindo gerenciar a memória utilizada de forma eficiente, o que pode fazer com que o Sistema fique lento ou até mesmo a aplicação (browser) trave.

É verdade que na maioria das vezes em que programamos em javascript para rodar no browser não precisamos nos preocupar com esse tipo de problema pois há um mecanismo chamado *garbage collector* que "limpa" a memória de tempos em tempos quando há possibilidade: uma variável que não é mais utilizada, uma function que não será mais executada, etc.

Se em algumas linguagens o programador precisa explicitamente dizer ao Sistema operacional quando determinada parte da memória pode ser limpa, há outras linguagens, como o javascript, em que o garbage collector faz o trabalho sujo pra gente. Mas nem sempre esse serviço pode ser feito de forma eficiente. E a raiz disso é o que chamamos referências indesejadas.

## 1 referência indesejada: objeto window (escopo global)

Essa é fácil de entender. Para que o  garbage collector possa limpar uma variavel na memoria, nenhuma referencia à essa variavel pode existir no código, certo? O problema com variaveis e funções no escopo global é que esse tipo de dado pode ser lido ou executado em qualquer momento não previsto (click de um botão, tecla  pressionada, retorno de uma API etc). Tudo o que é global não pode ser limpo. Pois tudo o que pode ser lido ou executado por outra parte do código precisa estar disponível.

De tempos em tempos o garbage collector procura por referencias na memória que não podem mais ser alcançadas por nenhuma outra parte do código e por esse motivo são marcadas como lixo e podem ser removidas.

Evitar poliur o escopo global é fácil, mas as vezes fazemos isso sem querer, veja:

{% codeblock lang:js %}
function foo() {
    console.log(this) //nesse caso, é Window
    this.variable = " global";
}
foo()
{% endcodeblock %}

Para evitar esse tipo de problema mascarado de normalidade, use "use stricit".

{% codeblock lang:js %}
function foo() {
"use strict"
    console.log(this) //nesse caso, é undefiend
    this.variable = " global"; // vai gerar um erro, mas o escopo global está intacto
}
foo()
{% endcodeblock %}


## setInterval

Todos nós que trabalhamos com javascript já precisamos criar uma função que fosse executada de tempos em tempos com o uso do setInterval. E não há nada de errado com isso, desde que você não se esqueça de limpar seu intervalo quando não for mais necessário.

{% codeblock lang:js %}
let x = 0
setInterval(function(){
  x++
  if(x < 10) console.log(x)
}, 1000)
{% endcodeblock %}

É fácil perceber nesse exemplo que será mostrado no console os números de 1 a 9 a cada 1 segundo. Porém, a função anônima continuará sendo executada enquanto a página estiver aberta e por esse motivo essa mesma função anônima não poderá ser limpa pelo garbage collector.

Para corrigir isso, devemos sempre nos lembrar de limpar o interval com o uso do clearInterval

{% codeblock lang:js %}
let interval = setInterval(function(){
  x++
  if(x < 10) return console.log(x)
  interval = null
  clearInterval(interval)
}, 1000)
{% endcodeblock %}

Tente levar esse exemplo para um caso mais real, como um cronômetro com três botões, iniciar, pausar e parar.


## Armazenar referencias do DOM

As vezes queremos usar os métodos convenientes de uma array como filter ou map em uma coleção de objetos do DOM (nodeList ou HTMLCollection). Nesses casos precisamos armazenar as referencias do DOM numa array

{% codeblock lang:js %}
const dom = document.querySelectorAll('.item')
const arr = []
for (let i = 0; i < dom.length; i++) { 
    arr[i] = dom[i]; 
}
{% endcodeblock %}

Nesse ponto você pode estar me chamando de antiquadro e se questionando se os meus conhecimentos de javascript são ultrapassados. Você pode ter pensado no seguinte código:

{% codeblock lang:js %}
const dom = document.querySelectorAll('.item')
const arr = [...dom]
{% endcodeblock %}

Muito mais elegante. Eu concordo. Mas eu pergunto: o seu código vai passar pelo babel?

![tela do babel mostrando que o spread operator vira um loop for](../images/tres-dicas-de-performance-javascript/babel_performance.png "tela do babel mostrando que o spread operator vira um loop for")

Vou colar o trecho do código transpilado que nos interessa para esse exemplo

<figure class="highlight js"><table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br></pre></td><td class="code"><pre><span class="line"><span class="function"><span class="keyword">function</span> \<span class="title">_arrayLikeToArray</span>(<span class="params">arr, len</span>) </span>{ </span><br><span class="line">  <span class="keyword">if</span> (len == <span class="literal">null</span> || len &gt; arr.length) len = arr.length; </span><br><span class="line">  <span class="keyword">for</span> (<span class="keyword">var</span> i = <span class="number">0</span>, arr2 = <span class="keyword">new</span> <span class="built_in">Array</span>(len); i &lt; len; i++) { </span><br><span class="line">   arr2[i] = arr[i]; </span><br><span class="line">  } </span><br><span class="line">  <span class="keyword">return</span> arr2; </span><br><span class="line">}</span><br></pre></td></tr></tbody></table></figure>

O bom e velho loop for é o que o babel faz por baixo dos panos. 

Mas vontando ao tópico do post, ao armazenar referências do DOM numa estrutura de dados como uma array ou um objeto, criamos uma referência para aquele elemento do DOM.

Se removermos esse elemento da arvore do DOM precisamos lembrar de remover as referencias junto, caso contrário esta referência continuará ocupando espaço na memória, mesmo que o elemento em si já não exista mais na página.

Há várias maneiras de fazer isso e a abordagem escolhida vai depender de caso a caso. Apenas tenha em mente que, se criou uma array com elementos do DOM e por algum motivo qualquer a árvore do DOM foi atualizada, atualize também a sua array com o DOM atualizado. Sendo assim, o espaço na memória que armazenava aquele objeto do DOM pode ser limpo.

## Conclusão

Então é isso. Algumas dicas para você ter em mente quando precisar dar um gás na performance da sua aplicação web. 
