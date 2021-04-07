def ciag( a=1, b=4, ile=10):
    lista = []
    i = 0
    if ile <= 0:
        print('error')
    elif ile == 1:
        return a*b
    else:
        while i != ile:
            a *= b
            lista.append(a)
            i += 1
        return lista
print(ciag())
print(ciag(ile=0))
print(ciag(ile=1))