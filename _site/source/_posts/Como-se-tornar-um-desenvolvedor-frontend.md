---
title: Como se tornar um desenvolvedor frontend
date: 2018-03-07 11:38:50
tags:
- javascript
- frontend
---
Atualmente sou desenvolvedor front-end e ministro relacionadas nas horas vagas. Nas minhas turmas, é bastante comum ver os alunos, principalmente os que estudam Javascript, ansiosos pela quantidade de tecnologias presentes nas descrições de vagas no mercado de trabalho.

Nesse turbilhão de ansiedade, só tenho uma palavra para acalmá-los: CALMA.

Se você também fica preocupado ou ansioso ao ver os requistos exigidos pelo mercado de desenvolvimento front-end, peço que continue lendo esse artigo.

Se você procurar na internet sobre o que fazer para se tornar um front-ender, verá que 99% dos artigos dizem a mesma coisa: pra você focar na base, ou seja, HTML, CSS e Javascript.

Não parece muito coerente termos, de um lado profissionais experientes escrevendo na web sugerindo focar no fundamental, enquanto o mercado pede as mais variadas tecnologias e ferramentas mesmo para quem está querendo ingressar na área. As mais comuns são: Webpack, Gulp, Sass, Less, React, Angular, Typescript entre outras.

Fica parecendo piegas. É o mesmo que eu falar mal dos políticos corruptos enquanto eu aproveito a oportunidade para ficar com o troco errado que alguém me deu desatentamente.

Para quem já está trabalhando na área é fácil pedir calma. É fácil falar para estudar apenas CSS e Javascript. É fácil não se estressar com o número de coisas que falta pra estudar. É fácil. Sabe esse profissional experiente que diz pra você focar somente no básico? Então… ele está coberto de razão. E eu vou explicar o porquê.

## A tecnologia evolui. Sempre.

O fato é que todas estas coisas novas que aparecem quase todo dia no mundo do desenvolvimento web só têm um objeto: lascar a vida do desenvolvedor. Não! Resolver alguns problemas comuns que tínhamos no passado.

Pode reparar. O webpack veio para suprir a necessidade de carregar assets no client-side. O Gulp ou o Grunt veio para automatizar nossas tarefas repetitivas. O Sass ou o Less veio para facilitar a escrita de CSS manuteníveis. React e Angular para nos facilitar na construção de aplicações web. Typescript veio para resolver uma questão chata no javascript que é o de só ver erros de código em runtime devido à sua linguagem ser fracamente tipada.

E sabe o que tem em comum entre os caras que desenvolveram aquelas tecnologias, você e eu? Todos nós tivemos que começar do começo.

Garanto pra você que a primeira pessoa que escreveu a primeira linha de código do Angular, do React ou até mesmo do Typescript, um dia de sua vida, mesmo que num passado distante, escreveu o seguinte trecho de código:

{% codeblock lang:html %}
<script>
  alert("olá Mundo")
</script>
{% endcodeblock %}

Também posso te garantir que o cara mais fodástico de qualquer pré-processador de CSS, em um dia de sua vida, este mesmo cidadão escreveu em seu editor favorito daquela época:
{% codeblock lang:css %}
.minha-classe{
  color: red;
}
{% endcodeblock %}

Então não se preocupe. Se esses caras chegaram lá, a gente também pode.

Mas de que adianta saber a base, se o mercado exige muito mais.

Eu não estou dizendo que você deve parar seus estudos depois de aprender o fundamental. O que eu estou dizendo é que o fundamental é o mais importante e deve vir primeiro lugar. E em segundo lugar também. Deixe-me explicar.

Depois que você aprender HTML, pesquise sobre semântica e acessibilidade. Dê uma boa olhada nos WAI-ARIAs e também em microdata e JSON-LD. Também é uma boa conhecer um pouco de SEO.

Depois que você se sentir confortável com CSS (ou seja, consegue dominar o posicionamento lado-a-lado e centralização na vertical), pesquise sobre arquitetura. Compreenda o que há por trás de metodologias como BEM ou SMACSS. Escreva código previsível, escalável, manutenível e reutilizável.

Se você já está confortável com Javascript puro, também apelidado carinhosamente de Vanilla Javascript, aprenda sobre progressive enhancement, algum design pattern (eu gosto do reveal module pattern) e comunicação com o servidor.

Não aprenda nenhum framework ou biblioteca sem antes aprender o que citei acima.

Se você domina o CSS, vc consegue fazer TUDO o que alguém constrói com Sass, Less ou Stylus. Perceba que nem estou citando estes frameworks CSS com suas centenas de classes que ficam sobrando no nosso site atrapalhando a performance.

Se você domina Javascript, pode fazer TUDO o que alguém construiu com angular ou react. Tá certo. Terá um pouco mais de trabalho, é verdade. Mas e quando não existia estes frameworks? Os desenvolvedores não tinham que escrever na unha? Então é possível ainda hoje. Aliás, aqui vai um segredo ultra-secreto: Sabe o que tem por trás destes frameworks da moda? Javascript puro. Isso significa que o time por trás destes frameworks tiveram que aprender conceitos básicos de javascript como atravessar o DOM e fazer requisições AJAX, fundamentais para as SPA’s da moda.

## Já sei de tudo isso. E agora?

Se você já domina a tríade que deu origem à tudo, pode pensar em dar um passo além, escolhendo o que quer aprender a seguir.

Se me permite, gostaria de deixar minha sugestão, em ordem de prioridade:

Se você for construir sites institucionais, ou Landing Pages:

<ol>
<li>O básico de utilização de um terminal</li>
<li>GIT e github</li>
<li>Pré-processadores e Post-CSS</li>
<li>Automatizador de tarefas: Gulp e npm-script</li>
<li>Como funciona a internet. DNS, HTTP(S), TCP e SSH.</li>
<li>Comunicação RESTful.</li>
</ol>
Se você quiser atacar o mercado de aplicações web, tudo listado acima e mais:
<ol>
<li>Testes automatizados (Jest é uma boa pedida).</li>
<li>Ferramenta de bundler: Webpack (eu também preciso aprender esse troço)</li>
<li>Typescript</li>
<li>Angular, React ou Vue.js</li>
</ol>

## Conclusão

Aprenda a base. Foque de verdade em HTML semântico e acessível, CSS escalável e manutenível e Javascript performático e bem escrito. Domine-as primeiro para depois se aventurar em novos terrenos.

Não se impressione com o número de tecnologias que aparecem quase que diariamente nas vagas de trabalho front-end. Elas são passageiras. Ninguém garante que Angular, React, Sass ou qualquer outra coisa que inventarem viverão muito tempo. Duvida? É só olhar para o saudoso Jquery e o não tão saudoso assim Bootstrap.
