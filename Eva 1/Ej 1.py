lista1 = [7,8,9,10]
lista2 = [1,2,3,4,7,9]
result = []
def complists (lista1, lista2):
    for number1 in lista1:
        for number2 in lista2:
            if number1 == number2:
                result.append(number1)
    return result

print(complists (lista1, lista2))