# Só para testar se a conexão está funcionando
from models import Pessoas, Usuarios

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)
    #pessoa = Pessoas.query.filter_by(nome='Caio').first()
    #print(pessoa.nome)


def insere_pessoa():
    pessoa = Pessoas(nome='Caio', idade=23)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    #pessoa = Pessoas.query.filter_by(nome='Caio').first()
    #print(pessoa.nome)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Caio').first()
    pessoa.idade = 21
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Caio').first()
    pessoa.delete()


if __name__ == '__main__':
    insere_usuario('Caio', '1234')
    insere_usuario('Lucas', '135')
    consulta_usuarios()
    # consulta_pessoas()
    # exclui_pessoa()