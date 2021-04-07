import random
lista = []
i=1
while i <= 10:
    lista.append(random.randint(1,10))
    i += 1
print(lista)
lista2 = [x for x in lista if x%2==0]
print(lista2)