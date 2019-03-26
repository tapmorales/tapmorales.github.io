---
title: 100 dicas de front-end (parte 2)
date: 2019-03-26 13:14:34
description: Na segunda parte do artigo, apresentarei mais 50 dicas rápidas sobre o desenvolvimento front-end
tags:
- css
- html
- frontend
- javscript
---
Dando continuidade a [parte 1 do post 100 dicas de front-end](https://serfrontend.com/blog/100-dicas-de-front-end-parte-1/), segue complemento ao texto anterior. Espero que curtam!

*51 - Em uma `<picture>`, a `<img>` não é opcional.*
Apesar de `<img>` servir como um fallback, ela continua sendo obrigatória, assim como o seu atributo `alt`. Contudo, dentro de uma `<picture>`, o user-agent pode usar outra fonte para "trocar" o src da `<img>`, dependendo dos atributos sizes e srcset. 

{% codeblock lang:html %}
<picture>
  <source media="(min-width: 480px)" 
    sizes="33vw" 
    srcset="rwd-images/1280.jpg 1280w, 
    rwd-images/960.jpg 960w, 
    rwd-images/480.jpg 480w" >
  <source sizes="100vw" 
    srcset="rwd-images/822_mob.jpg 822w, 
    rwd-images/640_mob.jpg 640w, 
    rwd-images/320_mob.jpg 320w">
  <img src="rwd-images/1280.jpg" alt="texto alternativo">

</picture>
{% endcodeblock %}

Essa será a única dica de HTML nesta parte 2. Caso queira mais dicas de HTML, veja na [parte 1](https://serfrontend.com/blog/100-dicas-de-front-end-parte-1/)

*52 - múltiplos gradientes ou backgrounds.*
Podemos incluir múltiplas imagens de background ou gradientes num elemento, sempre observando que a primeira imagem ou gradiente inserida ficará no topo, acima das outras imagens ou gradientes. Por exemplo, se quiser colocar um gradiente sobre uma imagem de fundo, devemos ter o seguinte código 

{% codeblock lang:css %}
body { 
  background-image: url(image-one.jpg), 
  linear-gradient(black, transparent); 
}
{% endcodeblock %}

*53 - currentColor*
Essa propriedade serve para indicar que queremos usar a mesma cor da fonte do elemento, seja essa cor aplicada diretamente ou herdada.

{% codeblock lang:css %}
button { 
  color: red;
  border: 2px solid currentColor;
}
button:hover {
  color: green;
}
{% endcodeblock %}

Desse jeito, a cor da borda mudará automaticamente ao passarmos o mouse sobre o button

*54 - will-change*
Essa propriedade serve para dizer ao navegador que uma propriedade possivelmente será alterada no futuro, fazendo com que o navegador faça as otimizações de performance previamente, o que pode, em alguns casos, melhorar a percepção de performance da interface do usuário. Use com cautela, pois seu uso indiscriminado pode ter o efeito reverso, ou seja, prejudicar a performance da página no browser
{% codeblock lang:css %}
.element { will-change: transform; }
{% endcodeblock %}

*55 - text-overflow*
Eu já usei essa propriedade algumas vezes na minha vida. Ela trata como o texto que excede ao tamanho do seu container deve se comportar. Apesar de aceitar alguns valores, você provavelmente irá optar por clip ou ellipsis. Este mostra reticências e aquele simplesmente esconde o texto que não couber no elemento. 

Para ver essa propriedade em ação, você precisa trabalhar junto com outras duas propriedades, white-space e overflow. Veja um exemplo:

{% codeblock lang:css %}
.reticecias{
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
{% endcodeblock %}
 
*56 - animation-play-state*
É possível pausar ou continuar uma animação feita com CSS usando a propriedade animation-play-state com o valor paused ou running.

Por exemplo, podemos pausar uma animação no hover do mouse.

{% codeblock lang:css %}
div {
  animation: mover 5s alternate infinite;
}

div:hover{
  animation-play-state: paused;
}

@keyframes mover{
  from {transform: translateX(0px);}
  to {transform: translateX(200px);}
}
{% endcodeblock %}

*57 - propriedade transform cria empilhamento z-index.*
Essa é loka. Em alguns momentos a propriedade transform pode ter um efeito indesejável, fazendo com que o elemento "pule" para frente de outros. Isso acontece porque, por baixo dos panos, a propriedade transform cria um contexto de emplilhamento z-index. 

Mais fácil explicar com códigos.

<p class="codepen" data-height="365" data-theme-id="0" data-default-tab="result" data-user="tapmorales" data-slug-hash="moogLx" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid black; margin: 1em 0; padding: 1em;" data-pen-title="transform e z-index">
<span>See the Pen <a href="https://codepen.io/tapmorales/pen/moogLx/">
transform e z-index</a> by daniel tapias morales (<a href="https://codepen.io/tapmorales">@tapmorales</a>)
on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

*58 - Selecionar o ante-penúltimo elemento usando a pseudo classe :nth-last-child(n).*
{% codeblock lang:css %}
.my-class:nth-last-child(3) {
  background:red;
}
{% endcodeblock %}

*59 - Selecionar os três último elementos usando o seletor ~ (next siblings).*
{% codeblock lang:css %}
.my-class:nth-last-child(4) ~ .my-class {
  background:red;
}
{% endcodeblock %}

*60 - nth-child vs nth-of-type - parte1.*
Esses seletores podem induzir ao erro. Por exemplo, você pode pensar que `p:nth-child(3)` irá selecionar o terceiro parágrafo. Mas isso não é bem verdade. O que este seletor faz é selecionar o terceiro filho **se** este for um parágrafo.

Portanto, a seguinte regra

{% codeblock lang:css %}
p:nth-child(3) { color: red; }
{% endcodeblock %}

Irá funcionar só na primeira div, já que na segunda div o terceiro filho não é um parágrafo
{% codeblock lang:html %}
<div>
  <p>...</p>
  <p>...</p>
  <p>p:nth-child(3) funciona aqui</p>
  <p>...</p>
</div>
<div>
  <p>...</p>
  <p>...</p>
  <br>
  <p>...</p>
</div>
{% endcodeblock %}

*61 - nth-child vs nyh-of-type - parte2.*
Já o nth-of-type seleciona o terceiro filho do tipo (ou tag). Então `p:nth-of-type(3)` irá selecionar nas duas divs o terceiro parágrafo. 

{% codeblock lang:html %}
<div>
  <p>...</p>
  <p>...</p>
  <p>p:nth-of-type(3) funciona aqui</p>
<p>...</p>
</div>
<div>
  <p>...</p>
  <p>...</p>
  <br>
  <p>p:nth-of-type(3) funciona aqui</p>
</div>
{% endcodeblock %}

Parece bem mais lógico, não é mesmo? Mas a confusão pode aparecer quando temos algo como o código abaixo.

{% codeblock lang:css %} 
p:nth-of-type(3) { color: red;}
.nth:nth-of-type(3) { background-color: yellow}
{% endcodeblock %}

{% codeblock lang:html %}
<div>
  <p class="nth">...</p>
  <p>...</p>
  <p>... </p>
  <p>...</p>
  <br>
  <p class="nth">...</p>
  <p class="nth">Achou que este estaria com fundo amarelo? Acho errado querido leitor</p>
  <p class="nth">...</p>
</div>
{% endcodeblock %}

O que aconteceu? O `.nth:nth-of-type(3)` deleciona o terceiro filho do tipo do seletor(no caso, um parágrafo) **se** este tiver a classe .nth. Um pouco confuso no início, eu assumo, mas como regra geral, saiba que o of-type (por tipo) diz respeito à tag, e não à classe ou ao id. 

Quer ver o código acima funcionando? Coloque uma classe .nth no terceiro parágrafo
{% codeblock lang:html %}
<div>
  <p>primeiro p</p>
  <br>
  <b> negrito </b>
  <p>segundo p</p>
  <p class="nth">terceiro p - FUNCIONOU \o/</p>
  <br>
</div>
{% endcodeblock %}

*62 - porcentagem - parte 1.*
O valor de porcentagem aplicado ao width, margin ou padding de um elemento filho é sempre relativo ao width do elemento pai. 

*63 - porcentagem - parte 2.*
Isso significa que height: 50% é a metade da altura do elemento pai (desde que a altura seja definida explicitamente, ou seja, não pode ter o valor auto, que é o valor default). Contudo, margin-top de 50% possui uma distância igual à metade da largura do elemento pai. 

O mesmo vale para padding-top, margin-bottom ou padding-bottom.

Imagine o seguinte:

{% codeblock lang:html %}
<div style="width: 500px; height: 300px;">
  <p style="height: 50%; margin-top: 10%"> ... </p>
</div>
{% endcodeblock %}

O parágrafo acima terá altura de 150px (50% da altura do elemento pai) mas 50px de margin-top (10% da **largura** do elemento pai)

*64 - porcentagem - parte 3.*

O valor em porcentagem aplicado em transform: translate é sempre proporcional ao tamanho do próprio elemento. Se aplicado ao translateX, é relativo à largura do elemento. Se aplicado ao height, se refere à altura.

*65 - a propriedade transform muda o eixo xy do elemento na ordem em que as transformações são aplicadas.* 
Isso significa que a ordem de escrita muda o resultado final. 

Por exemplo: `transform: translateX(500px) rotate(45deg)` tem um resultado bem diferente de `transform: rotate(45deg) translateX(500px)`.

*66 - opacidade menor que 1 gera contexto de empilhamento z-index.*
Essa também é loka. 

Aplicar opacidade menor que 1 também cria um contexto de empilhamento. Se você tiver problemas com isso especialmente em animações, tente trocar para rgba ou hsla. Em alguns casos isso é possível, em outros não. Se não for possível trabalhar com rgba ou hsla, terá que trabalhar em conjunto com z-index.

<p class="codepen" data-height="365" data-theme-id="0" data-default-tab="result" data-user="tapmorales" data-slug-hash="XGGvJv" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid black; margin: 1em 0; padding: 1em;" data-pen-title="XGGvJv">
<span>See the Pen <a href="https://codepen.io/tapmorales/pen/XGGvJv/">
XGGvJv</a> by daniel tapias morales (<a href="https://codepen.io/tapmorales">@tapmorales</a>)
on <a href="https://codepen.io">CodePen</a>.</span>
</p>

*67 - flexbox space evenly*
Falando de justify-content, que trata da distribuição dos flex-items no main axis, temos a opção space-evenly, que irá deixar todos os espaços vazios exatamente iguais, incluindo o espaço antes do primeiro item e após o último item.

*68 - border-box.*
Por padrão o padding soma ao valor do width e height do elemento. Esse comportamento pode ser alterado com `box-sizing: border-box;`

*69 - ordem de classes.*
a ordem das classes no HTML não muda a especificidade. Portanto, os dois códigos HTML abaixo produzem o mesmo resultado.
{% codeblock lang:html %}
<p class=" red blue "> ... </p>
<p class=" blue red "> ... </p>
{% endcodeblock %}

*70 - em*
1em aplicado à fonte é relativo ao tamanho da fonte do elemento pai. Se aplicado em qualquer outra propriedade é relativo ao tamanho da fonte do elemento atual, seja aplicado diretamente ou herdade de algum elemento ancestral.

*71 - vh e vw*
Essas unidades de medida são sempre relativas ao tamanho da viewport. 100vh é 100% da altura da viewport ao passo que 100vw é 100% da largura da viewport.

*72 - text-transform: uppercase vs font-variant small-caps*
Há uma diferença sutil entre essas duas propriedades. Ambas vão deixar as fontes em letras maiúsculas, mas a diferença está no tamanho da fonte. `text-transform: uppercase` deixa todas as letras de tamanho de fontes maiúsculas. Já `font-variant small-caps` mantem o tamanho de fontes minusculas mas com aparência de fontes maiúsculas.

*73 - gradientes em textos?*
O interessante com essa técnica é que ela só funciona com o prefixo -webkit-, até mesmo do Edge e Firefox nas versões mais novas. 

Para termos um gradiente no texto, temos que trabalhar com duas propriedades em conjunto além da background-image
{% codeblock lang:css %}
background-image: linear-gradient(red, blue);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
{% endcodeblock %}

*74 - formatar scrollbar em webkit*
Se quiser formatar a barra de rolagem, tenha em mente que só funciona em navegadores webkit. Então vamos direto ao código

{% codeblock lang:html %}
<div id="sc">
muito texto pra gerar barra de rolagem
</div>
{% endcodeblock %}

{% codeblock lang:css %}
#sc{
  width: 200px;
  height: 120px;
  overflow: scroll;
}

#sc::-webkit-scrollbar-track {
  border-radius: 5px;
  background-color: red;
}

#sc::-webkit-scrollbar{
  width: 10px; /* largura da barra vertical */
  height: 10px; /* altura da barra horizontal */
}

#sc::-webkit-scrollbar-thumb{
  border-radius: 5px;
  background-color: orange;
}
{% endcodeblock %}

Agora vamos às dicas de javascript

*75 - Comparar objetos*
Como comparar se um objeto é igual ao outro? Como sabemos `{} === {}` retorna false pois cada objeto, mesmo que contendo propriedades e valores iguais, ocupam posições diferentes na memória. Quando um objeto só possui propriedades, e não métodos, costumo transformar os dois objetos em strings com JSON.stringify() e comparar o resultado
{% codeblock lang:js %}
{ prop: 'value' } === { prop: 'value' } //false
JSON.stringfy({ prop: 'value' }) === JSON.stringfy({ prop: 'value' }) //true
{% endcodeblock %}

*76 - array com valores únicos*
Uma forma que você pode pensar para obter um array com valores únicos a partir de outro array talvez envolva loops ou, mais elegantemente, um callback dentro de um array.filter().

Contudo, sabendo que agora podemos trabalhar com conjuntos (que não podem ter valores duplicados por definição) podemos obter um array contendo os valores de um conjunto.

Por exemplo:
{% codeblock lang:js %}
const arr1 = [1, 2, 2, true, true, 'str', 0, 'str']
const set = new Set(arr1)
{% endcodeblock %}

Agora podemos facilmente transformar um conjunto em um array novamente utilizando o spread operator
{% codeblock lang:js %}
const arr2 = [...set]
{% endcodeblock %}
Sem loops nem callbacks. Sucesso!

*77 - Evite usar setInterval*
Para agendar uma função que será executada de tempos em tempos, prefira trabalhar com setTimeout recursivo. 

Essa é uma melhor prática devido a um mecanismo interno chamado event loop.

*78 - if melhorado - parte 1*
ao invés de escrever algo como:
{% codeblock lang:js %}
if(condicao){
    fazAlgo();
}
{% endcodeblock %}

prefira algo como:
{% codeblock lang:js %}
condicao && fazAlgo()
{% endcodeblock %}

*79 - if melhorado - parte 2*
ao invés de ter algo como:
{% codeblock lang:js %}
if(!condicao){
   fazAlgo();
}
{% endcodeblock %}

Prefira algo como:
{% codeblock lang:js %}
condicao || fazAlgo()
{% endcodeblock %}

*80 - Valor padrão*
Esse mesmo curto-circuito mostrado acima pode ser usado para atribuir valores padrões. Ex:
{% codeblock lang:js %}
let obj = obj || {}
{% endcodeblock %}

Se já não existir obj, então um objeto limpinho será atribuído à obj

*81 - `Math.max` e `Math.min` são muito uteis e pouco usados.*
Eles retornam o maior e menor valor, respectivamente, dos valores passados por parâmetro

*82 - potência abreviada* 
Com ES6 há uma forma abreviada de termos a potência de um número. Exemplo: 
{% codeblock lang:js %}
  Math.pow(2, 3)
{% endcodeblock %}

é o mesmo que 
{% codeblock lang:js %}
  2**3
{% endcodeblock %}
e significa 2 ao cubo.

*83 - Organizar arrays.*
O método sort() recebe uma função de callback que será executada para cada elemento do array e organizar esse array de acordo com o retorno desse callback. 

Para organizar um arra numérico em ordem crescente, faça o seguinte:
{% codeblock lang:js %}
let arr = [3,4,8,1,6,8]
arr = arr.sort((a, b) => a - b);
{% endcodeblock %}

*84 - formas de duplicar um array, deixando o array original intacto.*
{% codeblock lang:js %}
let arr = [3,4,8,1,6,8]
let arr1 = [].concat(arr)
{% endcodeblock %}
OU
{% codeblock lang:js %}
let arr2 = Array.from( ...arr );
{% endcodeblock %}

*85 - every e some*
Duas funções muito úteis e pouco utilizadas. Ambas recebem uma função de callback e retornam um booleano. A diferença é que a every() retorna true se todas as execuções do callback retornarem true. Já na some() basta que uma execução retorne true para que o retorno seja avaliado como true.
{% codeblock lang:js %}
let arr1 = [1,2,'3', 'teste']
arr1.some( el => isFinite(el) ) //true
arr1.every( el => isFinite(el) ) //false
{% endcodeblock %}

*86 - Obter timestamp facilmente*
{% codeblock lang:js %}
let tsNow = +new Date()
{% endcodeblock %}

*87 - Obter um boolean facilmente.*
Use a negação da negação
{% codeblock lang:js %}
!!"" // false
!!0 // false
!!null // false
!!undefined // false
!!NaN // false
!!"hello" // true
!!1 // true
!!{} // true
!![] // true
{% endcodeblock %}

*88 - passar parâmetro para uma função de callback*
Durante muito tempo eu fiz desse jeito pra poder passar um parâmetro para uma função de callback
{% codeblock lang:js %}
$elemento.addEventListener('click', function(){
    fazAlgo('meu-parametro-lindo')
})
{% endcodeblock %}

Mas recentemente descobri que há outra forma, utilizando algo que já conhecia há muito tempo: clousure.
{% codeblock lang:js %}
function fazAlgo(meuParam) {
  return function() {
    console.log('meuParam ', meuParam);
  }
}
{% endcodeblock %}

Agora é só executar a função dentro do listener, sem necessitar mais daquela função anônima feia
{% codeblock lang:js %}
$elemento.addEventListener('click', fazAlgo('meu-parametro-lindo')).
{% endcodeblock %}

Coisa Linda!

*89 - entender o this*
O this no Javascript é algo bem dinâmico e depende de vários fatores para sabermos exatamente o que é o this. 
Fiz [um artigo sobre isso](https://serfrontend.com/blog/entender-todas-as-formas-do-this-em-javascript/)

*90 - Sempre retornar uma instância mesmo que o desenvolvedor esqueça o operador new*
Em alguns casos, precisamos garantir que uma função seja sempre executada com o operador new para retornar uma nova instância do objeto.

Mas o que acontece se o programador esquecer de usar o operador new?

Podemos tratar isso fazendo uma rápida verificação e retornando assim uma nova instância.
{% codeblock lang:js %}
function Pessoa(nome){
  if(!(this instanceof Pessoa)){
	return new Pessoa(nome);
  }
  this.nome = nome;
}
const eu = new Pessoa('Daniel')
const ele = Pessoa('João') 
{% endcodeblock %}

*91 - diferença entre `function Pessoa(){}`, `const eu = Pessoa()`, e `const ele = new Pessoa()`*
Essa caiu pra mim na minha entrevista técnica para uma vaga de emprego.

function Pessoa(){} é somente uma expressão de função.
var eu = Pessoa() apenas armazena o valor retornado de Pessoa dentro da variavel eu
var ele = new Pessoa() cria um objeto limpo e armazena numa variavel chamada ele

*92 - copiar objeto*
Vimos como duplicar arrays. Mas como podemos fazer para duplicar objetos?

O jeito mais fácil é usarmos o método `Object.assign(destino, origem)`.

`destino` será um objeto limpo, sem nada. `origem` você já sabe o que é.
{% codeblock lang:js %}
var obj = { propriedade: 'valor' };
var clone = Object.assign({}, obj);
{% endcodeblock %}

*93 - Array.from vs Array.of*
Ambos servem para criar uma array. Array.from pode receber um objeto array-like ou uma array como parâmetro. Array.of recebe os valores separados por vírgula.

O código irá demonstrar melhor o que cada método faz:

{% codeblock lang:js %}
arr = Array.from( [1,2,3] ) // Uma array nova contendo os valores da array passada por parâmetro [1, 2, 3]
arr = Array.of(1,2,3) // Uma array nova contendo os valores passados por parâmetro [1, 2, 3]
arr = Array.of( [1,2,3] ) // Uma array contendo um único índice. [ [1,2,3] ]
arr = Array.from(1,2,3) // ERRO
{% endcodeblock %}

Agora falando um pouco de ferramentas front-end

94 - não instale pacotes globalmente com a flag -g. Portanto, evite usar npm install -g mesmo que a maioria dos tutoriais peça pra você fazer isso. Prefira instalar localmente e rodar o pacote usando npm-script.

95 - use um gerenciador de versões do node, como o nvm ou simplesmente n.

96 - No vscode use Alt Shift seta pra baixo ou para cima para duplicar linhas.

97 - No vscode use Alt seta pra baixo ou para cima para mover uma linha de código.

98 - limpe a pasta node_modules depois do deploy para otimizar seu precioso espaço em disco.

99 - o npx não vem com o nodejs se instalado pelo nvm. para resolver isso, ignore a dica 94 e faça o seguinte: npm i -g npx.

100 - o watch do node-sass não funciona muito bem no vscode. utilize o nodemon no lugar do --watch. 

Prontinho. 100 dicas conforme prometido.

E aí? Alguma dessas dicas foi novidade pra você? Tem sugestão de alguma dica que não incluí nessa lista? Deixe seu comentário ou feedback. Ficarei grato de saber o que você achou desse post.