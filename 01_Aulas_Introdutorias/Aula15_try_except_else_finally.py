#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 12:45:54 2021

@author: caio
"""

"""
Exception hierarchy:
link: https://docs.python.org/3/library/exceptions.html#exception-hierarchy

Erro da divisão por zero é da classe ZeroDivisionError,  mas também percente a 
ArithmeticError, porém é certo usar sempre a classe mais especifica se houver.
"""

# divisao = 10 / 0
# return: ZeroDivisionError: division by zero


#Tratando específicamente:
# Para tratar determinada classe do erro (ZeroDivisionError)
try:
    divisao = 10 / 0
except ZeroDivisionError:
    print( 'Não é possível realizar uma divisão por zero.')
except IndexError:
    print( 'Erro ao acessar índice inválido da lista.')


try:
    lista = [10]
    numero = lista[1]
except ZeroDivisionError:
    print( 'Não é possível realizar uma divisão por zero.')
except IndexError:
    print( 'Erro ao acessar índice inválido da lista.')
    

#Tratando genéricamente:
# Para qualquer tipo de erro
try:
    divisao = 10 / 0
except:
    print( 'Erro desconhecido')
    
    
    

# CASO 2:

# Tratar uma excessão que ainda não foi prevista. 
# BaseException é pai de todos os erros, todos pertencem a ele.
try:
    x = a
except ZeroDivisionError:
    print( 'Não é possível realizar uma divisão por zero.')
except IndexError:
    print( 'Erro ao acessar índice inválido da lista.')
except BaseException as ex:
    print('Erro desconhecido: Erro: {}'.format(ex))
    

    
try:
    x = a
except ZeroDivisionError:
    print( 'Não é possível realizar uma divisão por zero.')
except IndexError:
    print( 'Erro ao acessar índice inválido da lista.')
except NameError:
    print('Erro, variavel não encotrada')
    
    
    
# finally:
# Faz com que mesmo que dê erro, ele seja sempre executado.

try:
    name = 'Caio'
    assert(name == "lucas")
except AssertionError:
    print('Teste inválido')
finally:
    print(name)
    
    
# Exemplo:
    
while True:
    try:
        x = int(input("Digite um número de 0 a 10: "))
        print('Valor digitado: {}'.format(x))
        break
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números")
        
        

# CRIANDO ERRO PERSONALIZADO

class Error(Exception):
    pass

class Range10Error(Error):
    def __init__(self, message):
        self.message = message


# raise - Força uma exceção
try:
    x = 11
    if x > 10:
        raise Range10Error('Nota não pode ser maior que 10')
except Range10Error as ex:
    print(ex)