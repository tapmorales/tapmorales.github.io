---
title: Quando o header é aside
date: 2018-05-22 20:47:06
description: Ou, quando o header é ao lado e o aside é no topo.
tags:
- frontend
- html
- semântica
---

Não! Eu não estou falando de culturas onde a leitura é diferente da nossa e também não estou falando do design visto de lado.

A motivação para escrever este artigo foi no meio do planejamento do meu curso de [Web Fundamentos: HTML e CSS](https://www.udemy.com/curso-web-design-fundamentos-aprenda-html-css-e-javascript/?couponCode=PROMOSOCIAL), onde eu elaborei um pequeno projeto onde o resultado final é mostrado na imagem abaixo:

![Layout do exercício do curso de web fundamentos](../images/quando-o-header-e-aside/tags-semanticas-1.jpg "Layout do exercício do curso de web fundamentos")

A <del>inspiração</del> cópia para este exercício foi este [template](https://html5up.net/strata)

É muito comum estruturarmos os nossos layouts utilizando as tags semânticas do HTML, então, à primeira vista, talvez você tenha pensado que as tags mais corretas para chegarmos nesse resultado seriam: 

![Layout do exercício do curso de web fundamentos contendo tags erradas](../images/quando-o-header-e-aside/tags-semanticas-2.jpg "Layout do exercício do curso de web fundamentos contendo tags erradas")

Isso porque tendemos a pensar em &lt;header&gt; como sendo no topo, &lt;aside&gt; como sendo ao lado, &lt;footer&gt; no rodapé e &lt;nav&gt; sendo a navegação. Ou seja, somos levados a pensar em tags semânticas como pensamos em organização visual. E é aí que mora o problema, pois precisamos esquecer a parte visual e voltarmos para as origens das tags do HTML e qual o real significado de cada tag. Afinal, quem cuida do visual é o CSS, e não o HTML.

Parafraseando o site da [mozzila](https://developer.mozilla.org), resolvi transcrever pequenos trechos de código de lá. Aliás, já que estamos falando em semântica, inspecione o código fonte dessa página para ver qual tag utilizei para citar um trecho de outro site ;)

<blockquote cite="https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/header">O elemento <strong>HTML &lt;header&gt; </strong>representa um grupo de suporte introdutório ou navegacional. Pode conter alguns elementos de cabeçalho mas também outros elementos como um logo, seções de cabeçalho, formulário de pesquisa, e outros.
</blockquote>


<blockquote cite="https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/aside">O elemento <strong>HTML &lt;aside&gt;</strong> representa uma seção de uma página que consiste de conteúdo que é tangencialmente relacionado ao conteúdo do seu entorno, que poderia ser considerado separado do conteúdo. Essas seções são, muitas vezes, representadas como barras laterais. Elas muitas vezes contem explicações laterais, como a definição de um glossário; conteúdo vagamente relacionado, como avisos; a biografia do autor; ou, em aplicações web, informações de perfil ou links de blogs relacionados.
</blockquote>


<blockquote cite="https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/footer">O elemento <strong>HTML de Rodapé (&lt;footer&gt;) </strong>representa um rodapé para o seu sectioning content (conteúdo de seção) mais próximo ou sectioning root elemento (ou seja, seu parente mais próximo &lt;article&gt;, &lt;aside&gt;, &lt;nav&gt;, &lt;section&gt;, &lt;blockquote&gt;, &lt;body&gt;, &lt;details&gt;, &lt;fieldset&gt;, &lt;figure&gt;, &lt;td&gt;). Normalmente um rodapé contém informações sobre o autor da seção de dados, direitos autorais ou links para documentos relacionados.
</blockquote>


<blockquote cite="https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/nav">O Elemento <strong>HTML de Navegação (&lt;nav&gt;)</strong> representa uma seção de uma página que aponta para outras páginas ou para outras áreas da página, ou seja, uma seção com links de navegação. Nem todos os links de um documento devem estar dentro de um elemento &lt;nav&gt;, o qual é destinado apenas para grupos importantes de links de navegação; tipicamente o elemento &lt;footer&gt; contém uma lista de links que não precisam estar em um elemento &lt;nav&gt;.
</blockquote>


Com as definições bem fundamentadas em nossa mente e sem nos preocuparmos com o aspecto visual, veja se faz mais sentido a estrutura semântica representada na imagem a seguir:

![Layout do exercício do curso de web fundamentos contendo tags corretas](../images/quando-o-header-e-aside/tags-semanticas-3.jpg "Layout do exercício do curso de web fundamentos contendo tags corretas")

Se avaliarmos as tags mostradas na imagem acima e compararmos com os objetos semânticos de cada uma dessas tags, vemos que esta última faz muito mais sentido. Uma outra forma de representarmos essa estrutura seria através da figura a seguir:

![Representação errada do DOM do exercício do curso de web fundamentos](../images/quando-o-header-e-aside/tags-semanticas-4.jpg "Representação errada do DOM do exercício do curso de web fundamentos").

Ao transformarmos essa representação do DOM em código, teremos

{% codeblock lang:html %}
<body>
  <header>
  	<footer></footer>  	
  </header>
  <main></main>  
<body>
{% endcodeblock %}

Opa! Sinal vermelho! Colocar um footer dentro de um header? Isso não me parece uma boa escolha, visto que há um conflito semântico aí. Mas como agradar o designer que pensou nesse layout com tanto carinho? Bom, design é outra história. Portanto, vamos focar no HTML. Sendo assim, o mais correto seria:

![Representação correta do DOM do exercício do curso de web fundamentos](../images/quando-o-header-e-aside/tags-semanticas-5.jpg "Representação correta do DOM do exercício do curso de web fundamentos")

Agora transcrevendo em código com a estrutura corrigida:

{% codeblock lang:html %}
<body>
  <header></header>
  <main></main>
  <footer></footer>
<body>
{% endcodeblock %}

Mas e a questão do posicionamento do footer dentro da coluna à esquerda? Bom, isso é uma questão visual e, como dito anteriormente, quem cuida do visual é o CSS. O que não devemos permitir é que uma decisão de design afete a estrutura semântica de nossa página na web.

## Conclusão

Procure utilizar as tags corretas para estruturar seus layouts sem se preocupar com posições, tamanhos, margins etc. Tenha em mente o real objetivo de cada tag e escreva seus códigos muito mais semânticos e, por que não, acessíveis.