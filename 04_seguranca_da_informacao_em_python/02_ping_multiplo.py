import os
import time

# pinga em diversos hosts de vez

hosts = ['google.com.br',
         'www.pudim.com.br',
         'youtube.com',
         '8.8.8.8']

print("#" * 60)

for ip in hosts:
    print("\n" + ("-"*20) + " Iniciando ping á {}:".format(ip))
    os.system('ping -c 2 {}'.format(ip))
    time.sleep(3)

print("#" * 60)
