#Leia mensagem.txt  e grave cripto.txt com todas as vogais trocadas por '*'.
texto= open ('mensagem.txt')
saida=open('cripto.txt','w')
for linha in texto.readlines():     #gera uma lista onde  cada elementope uma linha
    for letra in linha:                     # para cada linha é uma letra
        if letra in 'aeiou':                # se a letra for 'aeiou' escreva *
            saida.write('*')
        else:
            saida.write(letra)
texto.close()
saida.close()
