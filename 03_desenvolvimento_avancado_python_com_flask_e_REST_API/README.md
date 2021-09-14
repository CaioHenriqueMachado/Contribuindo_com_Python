<h1 align="center" id="1">My notes about Python - Conceitos Avançados com Flask</h1>

> *Para entender os conceitos intermediários foi desenvolvido um projeto para aplicar todos os conceitos abordados. Nesse README estão apenas as informações iniciais para fazer um projeto usando Flask.

<img src="../img/line.png" alt="line" width="100%">
<br>

## SUMÁRIO
 - [Introdução](#0_0)
 - [Ambiente virtual](#0_1)
 - [Flask](#0_2)
 - [Tools](#0_3)
 - [Instalando Pacotes](#0_4)
 - [requirements](#0_5)
 - [Recursos da API](#0_6)

<img src="../img/line.png" alt="line" width="100%">
<br>

<h3 id="0_0">Introdução</h3>
<p align="justify"> O desafio desse projeto é desenvolver uma API onde terá a tabela de pessoas e atividades sendo possível listar, criar, editar ou excluir cadastros de pessoas ou atividades, a API também deve contar com um sistema de autenticação básica via login e senha para conseguir algumas das ações.</p>

<br>

**O que é API(Application Programming Interface)?**

Significado: *Interface de programação de aplicativos*

 - Conjunto de rotinas para acesso a um aplicativo/software/plataforma baseado na web
 - APIs são importantes quando se tem a intenção de realizar integrações com outros serviços

<br>

**REST:** Projeta a ideia de que todo recurso deveria responder aos mesmos métodos.

<br>

**REST API:** É uma API desenvolvida utilizando os princípios da arquitetura REST.

 - Um REST API é consumido através de requisições HTTP
 - REST API são geralmente representadas em seus formatos por JSON e XML. Também são usados páginas HTML, PDF e arquivos de imagens.
 - Ao implementar um REST API, cada método deve ser responsável por um tipo diferente de ação. Exemplo: Consulta, Alteração, Inclusão e Exclusão.

<br>

**URL vs URN vs URI:**

 - URL: globallabs.academy
 - URN: /category/blog/
 - URI: une protocolo(https://), URL(globallabs.academy) e URN (/category/blog/)

<br>

**XML:** 

- Linguagem de marcação
- Usado para compartilhar informações através de rerquisições HTTP
- Estruturada em tags.
- Ultimamente pouco usado por causa do JSON

<br>

**JSON:**

- Muito usado nos dias atuais.
- Usado para compartilhar informações entre sistemas independente da linguagem utilizada.
- Derivada do JavaScript

<img src="../img/line.png" alt="line" width="100%">
<br>

<h3 id="0_1">Ambiente virtual</h3>

***Atenção*: Essa etapa pode ser pulada caso criar um projeto direto pelo Pycharm.**

**Ambiente virtual**

Para criar o ambiente virtual:

> cmd: `python3 -m venv flask_env`

Caso dê erro, então usar:

> cmd: `python3 -m venv flask_env --without-pip`

> Aqui ele criou o ambiente virtual, porém como foi sem o pip, no passo seguinte deu erro ao tentar criar o projeto. 

Solução: No meu caso a solução foi criar o ambiente virtual direto pelo Pycharm.

Ambiente virtual do projeto: **flask_env**

Para ativar o ambiente virtual:

> cmd: `./flask_env/bin/activate`

> O que funcionou:

> cmd: `source ./flask_env/bin/activate`

Para desativar o ambiente virtual:

> cmd: `deactivate`

*Porém ao entrar no CMD pelo Pycharm ele já ativa o ambiente virtual sozinho.*

<img src="../img/line.png" alt="line" width="100%">
<br>

<h3 id="0_2">Flask</h3>

**O que é Flask?** 

 - Microframework para python utilizado para desenvolvimento de aplicações WEB.
 - Microframework por ter núcleo simples, porém é estendível
 - Mais utilizados para desenvolvimento de API

<img src="../img/line.png" alt="line" width="100%">
<br>

<h3 id="0_3">Tools</h3>

Ferramentas utilizadas:
 - Python 3.7
 - Pycharm Community
 - Flask
 - Postman

<img src="../img/line.png" alt="line" width="100%">
<br>

<h3 id="0_4">Instalando Pacotes</h3>

> Preferencialmente instalar em um ambiente virtual.

<br>

**Django**

 > cmd: `pip install django`

<br>

**Flask**

 > cmd: `pip install flask`

<br>

**RESTful**

 > cmd: `pip install flask-restful`

<br>

**SQLAlchemy**

 > cmd: `pip install sqlalchemy`

<br>

**FlaskHttpauth**

> Para autenticação no Flask

 > cmd: `pip install flask-httpauth`

<img src="../img/line.png" alt="line" width="100%">
<br>

<h3 id="0_5">Requirements</h3>

<p align="justify">No arquivo requirements.txt terão todos os pacotes usados para o projeto e suas respectivas versões.</p>

> cmd: `pip freeze > requirements.txt`

<img src="../img/line.png" alt="line" width="100%">
<br>

<h3 id="0_6">Recursos da API</h3>

 - Autenticação
   - Login e senha
 - Pessoa
   - Listar
   - Adicionar
   - Editar
   - Excluir
 - Atividades
   - Listar
   - Adicionar
   - Editar
   - Excluir

<br>

 - [Voltar ao topo](#1)
 - [Voltar ao menu principal](https://github.com/CaioHenriqueMachado/Contribuindo_com_Python/#1)

<br>
<img src="../img/line.png" alt="line" width="100%">