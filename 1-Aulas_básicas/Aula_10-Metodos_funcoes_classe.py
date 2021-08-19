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











