---
title: 'maneiras de lidar com arrays, objetos e arrays-like - parte 1'
date: 2018-07-04 20:28:12
description: Aprenda iterar sobre arrays, objetos e arrays-like com javascript..
tags:
- javascript
---
Antes de falar como percorrer os elementos de objetos, vou focar em arrays e arrays-like.

Os arrays-likes são estruturas que podem ter seus elementos acessados através de seu índice mas não possuem alguns métodos úteis que as arrays possuem, como push, slice, splice etc. Exemplos de arrays-like são objetos do DOM e o objeto interno arguments de uma função.

Há várias maneiras de percorrer os elementos de uma array. Normalmente usamos loops simples como o loop for, while ou do ... while.

{% codeblock lang:js %}
const arr = ["maria", "jose", "joão"];

while(arr.length){
  console.log(arr.pop());
}
{% endcodeblock %}

Ao final do loop while acima a arr será uma array vazia. Foi um exemplo simples e pouco prático pra demonstrar um pouco de código.

Contudo, podemos iterar sobre arrays sem precisarmos escrever loops for ou até mesmo while. Nós podemos utilizar métodos de arrays para percorrer os seus elementos e invocar uma função de callback para cada um dos elementos.

O primeiro método que veremos é o forEach(), que executa a função passada por parâmetro em cada elemento da array.

Reescrevendo o exemplo acima, teríamos:

{% codeblock lang:js %}
const arr = ["maria", "jose", "joão"];

arr.forEach( nome => console.log(nome) )
{% endcodeblock %}

Nesse exemplo executo uma arrow function em cada elemento da array e o mostro no console. Sem grandes problemas.

O segundo método que veremos é o map(), que executa a função de callback passada por parâmetro em cada elemento e retorna uma nova array. No exemplo abaixo, vamos criar uma array de números inteiros a partir de uma array de números decimais.

{% codeblock lang:js %}
const arrFloat = [2.545, 10.887, 3.4541];
const arrInt = arrFloat .map( n => parseInt(n, 10))
console.log(arrFloat); //[2.545, 10.887, 3.4541]
console.log(arrInt); //[2, 10, 3]
{% endcodeblock %}

Bacana! Vimos que podemos iterar sobre arrays com loops tradicionais ou alguns métodos próprios para isso. Agora vamos ver como faríamos para iterar sobre arrays-likes. Para isso, vou criar um NodeList utilizando a API querySelectorAll

{% codeblock lang:html %}
<nav> 
	<a href="#">link 1 </a> | 
	<a href="#">link 2 </a> | 
	<a href="#">link 3 </a> 
</nav>

<script> 
	var $links = document.querySelectorAll('a'); 
</script>
{% endcodeblock %}

Agora vou percorrer essa NodeList utilizando o loop for

{% codeblock lang:js %}
for(let i = 0; i < $links.length; i++){
  console.log($links[i].textContent)
}
{% endcodeblock %}

Funcionou. O código acima mostra no console os textos de cada um dos links.

Digamos que, para demonstrar, eu queira obter uma array contendo as strings de cada um dos links. Poderíamos pensar em algo como:

{% codeblock lang:js %}
const linksStr = $links
		.map( text => text.textContent );
{% endcodeblock %}

A ideia é percorrer os elementos da NodeList e, para cada elemento, retornar o seu textContent e armazenar em linksStr. Porém isso não funciona, pois uma NodeList (que é um array-like) não possui o método map(). 

Então como resolver? Da maneira antiga, teríamos que "pegar emprestado" o método map do prototype da array da seguinte forma:

{% codeblock lang:js %}
const linksStr = Array.prototype.map.call($links, text => text.textContent);
{% endcodeblock %}

Na linha acima, eu acesso direto o método map do protótipo da array e executo - com o call() - passando qual será o this - $links - e passando a função que será executada - text => text.textContent.

Essa era a única forma de chegarmos nesse resultado antes da ES2015. Eu disse, antes.

Utilizar o prototype pode parecer um pouco confuso para iniciantes. A boa notícia é que não precisamos recorrer ao protótipo para termos resultados parecidos com o exemplo acima. 

Com a chegada da ES2015 (ES6 para alguns), temos maneiras mais elegantes de chegarmos no mesmo resultado. Veremos algumas delas

## Array.from()

Array.from() cria uma array a partir de outra array, de uma array-like ou um objeto iterável. Veja um exemplo:

{% codeblock lang:js %}
const linksStr = Array
		.from($links)
		.map(text => text.textContent);
{% endcodeblock %}

A linha acima transforma o NodeList $links em uma array pura - Array.from() - e depois percorre cada elemento e retorna o respectivo textContent. Muito mais elegante, não é mesmo?

## Array.of() e spread operator (...)

Array.of() cria uma array contendo quantos argumentos forem passados. Exemplo: Array.of(1,2,3) retorna [1,2,3]. 
Já o spread operator "espalha" os elementos de uma array ou array-like passando-os como argumentos separados para uma função. Exemplo:

{% codeblock lang:js %}
const linksStr = Array
		.of(...$links)
		.map(text => text.textContent);
{% endcodeblock %}

O código acima "espalha" cada um dos elementos do DOM - ...$links - e os passa como argumentos separados para a função Array.of(). Depois efetua o .map() normalmente como nos exemplos anteriores.

Se você achou o código acima muito verboso e quer digitar menos, não se preocupe, seus problemas acabaram:

{% codeblock lang:js %}
const linksStr = [...$links]
		.map(text => text.textContent);
{% endcodeblock %}

[...$links] simplesmente cria uma array de verdade com base no spread operator da NodeList. Fantástico! 

Provavelmente existem outras formas de chegarmos no mesmo resultado, mas estas que eu passei são suficientes para iterarmos sobre arrays e arrays-like sem ficar utilizando loops ou até mesmo criando variáveis desnecessárias.

No próximo artigo irei explorar sobre a iteração em objetos. Aguarde!


## Bônus

Se você ficou com a pulga atras da orelha sobre o motivo de utilizar Array.of(), segue um código de exemplo:
{% codeblock lang:js %}
//cria uma array com três posições vazias, enquanto:
const arr = new Array(3);

//cria uma array com uma única posição, contendo o número 3. Até onde eu sei, essa é a única diferença entre new Array() e Array.of().
const arr = Array.of(3);
{% endcodeblock %}

Forte abraço e até a próxima