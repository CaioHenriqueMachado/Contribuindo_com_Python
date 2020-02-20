def f():
    return 42

x=f()
print(x)


def g():
    return 'quatro',42,3.15

a, b, c=g()

print(a ,b ,c)

def dicionario():
    return {'nome': 'Caio'}


print(dicionario())

x=dicionario()
print(x['nome'])
