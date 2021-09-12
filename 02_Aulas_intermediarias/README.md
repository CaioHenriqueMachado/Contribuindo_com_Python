<h1 align="center" id="1">My notes about Python - Conceitos Intermediários</h1>

:pushpin: **Note:**

> *Para entender os conceitos intermediários foi desenvolvido um projeto para aplicar todos os conceitos abordados. Nesse README estão apenas as informações iniciais para fazer um projeto usando o Django. Para ver o projeto finalizado [clique aqui](#0_9)*

<img src="../img/line.png" alt="line" width="100%">
<br>

## SUMÁRIO
 - [Introdução](#0_0)
 - [Tools](#0_1)
 - [Criando Ambiente virtual e Projeto por linha de comando](#0_2)
 - [Criando App](#0_3)
 - [Djando admin](#0_4)
 - [Migrates](#0_5)
 - [requirements](#0_6)
 - [Projeto final](#0_7)

<img src="../img/line.png" alt="line" width="100%">
<br>

<h3 id="0_0">Introdução</h3>
Como fazer comentarios em Python, seja na linha ou em bloco.

<br>

<h3 id="0_1">Tools</h3>

- Pycharm
- Framework Django
- Postman
- Python 3

> Para ver a versão do python 3 instalada na sua máquina: (Provavelmente vão ter as versões 2 e 3, então digite python3 para verificar)

> cmd: `python3 --version`

(Caso não tenha instalado, instale o python 3 e o pip)

<br>

<h3 id="0_2">Criando Ambiente virtual e Projeto por linha de comando</h3>

***Atenção*: Essa etapa pode ser pulada caso criar um projeto direto pelo Pycharm.**

**Ambiente virtual**

Para criar o ambiente virtual:

> cmd: `python3 -m venv myfirstvenv`

Caso dê erro, então usar:

> cmd: `python3 -m venv myfirstvenv --without-pip`
> Aqui ele criou o ambiente virtual, porém como foi sem o pip, no passo seguinte deu erro ao tentar criar o projeto. 

Solução: No meu caso a solução foi criar o ambiente virtual direto pelo Pycharm.

Ambiente virtual do projeto: **myfirstvenv**

Para ativar o ambiente virtual:

> cmd: `./myfirstvenv/bin/activate`

> O que funcionou:

> cmd: `source ./myfirstvenv/bin/activate`

Para desativar o ambiente virtual:

> cmd: `deactivate`

*Porém ao entrar no CMD pelo Pycharm ele já ativa o ambiente virtual sozinho.*
<br>

**Projeto**

**Atenção:** Para instalar os pacotes, certifique-se que você está dentro da pasta **myfirstvenv** com o ambiente virual ativo.

Com a venv ativa, escolha a pasta para criar um projeto:

> cmd: `django-admin startproject .project_01`

<br>

<h3 id="0_2">Criando App</h3>
<p align="justify">Para criar um App, entre na primeira pasta do projeto "project_01" e crie o app:</p>

> cmd: `django-admin startapp core`
<br>

<h3 id="0_3">Instalando Pacotes</h3>

**Django**
 `pip install django`


<br>
<h3 id="0_4">Django Admin</h3>
<p align="justify">Django admin é uma ferramenta dentro do Django no qual foi feita para fazer a criação e administração de usuarios, permissões, filtros, etc.</p>

<p align="justify">Para criar as tabelas padrão:</p>

> cmd: `python manage.py migrate`
> Após isso já é possível acessar: http://127.0.0.1:8000/admin


<p align="justify">Para criar usuário admin:</p>

> cmd: `python manage.py createsuperuser --username admin`

Email: admin@admin.com.br
passwd: caio1234

<br>
<h3 id="0_4">Migrates</h3>

<p align="justify">Após criar uma classe no model, rodar:</p>

> cmd: `python manage.py makemigrations core`

> Com isso, ele vai criar migrate (0001) com base na classe e colocar na pasta core

<p align="justify">Para rodar migrate especifica para visualizar:</p>

> cmd: `python manage.py sqlmigrate core 0001`

<p align="justify">Para rodar migrate no banco de dados:</p>

> cmd: `python manage.py migrate core 0001`

<br>
<h3 id="0_4">Requirements</h3>

<p align="justify">No arquivo requirements.txt terão todos os pacotes usados para o projeto e suas respectivas versões.</p>

> cmd: `pip freeze > requirements.txt`


[Voltar ao topo](#1)

[Voltar ao menu principal](https://github.com/CaioHenriqueMachado/Contribuindo_com_Python/#1)