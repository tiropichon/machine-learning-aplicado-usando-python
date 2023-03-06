import random
lista=[]
print(lista)
i=1
while i <= 6:
    posible=random.randint(1,49)
    if posible not in lista:
        lista.append(posible)
        i+=1
print("La futura combinación ganadora de la Bonoloto es:",sorted(lista))