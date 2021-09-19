# Nesse exemplo retorna uma lista ordenada


lista = [1,5,3,2,7,50,9]

def bubbleSort(list):
    for i in range(len(list)):
        for j in range(0, len(list) - 1 - i):
            if (list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list



if __name__ == "__main__":
    bubbleSort(lista)