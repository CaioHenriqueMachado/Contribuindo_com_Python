'''
Dados dois numeros int positivos, determine o maximo divisor comum entre eles
usando o algoritmo de Euclides. Ex(21,15)=3
      a      b     a%b             OBS: Nao tem problema de 1ºnum ser menor pois ele todo acaba sendo o resto entao nao muda nada.
    21   15         6
    15      6         3
    6        3          0
    
'''
a=int(input('a:  '))
b=int(input('b:  '))

while (a%b !=0):
    a, b = b, a%b

print('mdc = %d ' %b)
