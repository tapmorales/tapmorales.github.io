---
title: 'maneiras de lidar com arrays, objetos e arrays-like - parte 2'
date: 2018-10-04 08:47:23
description: Aprenda iterar sobre as propriedades de um objeto em Javascript..
tags:
- javascript
---
Na [primeira parte desse artigo](/blog/maneiras-de-lidar-com-arrays-objetos-e-arrays-like-parte-1/) falamos sobre algumas maneiras de iterar sobre arrays e arrays-like além dos loops tradicionais.

Nessa segunda parte iremos discutir algumas maneiras de iterarmos sobre as propriedades de um objeto. 
Em todos os exemplos de códigos no decorrer deste artigo, levarei em consideração o objeto literal criado (desculpe a falta de imaginação para elaborar os exemplos):

{% codeblock lang:js %}
const mamifero = {
  alimento: 'leite',
  locomove: null
}
const gato = {
  locomove: '4 patas',
  som: 'miau'
}
const cachorro = {
  locomove: '4 patas',
  som: 'au-au'
}
{% endcodeblock %}

Agora vou vincular os devidos protótipos

{% codeblock lang:js %}
Object.setPrototypeOf(gato , mamifero )
Object.setPrototypeOf(cachorro , mamifero )
{% endcodeblock %}

O que eu fiz aqui foi falar que gato e cachorro herdam as propriedades de mamifero através de sua cadeia de protótipos.
Na prática isso quer dizer que <code>gato.alimento</code> irá retornar "leite". Já <code>gato.locomove</code> irá retornar "4 patas" e não null, pois esta propriedade foi substituída no próprio objeto gato.

Agora que temos nossos objetos de exemplos criados, vamos ao que interessa e iterar sobre suas propriedades.

A maneira mais simples e mais verbosa de olharmos para as propriedades de um objeto é utilizando o loop for ... in. Veja no exemplo:

{% codeblock lang:js %}
for (let propriedade in gato){
  console.log( propriedade )
}
{% endcodeblock %}

Isso irá mostrar no console a saída:
locomove
som
alimento

Ou seja, serão mostrados no console os nomes das propriedades, e não os seus valores. O exemplo abaixo mostra como listar também os respectivos valores

{% codeblock lang:js %}
for (let propriedade in gato){
  console.log( propriedade, 'possui valor: ', gato[propriedade] )
}
{% endcodeblock %}

Compare a saída no console e veja a diferença.

Você pode ter percebido que além das propriedades do objeto gato, o loop for ... in mostrou também as propriedades herdadas de mamifero. Se não quisermos que isso aconteça, basta perguntarmos dentro do loop se a propriedade pertence ao próprio objeto, assim:

{% codeblock lang:js %}
for (let propriedade in gato){
  gato.hasOwnProperty(propriedade) && console.log( propriedade, 'possui valor: ', gato[propriedade] )
}
{% endcodeblock %}

Esse curto-circuito está aí apenas para mostrar que não precisamos necessariamente de um if. Mas o resultado é o mesmo de:

{% codeblock lang:js %}
for (let propriedade in gato){
  if(gato.hasOwnProperty(propriedade)){
   console.log( propriedade, 'possui valor: ', gato[propriedade] )
  }
}
{% endcodeblock %}

Um pouco mais verboso mas com o mesmo resultado final.

Se você digitar no console gato.toString() verá que a saída não é lá muito amigável. Que tal se nós sobrescrevermos o método toString() dentro de gato

{% codeblock lang:js %}
const gato = {
  locomove: '4 patas',
  som: 'miau',
  toString: function(){
    return 'eu sou um objeto gato'
  }
}
{% endcodeblock %}

O comando <code>gato.toString()</code> irá mostrar uma mensagem muito mais amigável no console, mas isso nos trouxe um problema, o loop for ... in está nos mostrando no console a implementação de toString(). 
Umas das maneiras de mostrar apenas as propriedades seria efetuar um typeof em cada propriedade e mostrar apenas as que são strings, números, booleanos, null e undefined. Mas veremos um jeito melhor.

## Propriedades enumeráveis.

Todas as propriedades que criamos normalmente em um objeto são criadas com uma flag interna chamada Enumerable setada para true. Na prática, isso quer dizer que estas propriedades são listadas num loop for ... in, por exemplo.

A boa notícia é que há uma maneira de criar uma propriedade não enumarada. Isso se dá através de um método de Object chamado defineProperty(). Vamos ao código:

{% codeblock lang:js %}
Object.defineProperty(cachorro, 'toString', {
  enumerable: false, 
  writable: false,
  value: function(){
  return 'eu sou um objeto gato'
}
})
{% endcodeblock %}

Agora ao executarmos o mesmo loop no objeto cachorro, veremos um resultado levemente diferente:

{% codeblock lang:js %}
for (let propriedade in cachorro){
  if(cachorro.hasOwnProperty(propriedade)){
   console.log( propriedade, 'possui valor: ', cachorro[propriedade] )
  }
}
{% endcodeblock %}

Perceba que agora a implementação de toString não é mais mostrada no console.

O método defineProperty recebe três parâmetros: objeto que queremos inserir a propriedade, o nome da propriedade, um objeto descritor. Para saber quais outras configurações podemos utilizar, [dê uma olhada na documentação](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)

## keys(), values() e entries()

Alguns métodos de Object podem tornar nosso código mais sucinto. O primeiro que veremos é o keys().

Esse método retorna um array contendo as propriedades do próprio objeto (descartando, portanto, a cadeia de protótipos) se esta propriedade for enumerável, obviamente.

{% codeblock lang:js %}
Object.keys(gato) //irá retornar ["locomove", "som", "toString"] 
Object.keys(cachorro) //irá retornar apenas ["locomove", "som"]
{% endcodeblock %}

Repare que em nenhum dos casos a propriedade alimento foi listada, pois esta não está presente no objeto em si.

Já o método values() retorna os valores, e não as propriedades. Veja:

{% codeblock lang:js %}
Object.values(cachorro) //irá retornar ["4 patas", "au-au"].
{% endcodeblock %}

Você deve ter percebido que enquanto o loop for ... in itera sobre as propriedades enumeráveis próprias e herdadas, keys() e values() iteram somente sobre as propriedades enumeráveis próprias, não as herdadas. Essa mesma característica acontece com entries(), que veremos a seguir.

```Object.entries()``` retorna um array onde cada elemento é outra array contendo a chave no índice 0 e o valor no índice 1. Veja o exemplo:

{% codeblock lang:js %}
Object.entries(cachorro) //irá retornar a seguinte Array:

//[
//  ["locomove", "4 patas"],
//  ["som", "au-au"]
//] 
{% endcodeblock %}

Uma observação importante é que nem values() nem entries() funcionam nativamente em browsers antigos

## Conclusão

Vamos ver agora como podemos tirar vantagem de keys() (melhor suporte em navegadores antigos), para iterar sobre o objeto cachorro e mostrar suas propriedades no console

{% codeblock lang:js %}
for (let propriedade of Object.keys(cachorro)){
  console.log( propriedade, 'possui valor: ', cachorro[propriedade] )
}
{% endcodeblock %}

Você pode ter percebido que utilizei um outro tipo de loop, o for ... of. Sabemos que ```Object.keys()``` devolve uma array e que o uso do for in em arrays é uma má prática. O ES6 introduziu portanto o loop for ... of que nos permite iterar sobre o que chamamos de um "iterável". Mas isso é assunto para um próximo artigo.

Um abraço

<code> &lt;jaba&gt; </code>
Garanta <b>83% de desconto</b>  <small>( de <del>R$ 114,99</del> por apenas <b>R$ 20,00</b>)</small> no meu curso de [Javascript Completo do iniciante ao mestre](https://www.udemy.com/javascript-completo-2018-do-iniciante-ao-mestre/?couponCode=PROSITE23) adquirindo-o pelo meu blog. [Compre agora](https://www.udemy.com/javascript-completo-2018-do-iniciante-ao-mestre/?couponCode=PROSITE23) ou conheça [outros cursos](/cursos).
<code> &lt;/jaba&gt; </code>

