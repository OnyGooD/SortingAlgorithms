import random
f = open("ki.txt","w",encoding="utf-8")
lines = f.writelines
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

lehetoseg = int(input("Kérlek válassz az alábbi lehetőségekből: \n 1-számgenerátor \n 2-szöveg generátor \n 3-számgenerátor ellenőrzése \n 4-szöveg generátor ellenőrzése \n választásod: "))


match lehetoseg:

    case 1:
        def random_generator(db1):
            random_szamok = ([random.randint(hatar1, hatar2) for _ in range(db1)])
            for szam in random_szamok:
                f.write(f"{szam};")
                print(f"{szam};")


        hatar1 = int(input("Add meg melyik számtól kezdődjön: "))
        hatar2 = int(input("Add meg melyik számmal végződjön: "))
        db1 = int(input("Add meg hány szám legyen: "))

        random_generator(db1)

    case 2:
        def generate_string(length):
            return ''.join(random.choice(abc) for _ in range(length))

        def generate_random_strings(number):
            string_lengths = [random.randint(1, 20) for _ in range(number)]
            random_strings = [generate_string(length) for length in string_lengths]
            return random_strings
        number_of_strings = int(input("Hány szöveg legyen?: "))
        random_strings = generate_random_strings(number_of_strings)
        for s in random_strings:
            f.write(f"{s};")
            print(f"{s};")

        generate_random_strings(number_of_strings)

    case 3:
        lehetoseg3_hatar1 = int(input("Add meg melyik számtól kezdődött: "))
        lehetoseg3_hatar2 = int(input("Add meg melyik számmal végződött: "))
        lehetoseg3_darab = int(input("Add meg hany legyen: "))

        for a in ['ki.txt']:
            if int(a) >= int(lehetoseg3_hatar1):
                print(f"{a} nagyobb mint {lehetoseg3_hatar1}")
            elif int(a) <= lehetoseg3_hatar1:
                print("nem jo valami")
            if int(a) <= lehetoseg3_hatar2:
                print(f"nagoyn jo minden, nagyobb nala")
            elif int(a) >= lehetoseg3_hatar2:
                print("valszeg nem jo valami")
            if len(int(a))-lehetoseg3_darab == lehetoseg3_darab:
                print("everything is alr")
            elif len(int(a))-lehetoseg3_darab != lehetoseg3_darab:
                print("nem is anyni karakter van")