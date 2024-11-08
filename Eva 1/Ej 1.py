lista1 = [1, 2, 3 ,4]
lista2 = [3, 4, 5, 6]

def intersect(lista1, lista2):
    result = []
    for i in lista1:
        for j in lista2:
            if j == i and j not in result:
                result.append(j)
    return result
print('El Resultado es:')
print(intersect(lista1, lista2))
