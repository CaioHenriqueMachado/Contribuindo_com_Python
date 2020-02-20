def ip_ok(ip):
    ip=ip.split('.')            # separa cada um dos quatro transformando em uma lista
    for byte in ip:             #o ponto separa os vagoes
        if int (byte)>255:  #se apos convertido para inteiro é > que 255
            return False        # 
    return True
arq=open('IPS.txt')         # abre o txt ja criado
validos= open('ips-validos.txt','w')        # cria esse txt
invalidos= open('ips-invalidos.txt','w')      # cria esse txt
for linha in arq.readlines():
    if ip_ok(linha):
        validos.write(linha)        # retorna valido
    else:
        invalidos.write(linha)      #retorna invalidos

arq.close()
validos.close()
invalidos.close()
