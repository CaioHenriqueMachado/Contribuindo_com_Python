from models import Pessoas

def insere_pessoa():
    pessoa = Pessoas(nome='Caio', idade=29)
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
    # insere_pessoa()
    # consulta_pessoas()
    # exclui_pessoa()