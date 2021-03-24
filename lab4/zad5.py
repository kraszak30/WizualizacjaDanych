class Ciagi:
     def __init__(self, n1, roznica, ilosc):
         self.n1 = n1
         self.roznica = roznica
         self.ilosc = ilosc
     def wyswietl_dane(self):
         print(self.n1, " ", self.roznica, " ", self.ilosc)
     def pobierz_paramety(self):
         print("Podaj parametry: ")
         self.n1 = int(input("n1: "))
         self.roznica = int(input("roznica: "))
         self.ilosc = int(input("ilosc: "))
     def policz_sume(self):
         suma = ((((2*self.n1)+((self.ilosc - 1)*self.roznica))/2)*self.ilosc)
         print(suma)

ciag = Ciagi(2,1,5)
ciag.wyswietl_dane()
ciag.pobierz_paramety()
ciag.policz_sume()
