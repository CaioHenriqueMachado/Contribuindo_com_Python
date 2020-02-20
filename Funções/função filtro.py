lista = [8, 9, -1, -3, 3, -5, -4, 5, -4, 2, 5, 91, -11, 5, 56, 93, 13, 15, -75, 98]
def maior_que_zero(num):
    if (num > 0):
        return True
    else:
         return False

lista_valida = filter(maior_que_zero, lista)
print (lista_valida[1])
