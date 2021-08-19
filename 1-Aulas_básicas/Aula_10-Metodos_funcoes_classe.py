#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 23:18:24 2021

@author: caio
"""

"""
FUNÇÃO:
Tudo que retorna valor

MÉTODO:
 - Tudo que não retorna valor
 - Em python chamamos de definição (por isso inicia com def)
"""


# EXEMPLO 1: 

class Calculadora1 ():
    def __init__(self, num1, num2):
        self.valor1 = num1
        self.valor2 = num2
        
    def soma(self):
        return "{} + {} = {}".format(self.valor1, self.valor2, self.valor1 + self.valor2)
    
    def subtracao(self):
        return "{} - {} = {}".format(self.valor1, self.valor2, self.valor1 - self.valor2)
        
    def divisao(self):
        return "{} / {} = {}".format(self.valor1, self.valor2, self.valor1 / self.valor2)
        
    def multiplicacao(self):
        return "{} * {} = {}".format(self.valor1, self.valor2, self.valor1 * self.valor2)
        

calculadora = Calculadora1(10, 50)

assert(calculadora.soma() == '10 + 50 = 60')

assert(calculadora.subtracao() == '10 - 50 = -40')

assert(calculadora.divisao() == '10 / 50 = 0.2')

assert(calculadora.multiplicacao() == '10 * 50 = 500')




# EXEMPLO 2: 

class Calculadora2 ():
    def __init__(self): # Neste exemplo não é necessário ter essa função
        pass
        
    def soma(self, valor1, valor2):
        return "{} + {} = {}".format(valor1, valor2, valor1 + valor2)
    
    def subtracao(self, valor1, valor2):
        return "{} - {} = {}".format(valor1, valor2, valor1 - valor2)
        
    def divisao(self, valor1, valor2):
        return "{} / {} = {}".format(valor1, valor2, valor1 / valor2)
        
    def multiplicacao(self, valor1, valor2):
        return "{} * {} = {}".format(valor1, valor2, valor1 * valor2)
        

calculadora = Calculadora2()

assert(calculadora.soma(10, 50) == '10 + 50 = 60')

assert(calculadora.subtracao(10, 50) == '10 - 50 = -40')

assert(calculadora.divisao(10, 50) == '10 / 50 = 0.2')

assert(calculadora.multiplicacao(10, 50) == '10 * 50 = 500')


# EXEMPLO 3: 

class Televisão():
    def __init__(self): 
        self.ligada = False
        self.volume = 5
        
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
        
    
    def aumentaVolume(self):
        self.volume += 1

    def abaixaVolume(self):
        self.volume -= 1


televisao = Televisão()

televisao.power()
assert(  televisao.ligada == True)

televisao.power()
assert(  televisao.ligada == False)

televisao.aumentaVolume()
assert(  televisao.volume == 6)

televisao.abaixaVolume()
assert(  televisao.volume == 5)


# EXEMPLO 4:
    
class Pessoa1: # Classe vazia
    pass                     

# Instanciando, adicionando atributos e valores. Os atributos ficaram somente na instancia "Caio"

Caio = Pessoa1()
Caio.nome = 'Caio'
Caio.emprego = 'Desempregado'
Caio.Idade = 20

assert(Caio.__dict__ == {'nome': 'Caio', 'emprego': 'Desempregado', 'Idade': 20})


# EXEMPLO 5:

class Pessoa2:
    def __init__(self,nome,cor,idade):
        self.nome       = nome
        self.cor        = cor
        self.idade      = idade
        self.__curtidas = 0     #  Metodo encapsulamento:  Não é possível ser acessada diretamente   

    def ola(self):
        return 'Ola meu nome é %s tenho %s e sou  %d'%(self.nome,self.cor,self.idade)

    def curtir(self):
        self.__curtidas+=1

    def mostra_curtidas(self):
        return self.__curtidas


caio=Pessoa2('Caio','Pardo',20)

#print (caio.__curtidas)
#return: # AttributeError: 'Pessoa2' object has no attribute '__curtidas'

assert(caio.idade == 20)

assert(caio.__dict__ == {'nome': 'Caio', 'cor': 'Pardo', 'idade': 20, '_Pessoa2__curtidas': 0})

assert(Pessoa2.ola(caio) == "Ola meu nome é Caio tenho Pardo e sou  20")

assert(caio.ola() == "Ola meu nome é Caio tenho Pardo e sou  20")

Pessoa2.curtir(caio)

caio.curtir()
assert(caio.mostra_curtidas() == 2)
















