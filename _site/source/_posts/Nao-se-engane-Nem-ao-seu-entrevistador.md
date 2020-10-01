---
<<<<<<< HEAD
title: Não se engane. Nem ao seu entrevistador
=======
title: Não se engane Nem ao seu entrevistador
>>>>>>> 562b4c8da066a624eec84e03224a9f9f8a3c6197
date: 2020-10-01 20:01:29
tags:
- carreira
- entrevista
---

# Não se engane. Nem ao seu entrevistador.

Trabalho como consultor desde meados de 2019 e logo depois que iniciei a jornada na nova empresa fui solicitado para ajudar com algumas entrevistas técnicas.

Para realização destas entrevistas há um roteiro a ser seguido: primeiro nos apresentamos, depois falamos um pouco da empresa, a seguir pedimos a apresentação do aspirante à vaga, e depois passamos um teste prático e outro teórico, para saber se o candidato ou candidata sabe mesmo tudo o que apontou em seu currículo.

Durante a entrevista nós vamos preenchendo uma planilha com alguns pontos importantes que já foram pré-estabelecidos. Pontuando de 0 a 5 para cada tópico já planilhado. Essas seções são sempre com dois entrevistadores.

Depois da entrevista propriamente dita, agradecemos o tempo da pessoa e começamos um processo interno onde vamos discutir alguns pontos anotados no decorrer da conversa e, depois de chegarmos num consenso, formatamos tudo num documento único e encaminhamos para o RH da empresa. A nossa parte foi concluída.

Eu escrevi tudo isso para te dar um contexto geral e te dar algumas dicas do que fazer (ou não fazer) nas suas entrevistas técnicas. Eu não estou aqui ditando regras, mas sim sugerindo ações com base na nossa percepção no momento de avaliar um candidato ou candidata.

## 1 – Não minta no currículo

Certa vez fui solicitado para entrevistar uma pessoa para um cargo alto, acima de sênior, que aqui chamamos arquiteto. Quando olhei o currículo da pessoa confesso que fiquei bem intimidado e pensei: "quem sou eu pra analisar essa pessoa? Ela que deveria me avaliar". Mas essa expectativa caiu logo por terra quando identificamos que a pessoa não tinha conhecimentos básicos de javascript. Sim, havia muita força de vontade mas para o cargo de arquiteta realmente não havia condições. Sugerimos então contratar a pessoa como júnior. Identificamos potencial de crescimento e vontade de evoluir, mas como a pessoa tinha se candidatado para uma vaga com alto grau de senioridade, o processo foi interrompido, infelizmente.

A lição aqui é óbvia. Não minta no currículo. Você pode queimar uma oportunidade de iniciar a carreira numa boa empresa. Seja transparente.

## 2 – Não minta no teste

Essa também é óbvia. Se você não souber algo na avaliação técnica, não tente enganar o entrevistador. Ele vai perceber sua tentativa de enganá-lo e acredite, a impressão é péssima. Lembre-se: não há nada de errado em não saber algo. Aliás, ninguém sabe tudo. E o entrevistador nem espera que você saiba tudo. Ele só está seguindo um protocolo para saber em que situação você está para não te colocar em furada, te colocando numa vaga a qual você não vai corresponder. Não minta. É muito melhor ser sincero e falar que não sabe.

Quando isso acontece comigo quando eu sou o entrevistador e a pessoa do outro lado da mesa ou do Skype responde com sinceridade que não sabe, fazemos questão de explicar. Ela podia não saber antes, mas agora ela já sabe.
Um exemplo recente. Perguntamos para um candidato: o que faz a seguinte regra de CSS?

{% codeblock lang:css %}
p {
  white-space: nowrap; 
  width: 50px; 
  overflow: hidden;
  text-overflow: ellipsis; 
}
{% endcodeblock %}

A resposta: deixar o texto arredondado.

Claramente ele não tinha ideia do que estava falando e arriscou. Se ele estivesse certo passaria despercebido, mas como passou muito longe disso, a sensação que nos passou é que estava tentando nos enganar.

Se ele tivesse sido sincero, certamente minha resposta seria: "não se preocupe. Isso é muito específico mesmo. Essas propriedades em conjunto fazem esconder parte do texto e coloca reticências quando for necessário... É isso".

Viu! Ninguém nasceu sabendo e não há nada de errado em não saber algo. O entrevistador quer ter uma ideia geral do seu conhecimento e não aplicar uma prova onde você só passa se tirar mais que 70%.

## 3 – Estude a base

Já fiz algumas entrevistas para front-end com angular ou react. Alguns candidatos me deram verdadeiras aulas quando perguntei sobre questões específicas do Angular ou React. 

Uma vez perguntei sobre o padrão Observable e saí da entrevista recompensado pela resposta do candidato.

Mas quando perguntamos sobre coisas mais básicas, a resposta era quase sempre: "isso eu nunca fiz", "nunca precisei fazer dessa forma", "a tecnologia x resolve isso pra mim".

Ele não estava totalmente errado, mas é muito importante saber a base primeiro. Se você sabe fazer uma requisição com async /await, seja curioso para saber qual o problema esse async / await resolve. Se você tirá-lo da sua requisição, o que acontece?

Ter esse conhecimento de base irá te ajudar de muitas maneiras no dia-a-dia. Acredite.

Mesmo que você já aprendeu front-end com Angular / React / Vue / Svelte, dedique um tempo para aprender o HTML, o CSS e o Vanilla Javascript.

### Mais um "causo" para tentar te convercer:

Mesmo que estamos procurando alguém para trabalhar com React ou Angular, a parte prática da avaliação é com javascript puro. Nós não pedimos para a pessoa desenvolver um sistema inteiro. Nós queremos apenas perceber o nível de lógica da pessoa que está sendo avaliada. 

Os itens abaixo são exemplos de questões que pedimos em entrevista. Faça uma auto-avaliação, se quiser.

Desenvolva uma função que recebe um array de strings e devolve a maior string encontrada. Se houver mais de uma palavra com o mesmo número de letras, devolve a primeira encontrada.

Crie uma função que recebe uma string e devolve as palavras invertidas, ex: Se receber "Hello World!" deve retornar "World! Hello".

Crie uma função que recebe um array de números e retorna quantas vezes os números se repetiram.

Viu! Javascript puro. Não estamos interessados em saber se a pessoa faz um CRUD com o seu framework favorito. Queremos saber se ela tem o mínimo de lógica para se virar bem com qualquer framework. A ferramenta pode mudar no futuro. Mas o raciocínio lógico é seu, ninguém muda.

## 4 – Não se subestime

Já fiz entrevistas com pessoas com bom conhecimento técnico que seria muito bem encaixado para a vaga em questão, mesmo que a pessoa não tenha respondido tudo corretamente. Como eu falei antes, não há problema em não saber.

No decorrer da entrevista a pessoa demonstrou conhecimento satisfatório, mas no fim da conversa a pessoa se demonstrou com pouca confiança em si mesma. 

Teve um candidato que foi muito bem nas questões teóricas e no final ele falou que não estava preparado para o cargo de advanced. Ele disse que poderia entrar como júnior. Eu olhei para o outro entrevistador e tivemos o mesmo pensamento. Na mesma hora dissemos ao candidato que ele estava sim preparado tecnicamente para um cargo mais elevado. Ele então demonstrou muita satisfação em ter esse feedback imediato. E o mais importante é que estávamos sendo sinceros.

É obvio que não há nenhum problema em ser júnior. Todo mundo teve que começar a carreira um dia e dificilmente já começou como tech leader (a não ser que a pessoa é filha do dono. Nesse caso, ela MERECEU rs).

A dica é: diga o que você sabe e quando não souber de algo, deixe isso claro. Se for solicitado para você se autoavaliar, faça. Caso contrário, deixo isso para o entrevistador.

## 5 – Não tenha medo de perguntar como se saiu
Se quiser ter uma ideia se foi bem ou não na entrevista, pode perguntar. Não é mal nenhum em tentar obter esse feedback na mesma hora e dificilmente o entrevistador vai ficar chateado em te dar uma posição inicial.
Pelo contrário. Isso demonstra atitude e pode contar um pontinho a mais 😊

## Conclusão

É isso pessoal. Espero que este artigo te ajude de alguma forma. Lembre-se: 

1 – Ninguém nasceu sabendo
2 - Seja transparente
3 - Estude a base
