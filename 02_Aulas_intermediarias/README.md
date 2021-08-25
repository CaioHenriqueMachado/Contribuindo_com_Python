Para ver a versão do python 3 instalada na sua máquina:
(Provavelmente vão ter a versão 2 e 3, então digite python3 
para verificar)
cmd: python3 --version

(Caso não tenha instalado, instale o python 3 e o pip)


Para criar o ambiente virtual:
cmd: python3 - m venv myfirstvenv
(ESTÁ COM UM ERRO, então usar:
cmd: python3 -m venv myfirstvenv --without-pip)
(porém sem ele deu erro ao criar projeto, então consegui criar direto pelo criar projeto do pycharm)




OBS: A virtual env (myfirstvenv) foi usada para todos as aulas 
feitas nessa pasta.

Para ativar o ambiente virtual:
cmd: ./myfirstvenv/bin/activate
(o que funcionou:)
cmd:source ./myfirstvenv/bin/activate

Para desativar o ambiente virtual:
cmd: deactivate


 - Entrar na pasta myfirstvenv e instalar os pacotes 
 (pip install django)

Com a venv ativa, escolha a pasta para criar um projeto:
django-admin startproject project_01

Para criar um App, entre na primeira pasta do projeto 'project_01' e crie o app:
django-admin startapp core



### Estrutura básica do Django:

Para criar as tabelas:

'cmd: python manage.py migrate'

Após isso já é possível acessar (http://127.0.0.1:8000/admin)


Para criar usuário admin:

'cmd: python manage.py createsuperuser --username admin'

Email address: admin@admin.com.br
passwd: caio1234


Depois de criar uma classe no model, rodar:
'python manage.py makemigrations core'

Com isso, ele vai criar migrate (0001) com base na classe e colocar na pasta core

Para rodar migrate especifica para visualizar
'python manage.py sqlmigrate core 0001'

Para rodar migrate no banco de dados:
'python manage.py migrate core 0001'


