class robaczek:
    x = 0
    y = 0
    krok = 1
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
    def idz_w_gore(self, ile_krokow):
        self.y = self.y + (self.krok * ile_krokow)
    def idz_w_dol(self, ile_krokow):
        self.y = self.y - (self.krok * ile_krokow)
    def idz_w_lewo(self, ile_krokow):
        self.x = self.x - (self.krok * ile_krokow)
    def idz_w_prawo(self, ile_krokow):
        self.x = self.x + (self.krok * ile_krokow)
    def pokaz_gdzie_jestes(self):
        print("x= ", self.x, "y= ", self.y)

gra = robaczek(0, 0, 1)
gra.pokaz_gdzie_jestes()
gra.idz_w_gore(1)
gra.idz_w_lewo(3)
gra.idz_w_gore(1)
gra.idz_w_prawo(5)
gra.pokaz_gdzie_jestes()

