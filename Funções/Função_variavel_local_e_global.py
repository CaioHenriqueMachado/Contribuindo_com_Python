a=5
def muda_e_imprime():
    a=7
    print('a dentro da função:  %d'  %a)
print("a antes de mudar:  %d"  %a)
muda_e_imprime()
print('a depois de mudar:  %d'  %a)



#agora A sao as mesmas pessoas:
a=5
def muda_e_imprime():
    global a
    a=7
    print('a dentro da função:  %d'  %a)
print("a antes de mudar:  %d"  %a)
muda_e_imprime()
print('a depois de mudar:  %d'  %a)
