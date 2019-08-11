---
title: redux com react para iniciantes
date: 2019-08-09 08:37:11
description: O que eu gostaria que alguém tivesse me dito quando comecei a estudar redux
tags:
- javascript
- frontend
- redux
- react
---
Essa é a segunda parte de um tutorial para iniciantes em redux. Vale a pena ver, se você ainda não viu, a primeira parte [redux com react para iniciantes](https://serfrontend.com/blog/redux-para-iniciantes/).

No primeiro artigo, discutimos alguns pontos importantes do redux e gostaria de recapitular.

- O Store do redux é o que gerencia o state. Ao criar um store, precisamos informar qual é a função reducer que irá manipular - ou não - os dados (também conhecidos como state).
- O state é imutável. Nenhuma alteração é feita diretamente no state. O reducer sempre precisa retornar um novo state.
- A store recebe uma action (``store.dispatch(minha-action)``), que é um objeto simples do javascript, que descreve a intensão de alterar algo no store. A action pode conter, opcionalmente, um parâmetro extra que é passado para o reducer. Comumente essa parâmetro chama-se payload em tutoriais que você pode encontrar na internet, aqui eu chamei simplesmente de 'parametro'.
- Sempre que um novo state é gerado, a função de callback em store.subscribe(callback) é executada. Nesse momento a view pode ser atualizada.

## conectando o redux ao react
O primeiro passo é instalarmos o react-redux, que é o responsável por permitir a conexão entre os dois. Se não tiver o redux instalado em seu projeto, instale-o também.

```
$ npm i react-redux
```
Eu estou prevendo que você já tem o redux instalado e já está no diretório first-redux, como fizemos no artigo anterior [redux com react para iniciantes](https://serfrontend.com/blog/redux-para-iniciantes/).

Depois de termos o react-redux pronto para uso, precisamos do Provider. Eu poderia dizer que o Provider é um *hight order component* (porque é mesmo) mas eu prefiro dizer que o Provider é o componente que permite que o react tenha acesso ao redux. 

Para importá-lo em nosso projeto, basta:
```
import { Provider } from 'react-redux' 
```

O Provider permite que o store se conecte à hierarquia de componentes a qual pertence. Mais fácil demonstrar com código:

{% codeblock lang:js %}
ReactDOM.render(<Provider>
			<App/>
		</Provider>, 
		document.getElementById('root')
);
{% endcodeblock %}

Viu? Envolvemos todo o nosso componente App no componente Provider. Agora todo o App tem acesso ao store. É só isso? Não. Ainda não. Precisamos informar qual store o Provider fornecerá para o App. Então precisamos adicionar uma prop store ao Provider. Essa prop passa a store em si.

Agora vou criar uma constante em português. Julguem-me.

{% codeblock lang:js %}
const minhaStore = createStore(reducer)
ReactDOM.render(<Provider store={minhaStore}>
			<App/>
		</Provider>, 
		document.getElementById('root')
);
{% endcodeblock %}

Estou omitindo boa parte do código que já discutimos antes e estou focando somente no que interessa.

Criei uma store usando o método createStore passando qual o reducer que deve olhar para as actions e os states. E passo essa store para o Provider.

Agora é a parte onde devemos conectar as coisas. Porém, neste ponto do artigo, eu estou enfrentando um dilema pessoal. Mostro como faz do jeito antigo ou mostro como faz direto com React Hooks? Pois bem, escolhi mostrar direto com hooks (não se preocupe com a nomenclatura, ok!). Mas saiba que antes da versão 16.8 do React era usado dois argumentos em connect() que hoje não precisamos mais usar. Eram esses argumentos chamados mapStateToProps e mapDispatchToProps. O primeiro conecta uma parte do state em props do react. Já o segundo conecta as actions do Redux em props do react. Digo isso para o caso de você achar algum desses argumentos em materiais na internet.

## Hooks
A principal motivação da inclusão dos hooks ao react é a capacidade que os hooks nos dão para controlar o estado de um componente sem a necessidade de criar um componente com classe.

Quem já fez um formulário com dois inputs ou mais sabe como é chato lidar com a alteração no input e setState ao mesmo tempo. Não é difícil, só é chato. É preciso escrever muito código para algo simples. Aliás, ponto para o Angular e o ngModel 😉. 

### useState
O método useSate (que você deve importar de 'react') cria um estado no componente e disponibiliza uma função que deve ser chamada sempre que você quiser alterar o state.

O código abaixo esclarece melhor os conceitos:


{% codeblock lang:js %}
import React, { useState } from 'react';

function meuInput {
  // cria um state name com o valor 'Daniel'. A função que deverá ser chamada para alterar o state é a setNome
  const [nome, setNome] = useState('Daniel');

  // renderizar o componente
  return (
    <div>
      <input 
        type="text"
        value={nome}
        onChange={e => setNome(e.target.value)}
      />
    </div>
  );
};

{% endcodeblock %}

### useSelector
Esse método, que também deve ser importado de 'react-redux', recebe um callback como parâmetro. Esse callback deve retornar o state novo. Se o state novo for diferente do anterior, então o componente irá renderizar o novo valor na tela. Tentei deixar a explicação simples.

O useSelector será executado sempre que houver um dispatch de uma action

### useDispatch
Muito parecido com o dispatch do redux sem react, nos dá a possibilidade de disparar uma action.

Estas são algumas possibilidades que temos usando o hooks, mas agora vamos voltar para o Redux.

Já que apresentei todos os conceitos necessários, vou construir o mesmo código que fizemos no artigo anterior, só que agora usando react-redux. Os comentários terão propósitos didáticos para reforçar o que vimos até aqui.

index.js
{% codeblock lang:js %}
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';

import { createStore }  from 'redux';

// importamos o que precisamos de react-redux
// - Provider - disponibiliza a store para toda a hierarquia de 
// componentes abaixo de <Provider>
// - useSelector executa o callback sempre que houver um dispatch. 
// O retorno deve ser o state.
// - useDispatch nos dá a chance de disparar uma action para a store
import { Provider, useSelector, useDispatch } from 'react-redux'

// não há nenhuma alteração no nosso reducer
function reducer(state = 0, action){
    let param = action.parametro || 1;
    switch (action.type) {
        case 'INCREMENTAR':
          return state + param
        case 'DECREMENTAR':
          return state - param
        default:
          return state
      }
}
// Sem alteração aqui também
const store = createStore(reducer)

// Criei um componente App em substituição do nosso element do artigo 
// anterior.
const App = function(){

  // useSelector recebe uma função de callback. Como temos apenas um 
  // state, então podemos retornar direto o mesmo state. 
  // Por isso o 'state => state', que seria o mesmo que
  // state => { return state }
  let counter = useSelector(state => state)

  // Nos dá acesso ao dispatch na store. Esse dispatch será executado 
  // no onClick da View
  const dispatch = useDispatch()

  return (
    <div> 
    <p>counter: {counter}</p>
    <button 
    	onClick={ () => dispatch({type: 'INCREMENTAR'})}> 
    	Incrementar 
    </button>
    <button 
    	onClick={ () => dispatch({type: 'DECREMENTAR'})}> 
    	Decrementar 
    </button>
    <button 
    	onClick={ () => dispatch({type: 'INCREMENTAR', parametro: 2})}> 
    	Incrementar 
    2</button>
    <button 
    	onClick={ () => dispatch({type: 'DECREMENTAR', parametro: 2})}> 
    	Decrementar 
    2</button>
    </div>
  )
}

// Tudo que está abaixo do Provider tem acesso ao store
ReactDOM.render( <Provider store={store}>
  <App />
</Provider>, document.getElementById('root'));
{% endcodeblock %}

Esse código ficou funcional. Claro que tem muitas coisas que poderíamos melhorar, mas quis deixar as coisas o mais simples possível. Contudo, só faltou um detalhe: digamos que eu tenha dois states. Dessa maneira, teríamos dois reducers. Como proceder?

A primeira coisa que temos que saber é que a função createStore aceita somente um reducer. Por conta disso, existe um método muito conveniente no redux chamado combineReducers.

Ele aceita um objeto como parâmetro, e cada propriedade desse objeto é um reducer. Digamos que agora temos o counterReducer, muito parecido com o que fizemos, e o nameReducer. Logo, poderíamos ter o seguinte código:

{% codeblock lang:js %}
function counterReducer(state = 0, action){
    let param = action.parametro || 1;
    switch (action.type) {
        case 'INCREMENTAR':
          return state + param
        case 'DECREMENTAR':
          return state - param
        default:
          return state
      }
}
function nameReducer(state = '', action){
    let param = action.parametro || state;
    switch (action.type) {
        case 'ALTERAR':
          return param
        default:
          return state
      }
}
// Combinamos os dois reducers em um
const store = createStore(combineReducers({
	counter: counterReducer,
	name: nameReducer
}))
{% endcodeblock %}

Agora o state não guarda apenas um valor, mas sim um objeto. Esse objeto possui duas propriedades (counter e name) que foram os nomes que demos ao passar o objeto para combineReducers().

Isso significa que antes, para pegar um valor do state, fazíamos ``let counter = useSelector(state => state)``. Agora esse código deve mudar, pois cada valor está dentro de sua respectiva propriedade.

{% codeblock lang:js %}
let counter = useSelector(state => state.counter)
let name = useSelector(state => state.name)
{% endcodeblock %}

Vamos testar?

Mudei o nome do componente App para Counter e acrescentei o Name. Segue código comentado

{% codeblock lang:js %}
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';

// Importei o combineReducers
import { createStore, combineReducers }  from 'redux';
import { Provider, useSelector, useDispatch } from 'react-redux'

// Criei dois reducers
function counterReducer(state = 0, action){
  let param = action.parametro || 1;
  switch (action.type) {
      case 'INCREMENTAR':
        return state + param
      case 'DECREMENTAR':
        return state - param
      default:
        return state
    }
}
function nameReducer(state = 'Daniel', action){
  let param = action.parametro || state;
  switch (action.type) {
      case 'ALTERAR':
        return param
      default:
        return state
    }
}
// Combinamos os dois reducers em um só
const store = createStore(combineReducers({
  counter: counterReducer,
  name: nameReducer
}))


const Counter = function(){

  // agora a função de callback, que é executada em cada dispatch, 
  // deve retornar state.counter e sate.name.
  let counter = useSelector(state => state.counter)
  let name = useSelector(state => state.name)

  const dispatch = useDispatch()

  // repare que, apesar de estar definido em outro componente, temos 
  // acesso ao name que está no Redux
  return (
    <div> 
    <p>counter: {counter} do {name}</p>
    <button 
    	onClick={ () => dispatch({type: 'INCREMENTAR'})}> 
    		Incrementar 
    </button>
    <button 
    	onClick={ () => dispatch({type: 'DECREMENTAR'})}> 
    		Decrementar 
    </button>
    <button 
    	onClick={ () => dispatch({type: 'INCREMENTAR', parametro: 2})}> 
    		Incrementar 
    2</button>
    <button 
    	onClick={ () => dispatch({type: 'DECREMENTAR', parametro: 2})}> 
    		Decrementar 
    2</button>
    </div>
  )
}

const Name = function(){
  let name = useSelector(state => state.name);
  const dispatch = useDispatch();  

  return (
    <div> 
      <input
        type="text"
        value={name}
        onChange={ (e) => dispatch({
        	type: 'ALTERAR', 
        	parametro: e.target.value})}
      />
    </div>
  )
}
ReactDOM.render( <Provider store={store}>
  <Counter />
  <Name />
</Provider>, document.getElementById('root'));
{% endcodeblock %}

**Importante:** viu como é facil a comunicação entre componentes? Repare que o componente Counter tem acesso ao valor name que foi definido em Name sem precisar criar props e criar um componente pai de todos só para armazenar o state. Lindo, não!?


## Conclusão 
É claro que dá para melhorar bastante. Dá pra dividir os reducers em arquivos separados e trabalhar com import e export. Dá pra criar uma função que retorna o objeto action. Dá também para criar um diretório só para armazenar as actions e outro diretório só para armazenar os reducers. Tem muita coisa que poderíamos fazer para não ficar num arquivo index.js gigante. Mas de qualquer forma, creio que meu objetivo foi cumprido, que foi desmistificar o Redux, que afinal de contas, nem é tão difícil assim.








