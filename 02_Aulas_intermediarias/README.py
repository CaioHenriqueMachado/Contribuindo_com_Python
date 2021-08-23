"""
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
 (pip3 install django)

Escolha a pasta para criar um projeto:
django-admin startproject 01_first_project

Para criar um App:
django-admin startapp 01_first_project

01_first_project

"""

print('oi')