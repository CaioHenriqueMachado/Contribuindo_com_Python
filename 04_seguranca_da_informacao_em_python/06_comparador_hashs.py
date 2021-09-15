import hashlib

string1 = 'Teste inicial'.encode('utf-8')

string2 = 'Teste inicial'.encode('utf-8')

hash1 = hashlib.new('ripemd160')

hash1.update(string1)


hash2 = hashlib.new('ripemd160')

hash2.update(string2)

print("-" * 60)

print(hash1.hexdigest())
print(hash2.hexdigest())


if hash1.digest() == hash2.digest():
    print("\nA string 1 é igual a string 2")
else:
    print("\nA string 1 é diferente a string 2")