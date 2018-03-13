---
title: diferenças entre this, target e currentTarget
date: 2018-03-12 20:47:57
description: Saiba quando usar um ou outro
tags:
- javascript
---
Nós sabemos que a palavra reservada ```this``` no Javascript pode representar [coisas diferentes devido a sua natureza dinâmica](https://serfrontend.com/blog/entender-todas-as-formas-do-this-em-javascript/ "entender todas as formas do this em javascript"). Por esse motivo, gostaria de detalhar melhor as diferenças entre o this e duas propriedades - ```target``` e ```currentTarget``` - do objeto event.

Para iniciarmos, o código abaixo não deve ser nenhuma novidade para voce.

{% codeblock lang:js %}
btn.addEventListener('click', function(e){
  console.log(this);
  console.log(e.target);
  console.log(e.currentTarget);
})
{%endcodeblock%}

Se você testar esse código e olhar no seu console, verá que qualquer um dos três representa o mesmo objeto, que neste caso, é o próprio botão clicado.

## Mas então qual a diferença entre eles? Vamos lá

O this é quase sempre o "dono do evento", ou seja, o elemento o qual foi atrelado o método addEventListener. As duas situações onde isso não acontece é quando utilizanos em nosso código:
- o ```bind()``` para definir o escopo do ```this``` programaticamente; 
- abrimos mão do escopo dinâmico quando resolvermos adotar uma arrow function nos nossos ouvintes de evento;

Veja os dois trechos de código a seguir:

{% codeblock lang:js %}
btn.addEventListener('click', function(e){
  console.log(this);
  console.log(e.target);
  console.log(e.currentTarget);
}.bind(this))
{%endcodeblock%}

{% codeblock lang:js %}
btn.addEventListener('click', (e) => {
  console.log(this);
  console.log(e.target);
  console.log(e.currentTarget);
})
{%endcodeblock%}

Nos dois trechos de código acima o ```this``` representa um elemento diferente daquele mostrado inicialmente neste artigo. No meu caso esse objeto diferemte é o global ```window``` (pois não estou usando a diretiva ```"use strict"```). 

De qualquer forma, as propriedades ```target``` e ```currentTarget``` ainda são o mesmo objeto. 

Então porque existem duas propriedades que aparentemente são a mesma coisa? Para entender isso, precisamos olhar para o que chamamos de **delegação de eventos**.

## Utilizando a delegação de eventos

Imagine que voce tem uma tabela onde o usuário pode incluir ou remover uma ou várias linhas através da própria interface. Imagine também que em cada uma dessas linhas há um botão que pode ser clicado para executar uma ação qualquer.

Se essa tabela possui 50 linhas (portanto, 50 botões) e em cada botão há um ouvinte de evento, você terá 50 EventListeners, o que pode comprometer a performance de sua aplicação.

Quando isso acontece, uma abordagem melhor é atrelarmos o evento num elemento mais acima e então verificar quem foi o alvo da ação para decidir o que deve acontecer. Veja um exemplo:

{% codeblock lang:js %}
table.addEventListener('click', function(e){
  console.log(this); //esse é dono do evento pois removi o bind e estou usando a expressão de funcao
  console.log(e.target);
  console.log(e.currentTarget);
})
{%endcodeblock%}

No trecho de código acima, o ```currentTarget``` é sempre o "dono do evento", independente do ```bind()``` ou das arrow functions. Já o ```target``` é o último elemento na hieraquia do DOM que recebeu o evento, ou seja, no exemplo acima, é o alvo do click.

Pensando ainda no exemplo de uma tabela, o ```target``` pode ser uma tag ```tr```, ```td``` ou qualquer elemento dentro de uma ```td```, como um ```button```, por exemplo.

## Conclusão
Escrever um simples addEventListener adotando o bind() ou as arrow functions em conjunto com o conceito de delegação de eventos para melhorar a performace de sua aplicação resultará em referências distintas tanto para o ```this``` quanto para as propriedades ```target``` e ```currentTarget``` do objeto Event.

Essa foi uma dica bastante rápida mas que pode ser muito útil em algumas situações.

Aproveito para fazer o meu jabá e dizer que qualquer um dos [meus cursos de frontend](/cursos) tem um descontão se você utilizar o cupom de desconto [PROMOSITE20](/cursos).

Um abraço