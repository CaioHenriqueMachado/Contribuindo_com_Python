
# IMPRIMA A TABUADA DE 1 ATÉ 10

TABUADA = 1

while (TABUADA <= 10):
    N=1
    print('\n\tTabuada do %d:' %TABUADA)
    while (N <= 10):
        print('%d x %d = %d' %(TABUADA, N, TABUADA*N))
        N+=1

    TABUADA+=1
