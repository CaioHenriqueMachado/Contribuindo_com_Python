# Nesse exemplo retorna se o número é primo ou não.

from exemplo_03 import divisores


def ehPrimo(valor):
    result = divisores(valor)
    if len(result) == 2:
        return True
    return False

# TESTE
assert ehPrimo(10) == False
assert ehPrimo(2) == True

assert ehPrimo(17)
assert ehPrimo(19)
assert ehPrimo(23)

assert not ehPrimo(0)
assert not ehPrimo(1)
assert not ehPrimo(4)
assert not ehPrimo(6)


if __name__ == "__main__":
    pass