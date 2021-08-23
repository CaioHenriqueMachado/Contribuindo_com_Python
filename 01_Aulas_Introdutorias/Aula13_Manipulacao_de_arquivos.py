#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 23:33:36 2021

@author: caio


OBJETIVO:
    1. Aprender a ler e escrever arquivos
    2. Manipular informações dos arquivos
    3. Copiar e mover arquivos
"""
# Usado apenas para mover ou copiar arquivos
import shutil


# EXEMPLO 1: 
file_name = 'teste.txt'
    
# Write - Cria o arquivo se não existir, caso exista já existir ele substitui
file = open(file_name, 'w')
file.write("ARQUIVO FEITO EM PYTHON\n\n")
file.close()


# 'a' - Cria o arquivo se não existir, caso exista já existir ele atualiza
file = open(file_name, 'a')
file.write("Esse arquivo foi criado apenas para teste")
file.close()


# EXEMPLO 2: 

def write(file, text):
    arquivo = open(file, 'w')
    texto = arquivo.write(text)
    return texto

def add(file, text):
    arquivo = open(file, 'a')
    texto = arquivo.write(text)
    return texto

def read(file):
    arquivo = open(file, 'r')
    texto = arquivo.read()
    return texto

def move(file, destiny_with_filename):
    shutil.move(file, destiny_with_filename)

def copy(file, destiny_with_filename):
    shutil.copy(file, destiny_with_filename)
    
    
# copy(file_name, './teste2.txt')
# move(file_name, './teste2.txt')



assert(read(file_name) == "ARQUIVO FEITO EM PYTHON\n\nEsse arquivo foi criado apenas para teste")



# EXEMPLO 3: Alunos e sua média final
    
texto_do_arquivo = 'Felipe, 5,10,10,10,2\n'
texto_do_arquivo += 'Pedro, 5,8,20,10,2\n'
texto_do_arquivo += 'João, 5,10,9,10,2\n'
texto_do_arquivo += 'Lucas, 5,10,7,10,2\n'
texto_do_arquivo += 'Lucy, 10,10,10,10,2'

write(file_name, texto_do_arquivo)


result = read(file_name)

result = result.split('\n')

medias = []
alunos = []
for linha in result:
    notas  = linha.split(',')
    aluno = notas[0]
    alunos.append(aluno)
    notas.pop(0)
    funcao_media = lambda notas: sum([int(i) for i in notas]) / 5
    medias.append(funcao_media(notas))


for aluno, media in zip(alunos, medias):
    print("O {} teve média {}".format(aluno, media))
           





