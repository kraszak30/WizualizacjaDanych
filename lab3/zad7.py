def ciag1(* liczby):
     if len(liczby) == 0:
         return 0
     else:
         wynik = liczby[0]
         for i in liczby:
             wynik *= i
         return wynik
print(ciag1())
print(ciag1(1,2,3,4,5,6,7))