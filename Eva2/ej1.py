import requests, json

#creacion de librerias
par = [] 
nopar = []
# indice de cant de post
index = 1 

print('Cantidad de posteos q desee')
cantpost = int(input())
while True :
    if cantpost > 0 and cantpost < 100:
        url = f'https://jsonplaceholder.typicode.com/posts/{index}'
        getApy = requests.get(url)
        data = getApy.json()
        if index <= cantpost:
            if data['id'] % 2 == 0:
                index += 1
                par.append(data)
            else:
                index += 1
                nopar.append(data)
        else:
            break
    else:
        print('Cantidad tiene q ser de 1 a 100')
        cantpost = int(input())

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, n - 1):
        if numero % i == 0:
            return False
    return True

with open('./Descargas/par.json', 'w') as archivo:
    json.dump(par, archivo)

with open('./Descargas/nopar.json', 'w') as archivo:
    json.dump(nopar, archivo)
