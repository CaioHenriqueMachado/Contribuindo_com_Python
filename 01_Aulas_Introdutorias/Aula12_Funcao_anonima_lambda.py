#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 23:12:59 2021

@author: caio
"""

# Função lambda é uma função anonima

"""
CARACTERÍSTICAS:
    - A função só Tem uma linha
    - A função não contém nome
"""

# Exemplo 1:
    
soma = lambda a, b: a + b

assert(soma(1,4) == 5)


# Exemplo 2:

contador_letras = lambda lista: [ len(x) for x in lista ]

lista = [ 'gato', 'cachorro', 'coelho', 'passaro' ]

assert (contador_letras(lista) == [4, 8, 6, 7])


# Exemplo 3:
    
calculadora = {
    'soma'          : lambda a, b: a + b,
    'subtracao'     : lambda a, b: a - b,
    'divisao'       : lambda a, b: a / b,
    'multiplicacao' : lambda a, b: a * b,
    }


soma = calculadora['soma']
assert(soma(10,2) == 12)

subtracao = calculadora['subtracao']
assert(subtracao(10,2) == 8)

divisao = calculadora['divisao']
assert(divisao(10,2) == 5)

multiplicacao = calculadora['multiplicacao']
assert(multiplicacao(10,2) == 20)









