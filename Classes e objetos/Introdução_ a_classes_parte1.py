class Pessoa:
    pass                     #código para deixar em branco.


Caio = Pessoa()
Caio.nome='Caio'
Caio.emprego='Desempregado'
Caio.Idade= 20


print(Caio.__dict__)


class Pessoa1:
    def __init__(self,nome,cor,idade):
        self.nome=nome
        self.cor=cor
        self.idade=idade

    def ola(self):
        print('Ola meu nome é %s tenho %s e sou  %d'%(self.nome,self.cor,self.idade))


caio=Pessoa1('Caio','Pardo',20)

print(caio.__dict__)
Pessoa1.ola(caio)

#PARA CRIAR UMA CLASSE SOBRE A OUTRA

class Pessoa2(Pessoa1):
    pass

lucas=Pessoa2('lucas','preto',21)
print(lucas.__dict__)
