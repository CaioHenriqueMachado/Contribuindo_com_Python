'''
Faça um programa que recebe um número natural não nulo  "n" e imprime/mostra na
tela todas as combinações das  "n" primeiras letras, isto é, todas as letras sozinhas,
depois todas as combinações de duas letras, as combinações de 3 letras, até a
combinação das "n" letras. No total serão (2^n)-1 possibilidades.
'''
num=int(input('Digite um numero:  '))
p1=num
limite=(2**num)-1
i=0
j=0
x=1
k=0
exibi=' '
linha1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
linha2=linha1
linha3=linha1
linha4=linha1
linha5=linha1
print('O numero imprimiu ' ,limite,' combinaçoes diferentes!! ')

while (num<=limite):
    num+=1
    if(x<=p1):                       #Para 1 digito 
        print(linha1[i])
        x=x+1
        i=i+1

    elif(k<=i):
        linha1[k]
        while(j<=i):
            if(linha1[k] == linha2[j]):             #Para 2 digitos
                j+=1
            exibi=linha1[k]+linha2[j]
            if(j!=i):
                print(exibi)
                j=j+1
                if(j==i):
                    k+=1
                    j=k


                
                
                
