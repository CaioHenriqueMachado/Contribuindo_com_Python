
# Aula 1 - Introdução


**FLASK:** Microframework para python utilizado para desenvolvimento de aplicações WEB.

- Microframework por ter núcleo simples, porém é estendível

- Mais utilizados para desenvolvimento de API


**API** - *Application Programming Interface - Interface de programação de aplicativos:*
 - Conjunto de rotinas para acesso a um aplicativo/software/plataforma baseado na web
 - APIs são importantes quando se tem a intenção de realizar integrações com outros serviços



**REST:** Projeta a ideia de que todo recurso deveria responder aos mesmos métodos 

**REST API:** É uma API desenvolvida utilizando os princípios da arquitetura REST

 - Um REST API é consumido através de requisições HTTP

 - REST API são geralmente representadas em seus formatos por JSON e XML. Também são usados páginas HTML, PDF e arquivos de imagens.

 - Ao implementar um REST API, cada método deve ser responsável por um tipo diferente de ação. Exemplo: Consulta, Alteração, Inclusão e Exclusão.


**URL vs URN vs URI:**

URL: globallabs.academy

URN: /category/blog/

URI: une protocolo(https://), URL(globallabs.academy) e URN (/category/blog/)


**XML:** 

- Linguagem de marcação

- Usado para compartilhar informações através de rerquisições HTTP

- Estruturada em tags.

- Ultimamente pouco usado por causa do JSON

**JSON:**

- Muito usado nos dias atuais.

- Usado para compartilhar informações entre sistemas independente da linguagem utilizada.

- Derivada do JavaScript



# Aula 2 - Instalando Flask e criando criando ambiente virtual

Ferramentas utilizadas:
 - Python 3.7
 - Pycharm Community
 - Flask
 - Postman



Flask: pip install Flask



**GERAR TXT COM DEPENDENCIAS**

Serve para a pessoa que ver o projeto saber quais são as dependências do projeto.

`pip freeze > requirements.txt`


**RESTful**

`pip install flask-restful`


**SQLAlchemy**

`pip install sqlalchemy`