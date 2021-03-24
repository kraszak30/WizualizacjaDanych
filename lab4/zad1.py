import random

plik = open("C:/Users/krasz/Dysk Google/Informatyka/semestr IV/Wizualizacja Danych/lab 4/zad1.txt", "w+")
i=1
while i <= 15:
    plik.write(str(random.randint(0,30)*2) + " ")
    i += 1
plik.close()