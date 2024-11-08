print('Elija su numero de sublistas')
lista = []
cantlist = int(input())

def lists (cantlist, lista):
    for i in range(cantlist):
        print(f'Selecione los numeros de la sublista {i + 1}')
        sublist = []
        while True:
            num = int(input())
            if num == -1:
                lista.append(sublist)
                i += 1
                break
            else:
                sublist.append(num)
    return lista

print(lista)