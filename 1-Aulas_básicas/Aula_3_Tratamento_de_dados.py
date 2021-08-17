'''

AULA 3

ENTRADA DE DADOS E EXIBIÇÃO

Para a entrada de dados, sempre será usado o método "input".

EXEMPLOS:
'''

NOME    = input ('Digite seu nome: ')
IDADE   = int(input ('Digite sua idade: '))
SIGNO   = input ('Digite seu signo: ')


#MÉTODOS DE EXIBIÇÃO

#EXEMPLO 1
print("Seu nome é", NOME, "com", IDADE, "anos de idade, signo de",SIGNO, "!!")

#EXEMPLO 2
print("Seu nome é "+ NOME + " com " + str(IDADE) + " anos de idade, signo de " + SIGNO + " !!")

#EXEMPLO 3
print("Seu nome é %s com %d anos de idade, signo de %s !!" %(NOME,IDADE,SIGNO))

#EXEMPLO 4
frase = "Seu nome é {0} com {1} anos de idade, signo de {2} !!"
print(frase.format(NOME,IDADE,SIGNO))

#EXEMPLO 5
frase = "Seu nome é {name} com {age} anos de idade, signo de {sig} !!"
print(frase.format(name=NOME,age=IDADE,sig=SIGNO))

#EXEMPLO 6
print(NOME, IDADE, SIGNO, sep = ", ", end = " !!")
