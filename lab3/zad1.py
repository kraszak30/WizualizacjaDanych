A = [1-x for x in range(11)]
B = [4**x for x in range(7)]
C = [x for x in B if x%2==0]
print(A ,B ,C)