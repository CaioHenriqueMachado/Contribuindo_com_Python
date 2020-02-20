
# Calcule a sequencia de Fibonacci:1,1,2,3,5,8,13,21,34,55


print("\nDigite até qual número a sequência irá:")
num = int(input('\nN: '))

x = 1
a = 1
b = 1

while( x <= num ):
    print (a)
    c = a + b
    a = b
    b = c
    x = x + 1
    

