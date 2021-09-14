import os

# Alguns parâmetros do comando ping:
#
# (-t): Utilizando o -t, o comando ficará enviando pacotes até o usuário forçar a parada (com Ctrl + C).
#
# (-a) no Windows / (host) no Linux/Mac: No Windows: Além de testar a conectividade, também tentará resolver o hostname da máquina pingada.
#
# (-n) no Windows / (-c) no Linux: O comando define o número de pacotes a ser enviado.
# Sintaxe: -c 8 site.com.br (8 pacotes serão enviados pelo comando).

print("#" * 60)
ip_ou_host = input("Digite o IP ou HOST a ser verificado:")
# Exemplo ip: 8.8.8.8
# Exemplo ip: google.com.br

# Também é possível dar um ping pelo cmd, o '-n 6' significa que serão enviados 6 pacotes
os.system('ping -c 6 {}'.format(ip_ou_host))

print("#" * 60)
