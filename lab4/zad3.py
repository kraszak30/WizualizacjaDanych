with open("C:/Users/krasz/Dysk Google/Informatyka/semestr IV/Wizualizacja Danych/lab 4/zad3.txt", "w+") as plik:
    plik.write("pierwsza linijka nowego pliku" + "\n")
    plik.write("druga linijka tekstu")
with open("C:/Users/krasz/Dysk Google/Informatyka/semestr IV/Wizualizacja Danych/lab 4/zad3.txt", "r") as plik:
    for a in plik:
        print(a)
plik.close()