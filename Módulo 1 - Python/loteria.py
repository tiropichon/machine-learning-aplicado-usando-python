import random
lista=[]
i=1
while i <= 5:
    posible=random.randint(0,9)
    if posible not in lista:
        lista.append(posible)
        i+=1
print("La futura combinación ganadora de la Loteria es:",sorted(lista))