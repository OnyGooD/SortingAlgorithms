import random
f = open("ki.txt","a",encoding="utf-8")
lines = f.writelines
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

lehetoseg = int(input("   ___                       _                    ___ _           _  \n  / __|___ _ _  ___ _ _ __ _| |_ ___   ___ _ _   / __| |_  ___ __| |__\n | (_ / -_) ' \/ -_) '_/ _` |  _/ -_) / _ \ '_| | (__| ' \/ -_) _| / /\n  \___\___|_||_\___|_| \__,_|\__\___| \___/_|    \___|_||_\___\__|_\_\ \n ( 1 ) --> Random Number Generator \n ( 2 ) --> Random Text Generator \n ( 3 ) --> Random Number Check \n ( 4 ) --> Rnadom Text Check \n What do you want? $: "))
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

        with open("ki.txt", "r", encoding="utf-8") as f:
            numbers = [int(x) for x in f.read().strip().split(";")]
            for num in numbers:
                if not (lehetoseg3_hatar1 <= num <= lehetoseg3_hatar2):
                    print(f"{num} is not within the range [{lehetoseg3_hatar1}, {lehetoseg3_hatar2}]")
                if len(numbers) != lehetoseg3_darab:
                    print(f"The number of generated numbers is not {lehetoseg3_darab}")

    case 4:
        lehetoseg4_db = int(input("Hány szöveg legyen?: "))
        with open("ki.txt", "r", encoding="utf-8") as f:
            strings = [x for x in f.read().strip().split(";")]
            if len(strings) != lehetoseg4_db:
                print(f"The number of generated strings is not {lehetoseg4_db}")
            for s in strings:
                if not (1 <= len(s) <= 20):
                    print(f"The length of string '{s}' is not within the range [1, 20]")