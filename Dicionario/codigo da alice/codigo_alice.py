arq = open('alice.txt')     #Abre o arquivo
texto = arq.read()          #Lendo todo arquivo 
texto = texto.lower()       #Deixa tudo em minusculo
import string
for c in string.punctuation:        # replace de todos os caracteres especiais por branco
    texto = texto.replace(c, ' ')
texto = texto.split()

dic = {}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1
print ('Alice aparece %s vezes' %dic['alice'])
arq.close()
