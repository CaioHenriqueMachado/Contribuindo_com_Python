import hashlib

string = input("Digite o texto a ser gerado a Hash: ")

menu = int(input("""##### Escolha o tipo de Hash ####
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o número do Hash a ser gerado:"""))


result = hashlib.md5(string.encode('utf-8'))

print(menu)
if menu == 1:
    print("o Hash MD5 da string: {} é : {}".format(string, result.hexdigest()))
elif menu == 2:
    print("o Hash SHA1 da string: {} é : {}".format(string, result.hexdigest()))
elif menu == 3:
    print("o Hash SHA256 da string: {} é : {}".format(string, result.hexdigest()))
elif menu == 4:
    print("o Hash SHA512 da string: {} é : {}".format(string, result.hexdigest()))
else:
    print("Seleção errada")