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
        self.__curtidas=0          #Metodo encapsulamento, __curtidas troca pra uma variavel aleatoria para que o usuario nao coloque quantas curtidas quiser, só vai poder curtir de 1 em 1. (chamando a função) 

    def ola(self):
        print('Ola meu nome é %s tenho %s e sou  %d'%(self.nome,self.cor,self.idade))

    def curtir(self):
        self.__curtidas+=1

    def mostra_curtidas(self):
        print(self.__curtidas)


caio=Pessoa1('Caio','Pardo',20)

print(caio.__dict__)
Pessoa1.ola(caio)

Pessoa1.curtir(caio)
Pessoa1.mostra_curtidas(caio)
