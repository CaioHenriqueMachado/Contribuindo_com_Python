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
    
from Aula10_Metodos_funcoes_classe import Calculadora1


calculadora = Calculadora1(10, 50)

assert(calculadora.soma() == '10 + 50 = 60')

assert(calculadora.subtracao() == '10 - 50 = -40')

assert(calculadora.divisao() == '10 / 50 = 0.2')

assert(calculadora.multiplicacao() == '10 * 50 = 500')



# EXEMPLO 2: 
    
from Aula10_Metodos_funcoes_classe import Calculadora2

calculadora = Calculadora2()

assert(calculadora.soma(10, 50) == '10 + 50 = 60')

assert(calculadora.subtracao(10, 50) == '10 - 50 = -40')

assert(calculadora.divisao(10, 50) == '10 / 50 = 0.2')

assert(calculadora.multiplicacao(10, 50) == '10 * 50 = 500')


# EXEMPLO 3:

from Aula10_Metodos_funcoes_classe import Televisão

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

from Aula10_Metodos_funcoes_classe import Pessoa1
            

# Instanciando, adicionando atributos e valores. Os atributos ficaram somente na instancia "Caio"

Caio = Pessoa1()
Caio.nome = 'Caio'
Caio.emprego = 'Desempregado'
Caio.Idade = 20

assert(Caio.__dict__ == {'nome': 'Caio', 'emprego': 'Desempregado', 'Idade': 20})


# EXEMPLO 5:
    
from Aula10_Metodos_funcoes_classe import Pessoa2


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
















