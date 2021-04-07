def nty(a1,q,n):
    an = a1 * q ** (n-1)
    return an

def suma(a1,q,n):
    if q == 1:
        suma = a1 * n
    else:
        suma = a1 * ((1-q**n)/(1 - q))
    return suma