import random
f = open("ki.txt","a",encoding="utf-8")
lines = f.writelines
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

lehetoseg = int(input("   ___                       _                    ___ _           _  \n  / __|___ _ _  ___ _ _ __ _| |_ ___   ___ _ _   / __| |_  ___ __| |__\n | (_ / -_) ' \/ -_) '_/ _` |  _/ -_) / _ \ '_| | (__| ' \/ -_) _| / /\n  \___\___|_||_\___|_| \__,_|\__\___| \___/_|    \___|_||_\___\__|_\_\ \n ( 1 ) --> Random Number Generator \n ( 2 ) --> Random Text Generator \n ( 3 ) --> Random Number Check \n ( 4 ) --> Random Text Check \n What do you want? $: "))
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

        # Írás a fájlba utolsó pontosvessző nélkül
        with open("ki.txt", "w") as f:
            for i, s in enumerate(random_strings):
                if i == len(random_strings) - 1:  # ha ez az utolsó string
                    f.write(f"{s}")
                    print(f"{s}")
                else:
                    f.write(f"{s};")
                    print(f"{s};")

    case 3:
        fajl_nev = 'ki.txt'
        min_ertek = int(input("Add meg a minimum határt: "))
        max_ertek = int(input("Add meg a maximum határt: "))
        darabszam = int(input("Add meg a számok számát, amit vársz: "))

        
        with open(fajl_nev, 'r') as file:
            sor = file.readline().strip()  # Egy sor beolvasása
            szamok = list(map(int, sor.split(';')))  # Számok listává alakítása

            # Darabszám ellenőrzése
            if len(szamok) != darabszam:
                print(f"A számok száma nem felel meg a kívántnak: {darabszam} helyett {len(szamok)}.")
            else:
                # Határok ellenőrzése
                minden_megfelel = True
                for szam in szamok:
                    if szam < min_ertek or szam > max_ertek:
                        minden_megfelel = False
                        print(f"A(z) {szam} nem felel meg a határoknak ({min_ertek}, {max_ertek}).")

                if minden_megfelel:
                    print(f"Minden szám {min_ertek} és {max_ertek} között van.")

            # def ellenoriz(nev, minimum, maximum, darabszam):
            #     with open(nev, 'r') as file:
            #         sor = file.readline().strip()  # Egy sor beolvasása a fájlból
            #         szamok = list(sor.split(';'))  # Számok beolvasása és konvertálása

            #         print(f"A fájlban {len(szamok)} szám található.")

            #         # Ellenőrizzük, hogy a fájlban lévő számok száma megegyezik-e a megadott darabszámmal
            #         match len(szamok):
            #             case 0:
            #                 print("A fájl üres.")
            #             case szam if szam != darabszam:
            #                 print(f"A számok száma nem felel meg a kívántnak: {darabszam} helyett {szam}.")
            #             case _:
            #                 # Ellenőrizzük, hogy minden szám a megadott határok között van-e
            #                 megfelel = all(minimum <= szam <= maximum for szam in szamok)
            #                 if megfelel:
            #                     print(f"Minden szám {minimum} és {maximum} között van.")
            #                 else:
            #                     print(f"Van olyan szám, ami nem felel meg a határoknak ({minimum}, {maximum}).")

            # fajl_nev = 'ki.txt'
            # min_ertek = int(input("Add meg a minimum határt: "))
            # max_ertek = int(input("Add meg a maximum határt: "))
            # darabszam = int(input("Add meg a számok számát, amit vársz: "))

            # ellenoriz(fajl_nev, min_ertek, max_ertek, darabszam)

        # lehetoseg3_hatar1 = int(input("Add meg melyik számtól kezdődött: "))
        # lehetoseg3_hatar2 = int(input("Add meg melyik számmal végződött: "))
        # lehetoseg3_darab = int(input("Add meg hany legyen: "))
        # f = open("ki.txt","r",encoding="utf-8")
        # lines = f.readlines
        # numbers = []
        # for t in lines:
        #     t = t.strip()
        #     parts = t.split(';')
        #     numbers.append({
        #         "num":int(parts),
        #         })
        # for i in range(1):
        #     if (numbers['num']) >= lehetoseg3_hatar1 and (numbers['num']) <= lehetoseg3_hatar2:
        #         print("minden okes")
            

            

        # for num in lines:
        #     numbers = [
        #         f.read().strip().split(";")
        #     ]

        # with open("ki.txt", "r", encoding="utf-8") as f:
        #     for num in numbers:
        #         if not (lehetoseg3_hatar1 <= num <= lehetoseg3_hatar2):
        #             print(f"{num} is not within the range [{lehetoseg3_hatar1}, {lehetoseg3_hatar2}]")
        #         if len(numbers) != lehetoseg3_darab:
        #             print(f"The number of generated numbers is not {lehetoseg3_darab}")

    case 4:
        number_of_strings = int(input("Hány szöveg legyen?: "))
        with open("ki.txt", "r", encoding="utf-8") as file:
            strings = [s.strip() for s in file.read().split(";")]
            
            # Check if the number of strings matches the expected value
            if len(strings) != (number_of_strings):
                print(f"The number of generated strings is not {number_of_strings}")
            else:
                # Check if each string has a length between 1 and 20
                for s in strings:
                    if not (0 <= len(s) <= 20):
                        print(f"The length of string '{s}' is not within the range [0, 20]")
                    else:
                        print(f"String '{s}' is valid")

        # lehetoseg4_db = int(input("Hány szöveg legyen?: "))
        # with open("ki.txt", "r", encoding="utf-8") as f:
        #     strings = [str(x) for x in f.read().strip().split(";")]
        #     if len(strings) != lehetoseg4_db:
        #         print(f"The number of generated strings is not {lehetoseg4_db}")
        #     for s in strings:
        #         if not (1 <= len(s) <= 20):
        #             print(f"The length of string '{s}' is not within the range [1, 20]")
