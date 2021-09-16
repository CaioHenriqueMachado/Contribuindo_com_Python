import ctypes

atributo_ocutar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('exemplo_ocultar.txt', atributo_ocutar)

if retorno:
    print('Arquivo foi ocultado')
else:
    print('Arquivo não foi ocultado')

