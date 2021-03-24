class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jendostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        print(self.nazwa_produktu, " ", self.ilosc, " ", self.jendostka_miary, " ", self.cena_jed)
    def ile_produktu(self):
        print(self.ilosc, " ", self.jendostka_miary)
    def ile_kosztuje(self):
        cena = self.ilosc*self.cena_jed
        print(cena)
ziemniaki = NaZakupy('ziemniaki', 13, 'kg', 1.2)
ziemniaki.wyswietl_produkt()
ziemniaki.ile_produktu()
ziemniaki.ile_kosztuje()