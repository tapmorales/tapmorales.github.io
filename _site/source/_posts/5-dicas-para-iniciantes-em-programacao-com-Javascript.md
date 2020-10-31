---
title: 5 dicas para iniciantes em programação com Javascript
date: 2020-10-31 15:27:36
tags:
  - javascript
---

Quando estamos ingressando na área de programação, alguns conceitos fundamentais ficam bem obscuros na nossa mente. Por exemplo, quando estamos iniciando na carreira, termos como "linguagem fortemente tipada" ou "instâncias de classes", por mais que sejam o arroz com feijão para quem já trabalha na área a algum tempo, não são tão claros para quem está iniciando.

Este artigo é voltado para as pessoas que estão começando na área. Pretendo explicar de forma simples alguns termos que parecem ser complexos, mas que na verdade são bem mais simples do que parecem.

Simbora?

## 1 - Tipo de dados ou datatypes
Antes de falarmos sobre tipos de dados, vamos valar de variáveis.
Uma variável é um lugar na memória onde podemos armazenar valores, certo? Mas podemos armazenar qualquer valor em uma varíavel? Em javascript, sim.

Podemos armazenar uma string, um número, um booleano, undefined, uma array, um objeto, uma função, um symbol. Enfim, em javascript podemos armazenar qualquer valor numa variável. Podemos inclusive armazenar valores de tipos diferentes na mesma variável. Mas você não vai querer fazer isso, acredite.

Ou seja, em javascript, se fizermos:

{% codeblock lang:js %}
let foo = null
foo = "texto"
foo = 10
{% endcodeblock %}

Não haverá qualquer problema de sintaxe e o código vai funcionar sem problemas, mas não devemos trocar deliberadamente os tipos de dados que armazenamos para não obtermos resultados indesejados.

Quando falamos "tipos de dados" em programação, estamos nos refereindo sobre tipos de valores que podemos armazenar numa variável ou num parâmetro de função.

Em javascript há 7 tipos primitivos:

- string
- number
- boolean
- null
- undefined
- symbol (somente no ES2015 +)
- bigint (sinceramente, nunca precisei usar, e não é incomum achar em sites de renome que há apenas 6 tipos primitivos em javascript, e não 7).

Em javascript, tudo que não é um valor primitivo, é objeto.

Uma Array? É objeto. 

Uma function? É um objeto - com a incrível capacidade de ser executado mas ainda assim, é um objeto. 

Um Set? Objeto também. 

Um Object? Esse não precisa nem falar né? 🤪

Então quando você ouvir falar em tipos de dados saiba que é simplesmente uma maneira de identificar que tipo de valor uma informação é.

**Importante**: Há diferentes tipos em diferentes linguagens. Mas em javascript temos os 7 tipos primitivos e mais os objetos.

A próxima dica é quase que uma continuação da dica número 1. Eu estou falando de: 

## 2 – Linguagem fortemente ou fracamente tipada.

Em algumas linguagens de programação precisamos informar qual o tipo de dado que uma variável irá armazenar no momento de sua declaração. 

Por exemplo: em typescript, temos a seguinte sintaxe:

{% codeblock lang:ts %}
let meuTexto: string
{% endcodeblock %}

Ou seja, falamos que esta variável aceita receber apenas strings.

Nesse caso específico não é uma boa prática deixar da forma acima devido a um conceito chamado "inferência de tipos". Ou seja, em typescript, basta criar a variável normalmente com o seu valor que o typescript irá saber que se trata de uma variável que aceita apenas strings.

Veja outro exemplo em typescript:

{% codeblock lang:ts %}
function isOdd(n: number): boolean { return n % 2 }
{% endcodeblock %}

Repare que estamos definindo o tipo de parâmetro que a função isOdd aceita além do tipo de retorno. Quando fazemos isso, podemos dizer que estamos tipando o parâmetro e o retorno da função.

Há linguagens que essa tipagem explicita é obrigatória, portanto, dizemos que é fortemente tipada. Já o javascript, que é uma linguagem fracamente tipada, não nos obriga definir os tipos para nada.

Para tornar o desenvolvimento com javascript um mais seguro com relação à tipagem, nasceu o Typescript, que é um superset que vai transformar um código typescript (opcionalmente tipado) em javascript (fracamente tipado)
 
## 3 - Orientação à objetos

Não, orientação à objetos **não é uma forma de criar softwares arrastando objetos na tela** como disse um "especialista" que deu entrevista pra rede globo.

<iframe width="560" height="315" src="https://www.youtube.com/embed/EK49T77VQOQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Uma linguagem que trabalha com o paradigma orientação de objetos é uma linguagem que trabalha com alguns conceitos onde o pilar nesse tipo de programação é que tudo é um objeto. E por objeto entende-se um conjunto de características (propriedades) e funções (métodos).

Mas se tudo é objeto, o que são as classes? Pois bem, uma classe é como se fosse uma função que devolve um objeto com propriedades e métodos pré-definidos.

No javascript, por exemplo, quando fazemos:

{% codeblock lang:js %}
const hoje = new Date()
{% endcodeblock %}

Estamos criando um objeto (chamado hoje) a partir de uma classe (Date). Esse objeto possui várias propriedades e métodos, como getDate(), getFullYear() e mais um monte de métodos. 
Repare o que aconteceu aqui: criamos um objeto novinho com várias coisas pré-definidas.

Numa linguagem orientada a objetos há a possibilidade de criarmos as nossas próprias classes que, ao serem utilizadas, vão devolver objetos.

Exemplo clássico:

{% codeblock lang:js %}
const eu = new Pessoa()
{% endcodeblock %}

Ou seja, a classe Pessoa cria e retorna um objeto, que agora está armazenado na const eu.

## 4 - DOM

Também respondo muitas dúvidas sobre esse tal de DOM.

Entendê-lo não é complicado. DOM (Document Object Model) nada mais é do que a representação em formado de objetos daquilo que o usuário vê na tela, ou seja, do html. Sempre que você digita "document." Está, na verdade, acessando o DOM.

A confusão se dá quando elementos do DOM são armazenado em variáveis. Se esse é o seu caso, não se preocupe. É normal.

Uma dica que posso te dar é criar o seu código primeiro sem armazenar nada em variável.
Espalhe document.getElementById, document.querySelector etc pelo seu código. Depois, tente colocar elementos repetidos numa variável e ir substituindo onde necessário. Lembra que em javascript uma variável pode armazenar qualquer valor? Pois bem, isso inclui referencias do DOM.


## 5 - A ordem importa.

Eu vejo muita gente que está iniciando na área errar nesse ponto.
Imagine um formulário com um input e um botão. Imaginou? Agora veja o seguinte código.

{% codeblock lang:js %}
let valor = document.querySelector("input").value
document.querySelector("form").addEventListener("submit", function(e){
	e.preventDefault()
	console.log(valor)
})
{% endcodeblock %}

O que vai acontecer quando o usuário digitar um valor no input e pressionar o botão? Se respondeu que não será mostrado nada no console, parabéns! É isso mesmo.
Esse código está mal pois no momento que o código é executado o input estará vazio e "valor" armazenará uma string vazia.

Mesmo que depois o usuário digite algo no input, esse "algo" não será refletido na variável. Por isso nada será exibido no console. O que queremos fazer, na verdade, é guardar o texto digitado na variável apenas quando o usuário clicar no botão, e não antes.
É isso por hoje. Espero que tenham curtido. 

### Dica extra: 

Não se esqueça que um sinal de igual é operador de atribuição e dois ou três iguais é operador de comparação.

{% codeblock lang:js %}
let isValid = false
if(isValid = true){
	console.log("é válido")
}
{% endcodeblock %}

Não só vai executar o trecho do bloco if como também vai inserir true na isValid que antes era false.

Cuidado com isso. Não cometa essa falha terrivelmente amadora.

PS: Fiz exatamente isso no trabalho poucos dias antes de escrever esse artigo. Hahaha. Somos humanos. Cometemos falhas.
