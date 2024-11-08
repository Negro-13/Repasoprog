print('Ingrese cantidad de listas')
cantList = int(input())
finalList = []

def createList(cantList, finalList):
    for i in range(cantList):
        subList= []
        print(f'Numeros de la lista {i +1}')
        while True:
            num = int(input())
            if num == -1:
                finalList.append(subList)
                break
            else:
                subList.append(num)
    return finalList


print(createList(cantList, finalList))
