# Nesse exemplo precisa trocar o valor de duas variaveis e fazer o teste para verificar se realmente foram trocadas.


valor1 = 30
valor2 = 50

temp = valor1
valor1 = valor2
valor2 = temp

assert valor1 == 50
assert valor2 == 30