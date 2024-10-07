import random
import string
f = open("ki.txt","a",encoding="utf-8")
lines = f.writelines

lehetoseg = int(input("   ______                           __          ___        ________              __  \n  / ____/__  ____  ___  _________ _/ /____     ( _ )      / ____/ /_  ___  _____/ /__\n / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ _ \   / __ \/|   / /   / __ \/ _ \/ ___/ //_/\n/ /_/ /  __/ / / /  __/ /  / /_/ / /_/  __/  / /_/  <   / /___/ / / /  __/ /__/ ,<   \n\____/\___/_/ /_/\___/_/   \__,_/\__/\___/   \____/\/   \____/_/ /_/\___/\___/_/|_|  \n                                                                                     \n ( 1 ) --> Generate Random Number \n ( 2 ) --> Generate Random Text \n ( 3 ) --> Check Random Number \n ( 4 ) --> Check Random Text \n What do you want? $: "))
match lehetoseg:
    case 1:
        hatar1_case1 = int(input("Add meg melyik számtól kezdődjön: "))
        hatar2_case1 = int(input("Add meg melyik számmal végződjön: "))
        db1_case1 = int(input("Add meg hány szám legyen: "))

        random_szamok_case1 = [random.randint(hatar1_case1, hatar2_case1) for _ in range(db1_case1)]

        with open("ki.txt", "a") as f:
            for idx_case1, szam_case1 in enumerate(random_szamok_case1):
                if idx_case1 < len(random_szamok_case1) - 1:
                    f.write(f"{szam_case1};")
                else:
                    f.write(f"{szam_case1}\n")

    case 2:
        abc_case2 = string.ascii_lowercase + string.ascii_uppercase

        number_of_strings_case2 = int(input("Hány szöveg legyen?: "))

        random_strings_case2 = []
        for _ in range(number_of_strings_case2):
            string_length_case2 = random.randint(1, 20)
            random_string_case2 = ''.join(random.choice(abc_case2) for _ in range(string_length_case2))
            random_strings_case2.append(random_string_case2)

        with open("ki.txt", "a") as f:
            for i_case2, s_case2 in enumerate(random_strings_case2):
                if i_case2 == len(random_strings_case2) - 1:
                    f.write(f"{s_case2}\n")
                else:
                    f.write(f"{s_case2};")

    case 3:
        fajl_nev = 'ki.txt'
        min_ertek = int(input("Add meg a minimum határt: "))
        max_ertek = int(input("Add meg a maximum határt: "))
        darabszam = int(input("Add meg a számok számát, amit vársz: "))

        
        with open(fajl_nev, 'r') as file:
            sor = file.readline().strip()
            szamok = list(map(int, sor.split(';')))

            if len(szamok) != darabszam:
                print(f"A számok száma nem felel meg a kívántnak: {darabszam} helyett {len(szamok)} szám van.")
            else:
                minden_megfelel = True
                for szam in szamok:
                    if szam < min_ertek or szam > max_ertek:
                        minden_megfelel = False
                        print(f"A(z) {szam} nem felel meg a határoknak ({min_ertek}, {max_ertek}).")

                if minden_megfelel:
                    print(f"Minden szám {min_ertek} és {max_ertek} között van.")

    case 4:
        number_of_strings = int(input("Hány szöveg legyen?: "))

        with open("ki.txt", "r", encoding="utf-8") as file:
            strings = [s.strip() for s in file.read().split(";") if not s.strip().isdigit()]  # Csak a nem szám karakterláncokat vizsgálja

            if len(strings) != number_of_strings:
                print(f"A szövegek száma nem felel meg a kívántnak: {number_of_strings} helyett {len(strings)} szöveg van.")
            else:
                for s in strings:
                    if not (0 <= len(s) <= 20):
                        print(f"Szöveg: '{s}' nem érvényes -- Nem 0 és 20 karakter között van")
                    else:
                        print(f"Szöveg: '{s}' érvényes")
