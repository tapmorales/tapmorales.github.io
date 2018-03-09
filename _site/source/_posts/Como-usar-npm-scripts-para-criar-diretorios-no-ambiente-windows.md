---
title: Como usar npm-scripts para criar diretórios no ambiente windows
date: 2018-03-07 11:39:37
tags:
- npm-script
- workflow
- frontend
---
Esse post nem é um post de verdade, mas sim uma dica rápida.
Meu objetivo é mostrar como é possível criar diretórios a partir do npm-scripts no ambiente Windows.

## Por que este post foi escrito?

Na primeira versão do <a href="https://www.udemy.com/ferramentas-front-end-git-npm-script-gulp-e-sass/?couponCode=PROMOSITE20" title="Torne-se um desenvolvedor front-end">projeto construído para este curso</a> eu utilizei o <a href="https://bower.io/" target="_blank">bower</a> como gerenciador de dependência do lado do front-end. Contudo, após finalizar a gravação de todas as aulas, resolvi voltar alguns commits anteriores e criei uma nova branch para regravar algumas aulas, substituindo o bower pelo npm.

Para que as demais video-aulas continuassem a fazer sentido, criei um npm-script para copiar as dependências de node_modules para dentro de components. Fazendo isso, não precisaria regravar todas as aulas, pois a estrutura de pastas seria a mesma. Assim quem fosse assistir na sequência não se sentiria perdido.

No final, este foi o npm-script criado:

{% codeblock lang:js %}
"scripts": {
    "postinstall": "cp -r node_modules/bootstrap/dist src/components/bootstrap/ &amp;&amp; cp -r node_modules/font-awesome/css src/components/font-awesome/ &amp;&amp; cp -r node_modules/font-awesome/fonts src/components/font-awesome/",
    "gulp": "gulp"
  },
<{% endcodeblock %}

Tudo funcionou perfeitamente pois eu já tinha em meu projeto a estrutura de pastas criadas previamente e não me atentei ao detalhe de que, se essa estrutura de pasta não existisse, tudo falharia.

## É só criar a estrutura de pasta usando mkdir -p

Pois é. Deveria funcionar. Mas não é assim que acontece no Windows. 

Se voce digitar no seu terminal algo:
{% codeblock lang:js %}
$ mkdir -p meu/caminho/que/nao/existe
<{% endcodeblock %}

Você verá que todo o path foi criado justamente por causa da flag -p.

Mas se você tentar fazer o mesmo no npm-script e rodar o comando, verá um erro. 

## E como resolver.

Para resolver essa questão utilizei um módulo do node chamado mkdirp. Este módulo permite criarmos diretórios se for necessário. Sua utilização é muito fácil. Primeiro, vamos instalar o módulo e registrá-lo como dependência em nosso package.json.
{% codeblock lang:js %}
$ npm i mkdirp -D
<{% endcodeblock %}

Depois, basta eu acrescentar um script para criar os diretórios necessários antes de tentar copiar os arquivos da pasta node_modules, Assim:
{% codeblock lang:js %}
"postinstall": "mkdirp src/components/bootstrap/ src/components/font-awesome/",
<{% endcodeblock %}

Segue o código inteiro para sua referência:
{% codeblock lang:js %}
"scripts": {
    "test": "echo \"Error: no test specified\" &amp;&amp; exit 1",
    "start": "echo startando",
    "prestart": "echo prestart",
    "poststart": "echo post start",
    "postinstall": "mkdirp src/components/bootstrap/ src/components/font-awesome/ &amp;&amp; cp -r node_modules/bootstrap/dist src/components/bootstrap/ &amp;&amp; cp -r node_modules/font-awesome/css src/components/font-awesome/ &amp;&amp; cp -r node_modules/font-awesome/fonts src/components/font-awesome/",
    "gulp": "gulp"
  }
<{% endcodeblock %}

Moleza, não!

Forte abraço e até a próxima
