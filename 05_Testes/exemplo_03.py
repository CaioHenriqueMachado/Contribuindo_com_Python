# Nesse exemplo retorna os divisores de um numero

def divisores(valor):
    result = []
    for i in range(1, valor + 1):
        if ( valor % i == 0 ):
            result.append(i)
    print(result)
    return result

# TESTE

assert  divisores(2) == [1, 2] 
assert  divisores(4) == [1, 2, 4] 
assert  divisores(6) == [1, 2, 3, 6] 
assert  divisores(10) == [1, 2, 5, 10] 
assert  divisores(12) == [1, 2, 3, 4, 6, 12]

if __name__ == "__main__":
    pass