# Ferramenta para a manupulação de endereços, seja rede ou proprio IP

import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

# Somando
print(endereco + 256)

# Imprimir rede mesmo ela não existindo
ip1 = '192.168.0.100/24'

rede = ipaddress.ip_network(ip1, strict=False)

print(rede)

# printar todos ips da rede

for ip in rede:
    print(ip)