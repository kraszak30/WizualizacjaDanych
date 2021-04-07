slownik = {'kefir':'szt', 'chleb':'szt', 'ziemniaki':'kg', 'ser':'kg'}
A = [key for key, value in slownik.items() if value == 'szt']
print(slownik, A)