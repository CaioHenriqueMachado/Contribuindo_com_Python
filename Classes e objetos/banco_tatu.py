#incompleto

class Cliente:
    def __init__(self , nome,  telefone):
        self.nome=nome
        self.telefone=telefone

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo=saldo
        self.clientes=clientes
        self.numero=numero
    def resumo(self):
        print('CC Número: %s Saldo:  %10.2f' %(self.numero, self.saldo))
    def saque (self , valor):
        if self.saldo>= valor:
            self.saldo -= valor
    def deposito(self , valor):
        self.saldo  +=valor

from tatu import Cliente
from tatu import Conta
joão = Cliente('João da Silva','777-1234')
maria= Cliente('Maria da Silva', '555-4321')
print ('Nome %s.  Telefone: %s.' %(joão.nome , joão.telefone))
print ('Nome %s.  Telefone: %s.' %(maria.nome , maria.telefone))
conta1=Conta([joão],1,1000)
conta2=Conta([maria, joão],2,500)
conta1.resumo()
conta2.resumo()
            
