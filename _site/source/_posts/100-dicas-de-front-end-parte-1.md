---
title: 100 dicas de front-end (parte 1)
date: 2019-01-18 13:09:10
description: Nessa primeira parte desse artigo, apresentarei 50 dicas rápidas sobre o desenvolvimento front-end
tags:
- css
- html
- frontend
---
Resolvi participar da brincadeira e fiz minha compilação com 100 dicas de front-end.

Pode ser que muitas dessas dicas você já saiba, mas creio que até mesmo para os mais experientes possa ter algo de novo.

Resolvi dividir as 100 dicas em duas partes pois percebi que este texto estava ficando muito longo. Espero que não se incomode.
Então, vamos às dicas:

1 – Não deve ser novidade para ninguém que o HTML deve ser usado para marcar nosso conteúdo com tags semânticas. Quando for escrever seu código HTML, tente não pensar no resultado visual e foque no que cada informação da página representa.

2 – Partindo desse princípio, não há nada de errado em usar corretamente a tag ```<br>``` para gerar quebra de linha. Mas se você escrever dois ```<br>```’s seguidos provavelmente o que você está querendo, na verdade, são dois parágrafos.

3 – Ainda sobre essa ótica, uma ```<aside>``` não precisa ficar, necessariamente, ao lado. A tag ```<aside>``` está diretamente relacionada ao que ela representa e não à sua posição no layout. Eu escrevi sobre isso aqui  [Quando o header é aside](https://serfrontend.com/blog/quando-o-header-e-aside/)

4 – Outra tag que pode gerar confusão é o ```<address>```. Essa tag não deve ser utilizada para mostrar um endereço, mas sim as informações de contato do dono da página ou da seção. Segundo o site da [MDN](https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/address), para representar um endereço arbitrário, um que não seja relacionado à informação para contato do dono da página ou da seção, use um elemento ```<p>``` ao invés do elemento ```<address>```.

5 – Nós seres humanos sabemos que "22h00", "22:00" ou "10 horas da noite" representam o mesmo horário. Mas para informarmos à máquina que se trata de um horário, precisamos escrever a marcação correta, ou seja, ```<time datetime="22:00">22h00</time>```. Podemos, inclusive, acrescentar informações sobre o horário universal UTC:  ```<time datetime="22:00-03:00">22h00</time>```.

6 – Quando você precisar representar uma tecla do teclado, use a tag ```<kbd>```. Exemplo: ```<p>Precione <kbd>Ctrl</kbd> + <kbd>P</kbd> Para imprimir</p>```.

7 – Quando você precisar incluir alguma citação externa na sua página, utilize as tags [```<blockquote>```](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote), [```<cite>```](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite) ou [```<q>```](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q) para isso.

8 – Imagens responsivas de verdade precisam utilizar o atributo ```srcset``` (faça o que eu digo, não faça o que eu faço 😁). Exemplo:

```<img src=http://lorempixel.com/400/200/ srcset=http://lorempixel.com/600/300/ 600w, http://lorempixel.com/800/400/ 800w alt="texto alternativo convencional" sizes="(min-width: 480px) 33.33vw, 100vw">```.

No código acima, informamos ao browser que se a viewport for menor que 480px, a imagem ocupará a largura total, caso contrário, a imagem ocupará 1/3 da tela. O browser irá decidir por conta própria qual a melhor fonte de imagem para renderizar na tela.

9 - Você pode incluir emojis no seu HTML ou CSS da maneira que escreve no seu celular 

10 – A tag ```<picture>``` para imagens responsivas é opcional e é utilizado em conjunto com a tag ```<source>``` quando você tem mais de uma fonte de imagem. 
	Você pode ler a respeito no link que escrevi há muito tempo no medium [design responsivo nos dias de hoje](https://medium.com/@tapmorales/design-responsivo-nos-dias-de-hoje-838b869d5fc8).

11 - Uma ```<dl>``` pode ter mais de um ```<dt>``` e ```<dd>```.

Veja dois exemplos copiados na cara-de-pau do [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl).
{% codeblock lang:html %}
<dl>
  <dt>Firefox</dt>
  <dt>Mozilla Firefox</dt>
  <dt>Fx</dt>
  <dd>
    A free, open source, cross-platform,
    graphical web browser developed by the
    Mozilla Corporation and hundreds of
    volunteers.
  </dd>

  <!-- Other terms and descriptions -->
</dl>

<dl>
  <dt>Firefox</dt>
  <dd>
    A free, open source, cross-platform,
    graphical web browser developed by the
    Mozilla Corporation and hundreds of
    volunteers.
  </dd>
  <dd>
    The Red Panda also known as the Lesser
    Panda, Wah, Bear Cat or Firefox, is a
    mostly herbivorous mammal, slightly larger
    than a domestic cat (60 cm long).
  </dd>

  <!-- Other terms and descriptions -->
</dl>
{% endcodeblock %}

12 – Sabe quando você quer destacar um pedaço do texto e acaba envolvendo-o dentro de uma ```<span>``` com uma classe .destaque? Forte indício de que você estava querendo, na verdade, era usar a tag ```<mark>```.

13 – Utilize as tags ```<del>``` e ```<ins>``` para representar textos removidos ou inseridos, respectivamente.

14 – O HTML5 possui um atributo que informa ao agente de usuário que o conteúdo de determinada tag pode ser editado pelo usuário. Deve ser utilizado em conjunto com o javascript. Segue um exemplo de utilização no mundo HTML.

{% codeblock lang:html %}
<p contenteditable="true"> Edite seu conteúdo </p>
{% endcodeblock %}

15 – Por padrão, a tag ```<a>``` recebe o foco quando o usuário navega pelo teclado. Se você precisar que outro elemento tenha o mesmo comportamento, utilize o atributo ```tabindex```. Este atributo recebe um numero inteiro que representa a ordem de navegação.

16 – É possível incluir links que, ao serem clicados, abre o telefone em aparelhos mobile: 
{% codeblock lang:html %}
<a href="tel:1-408-555-5555">1-408-555-5555</a>
{% endcodeblock %}

17 – o atributo ```target="_blank"``` possui problemas de segurança em links. use ```rel="noopener noreferrer"``` para minimizar esse problema.

18 – microdados acrescentam mais valor semântico quando as tags HTML não são suficientes.

Como exemplo, avalie o código a seguir:

{% codeblock lang:html %}
<p>
Daniel Tapias Morales<br>
Intrutor<br>
<a href="http://www.serfrontend.com" >serfrontend.com</a>
</p>
{% endcodeblock %}

Não há nada de errado com o parágrafo acima, porém, a máquina não sabe que se trata de uma pessoa (Daniel) e nem tãopouco de um cargo (instrutor). Vamos corrigir isso usando microdados:

{% codeblock lang:html %}
<p itemscope itemtype="http://schema.org/Person">
<span itemprop="name">Daniel Tapias Morales</span><br>
<span itemprop="jobTitle">Intrutor</span><br>
<a href="http://www.serfrontend.com" itemprop="url">serfrontend.com</a>
</p>
{% endcodeblock %}
Para saber mais http://schema.org

19 – Muito semelhante aos Microdados, que passa informações adicionais ao user-agent, o JSON-LD oferece informações padronizadas aos user-agents como os motores de busca. O conceito é muito parecido com os microdados mas os atributos não são mais inseridos no meio das tags HTML. Esse assunto é muito extenso (e pra ser sincero eu não sou a melhor pessoa pra falar sobre ele). De qualquer forma, segue um exemplo de código

{% codeblock lang:html %}
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "Person",
  "name": "Daniel Tapias Morales",
  "jobTitle": "Intrutor",
  "url": "http://serfrontend.com"
}
</script>
{% endcodeblock %}

20 – Se possível, inclua ```<caption>``` como primeiro filho de suas ```<table>``` contendo uma descrição dos dados da tabela. Note que o atributo summary foi depreciado

21 – Nas células de sua tabela que representam cabeçalhos, troque as suas ```<td>``` por ```<th>```. 

22 – Inclua atributos scope nas suas ```<th>``` para informar ao agente de usuário se este cabeçalho se refere a linhas, colunas, conjunto de linhas ou conjunto de colunas.

Os valores possíveis são, portanto: row, col, rowgroup ou colgroup.

Vai ficar mais fácil entender com uma imagem
![Utilização do scope em <th>](../images/100-dicas-de-front-end-parte-1/table.png "Utilização do scope em <th>")

23 – Agora falando de formulários, utilize as tags ```<fieldset>``` para criar grupos lógicos de suas entradas de dados.

24 – A tag ```<legend>``` acrescenta uma descrição ao ```<fieldset>```.

25 – Faça um vínculo entre o texto que aparece ao usuário e o seu respectivo input com a tag ```<label>```. Voce pode fazer esse vínculo de duas formas:

26 – Com o atributo id que deve ter o mesmo valor do atributo for do ```<label>```.

Veja um exemplo:
{% codeblock lang:html %}
<label for="user">Usuário</label>
<input type="text" id="user" name="txtuser" />
{% endcodeblock %}

27 – Ou envolvendo o input e o texto com a tag ```<label>```.
Mais um exemplo: 
{% codeblock lang:html %}
<label>Usuário <input type="text" name="txtuser" /></label>
{% endcodeblock %}

28 – Nunca, mas NUNCA, crie um ```<input type="radio">``` ou ```<input type="checkbox">``` sem um ```<label>``` relacionado. Isso cria um vínculo entre o campo e o texto que aparece para o usuário. Isso é regra básica para melhorar a acessibilidade de sua interface.

30 – É permitido ter dois ```<label>``` para o mesmo input. Não há nada de errado com isso.

31 – Se a função da sua página é fazer com que o usuário digite algo em um input, como por exemplo uma página de busca ou um formulário de login, acrescente um atributo ```autofocos``` no seu input. Isso também facilita a usabilidade

32 – Voce pode utilizar a tag ```<optgroup>``` para agrupar ```<option>``` dentro de um ```<select>```.

{% codeblock lang:html %}
<select>
  <optgroup label="Grupo 1">
    <option>Opção 1.1</option>
  </optgroup> 
  <optgroup label="Grupo 2">
    <option>Opção 2.1</option>
    <option>Opção 2.2</option>
  </optgroup>
  <optgroup label="Grupo 3" disabled>
    <option>Opção 3.1</option>
    <option>Opção 3.2</option>
    <option>Opção 3.3</option>
  </optgroup>
</select>
{% endcodeblock %}

33 – Se vc tem um texto muito grande sem espaço (exemplo de uma URL) e está quebrando em aparelhos mobile, pode colocar ```<br>``` opcionais. Como? Com a tag ```<wbr>```. É só colocar essa tag onde você quer que quebre para a próxima linha se for necessário.

Exemplo:
{% codeblock lang:html %}
<p> http://www.serfrontend.com/<wbr>qualquer/<wbr>url/<wbr>/bem/<wbr>grande...</p>

{% endcodeblock %}
34 – Ao contrário do  ```<wbr> ``` há também a tag  ```<nobr> ```, que diz para o navegador que não pode quebrar linha. Mas atenção: essa tag foi depreciada e não deve ser usada. Use CSS no lugar.

{% codeblock lang:html %}
<span style="white-space: nowrap">Texto longo sem quebras de linha</span>
{% endcodeblock %}

35 – Outra tag que foi depreciada e, portanto, não deve ser usada é a ```<hgroup>``` que servia para agrupar títulos. Não a use.

36 – A tag ```<figure>``` não tem nada a ver com figuras. Ela é usada para demarcar uma área independente do documento. Algo que,  se for removido da página, não causa prejuízo ao conteúdo principal. 

37 – dentro de ```<figure>``` você pode incluir um ```<figcaption>``` que representa uma legenda da tag ```<figure>```.

38 – Outra tag bem importante para semântica é a ```<abbr>```. É usada quando temos abreviações. Você pode ter pensado em ```<acronym>```, mas esta foi depreciada.

{% codeblock lang:html %}	
<p>Eu amo <abbr title="Linguagem de marcação de hypertextos">HTML</abbr></p>
{% endcodeblock %}

38 – Coloque o atributo lang no seu ```<html>``` indicando qual é o idioma da página. E coloque o atributo lang em outras tags atualizando o idioma quando necessário. Exemplo:
{% codeblock lang:html %}	
<html lang="pt-br">
  <body>
    <p> Eu amo o <i lang="en-us">Hypertext Language Markup</i>.</p>
  </body>
</html> 
{% endcodeblock %}

39 – Falando agora de CSS. Já precisou colocar uma borda interna em um elemento? Não faça gambiarras. Você pode incluir um outline e um outline-offset. Inclusive pode animar a distância interna da borda.

{% codeblock lang:css %}
div{
  outline: 1px dotted blue;
  outline-offset: -10px;
}
div:hover{
outline-offset: -50px;
}
{% endcodeblock %}

<p class="codepen" data-height="465" data-theme-id="0" data-default-tab="css,result" data-user="tapmorales" data-slug-hash="WLqgwK" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid black; margin: 1em 0; padding: 1em;" data-pen-title="outline animated">
  <span>See the Pen <a href="https://codepen.io/tapmorales/pen/WLqgwK/">
  outline animated</a> by daniel tapias morales (<a href="https://codepen.io/tapmorales">@tapmorales</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

40 – Provavelmente vc já sabia que dá pra incluir um contador com CSS.

{% codeblock lang:css %}
main {
  counter-reset: paragrafos;                     
}

h3::before {
  counter-increment: paragrafos;                 
  content: counter(paragrafos);                  
}
{% endcodeblock %}

Mas além disso, dá pra definir qual número inicial da contagem.

{% codeblock lang:css %}
main {
  counter-reset: parágrafos 9;                     
}

h3::before {
  counter-increment: paragrafos;                 
  content: counter(paragrafos);                  
}
{% endcodeblock %}

Agora a contagem começará em 10.

41 – Sabia que dá pra ampliar ou diminuir uma sombra do box-shadow? É só passar um valor adicional antes da cor. Este valor é um número em pixels. Se positivo, então a sombra é ampliada. Se negativo, a sombra é reduzida.

{% codeblock lang:css %}
box-shadow: 2px 2px 2px 10px rgba(0, 0, 0, 0.2);
{% endcodeblock %}

A sombra será ampliada 10 pixels.

42 – Por padrão, as células de uma tabela são separadas umas das outras. Para mudar esse comportamento:

{% codeblock lang:css %}
border-collapse: collapse;
{% endcodeblock %}

43 - provavelmente você já conhece text-decoration: underline; Mas saiba que dá fazer coisas muito mais legais, como por exemplo: ```text-decoration: underline wavy #c09;``` que na verdade é um atalho para 

{% codeblock lang:css %}
text-decoration-line: underline;
text-decoration-style: wavy;
text-decoration-color: #c09;
{% endcodeblock %}
<p class="codepen" data-height="465" data-theme-id="0" data-default-tab="css,result" data-user="tapmorales" data-slug-hash="VqJGxz" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid black; margin: 1em 0; padding: 1em;" data-pen-title="VqJGxz">
  <span>See the Pen <a href="https://codepen.io/tapmorales/pen/VqJGxz/">
  VqJGxz</a> by daniel tapias morales (<a href="https://codepen.io/tapmorales">@tapmorales</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>

Isso não vai funcionar no IE. Mas é a vida!

44 – Media-queries não gera especificidade. Isso significa que o código abaixo não funciona da maneira que você espera.

{% codeblock lang:css %}
@media screen and (min-width: 1000px) {
  body{
    background: red;
  }
}
body{
  background: blue;
}
{% endcodeblock %}


45 - No flexbox, não existe horizontal e vertical. O que existe é eixo principal (main axis) e transversal (cross axis). Você pode falar que o eixo principal é horizontal com flex-direction: row; e que é vertical quando flex-direction: column. Um detalhe importante é que isso é válido apenas em escritas horizontais (dir=ltr).

46 – Há um espaço obrigatório entre elementos com display: inline-block assim como há um espaço entre duas palavras (elementos inline). Existem gambiarras que removem esses espaços, mas todas elas são muito feias para constar nessa lista.

47 – Provavelmente você já conhece background-repeat. Sabia que esta propriedade aceita dois valores pouco usados: ```round``` e ```space```? Pois é, elas tratam como a imagem de fundo irá se repetir. 
Ambos os valores fazem com que a imagem de fundo que se repete nunca seja cortada (exceto quando o valor for ```space``` e a imagem for maior do que o elemento). A diferença é que enquanto o valor ```space``` distribui as imagens igualmente no espaço interno do elemento, o valor ```round``` aumenta ou diminui a imagem de fundo para que se ajuste ao elemento. 

<p class="codepen" data-height="485" data-theme-id="0" data-default-tab="css,result" data-user="tapmorales" data-slug-hash="oJraqM" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid black; margin: 1em 0; padding: 1em;" data-pen-title="oJraqM">
  <span>See the Pen <a href="https://codepen.io/tapmorales/pen/oJraqM/">
  oJraqM</a> by daniel tapias morales (<a href="https://codepen.io/tapmorales">@tapmorales</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>


48 – Já tentou aplicar ```box-shadow``` num elemento com transparência e o resultado não foi exatamente o que você esperava? Tente trocar o ```box-shadow``` por ```filter: drop-shadow()```. A diferença é que este respeita a transparência do conteúdo, seja um .png transparente, um svg ou até mesmo um desenho criado pelo próprio CSS.

49 – Sabia que dá pra utilizar no CSS qualquer valor passado por atributo HTML? Para isso, basta usar o ```attr()```. Veja um exemplo:

{% codeblock lang:html %}
<div data-index-number="12314">
...
</div> 
{% endcodeblock %}

CSS:
{% codeblock lang:css %}
div::before {
  content: attr(data-index-number);
}
{% endcodeblock %}

Importante notar que este conteúdo não está acessível em tecnologias assistivas ou motores de busca. Nem mesmo é possível que o usuário selecione este conteúdo na página.

50 – Para incluir o valor do atributo href dinamicamente em link quando impresso ou salvo em pdf, utilize a seguinte regra:

{% codeblock lang:css %}
@media print{
    a[href]::after{
        content: " (" attr(href) ")";
    }
}
{% endcodeblock %}

O que esta regra faz é incluir depois do texto do link o valor do atributo href entre parênteses, apenas em impressões ou PDF’s.


Por enquanto é isso. Em breve apresentarei mais 50 dicas de front-end. 

Obrigado pela leitura