#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 13:58:16 2021

@author: caio
"""

# Instalando pacote requests
#cmd:  pip install requests

# Usando api viacep


import requests

response = requests.get('https://viacep.com.br/ws/01001000/json/')

#POKEMON POKEAPI: https://pokeapi.co/api/v2/pokemon/ditto/

assert(response.status_code == 200)

response_string = response.text

assert(str(type(response_string)) == "<class 'str'>")

response_json = response.json()

assert(str(type(response_json)) == "<class 'dict'>")


logradouro = response_json['logradouro']
assert(logradouro == "Praça da Sé")


print(response.json())