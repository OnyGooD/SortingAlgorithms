import random
import string

f = open("ki.txt","a",encoding="utf-8")
lines = f.writelines

def prGreen(szoveg): print("\033[92m {}\033[00m".format(szoveg))
def prYellow(szoveg): print("\033[93m {}\033[00m".format(szoveg))
def prRed(szoveg): print("\033[91m {}\033[00m".format(szoveg))

lehetoseg = int(input("   ______                           __          ___        ________              __  \n  / ____/__  ____  ___  _________ _/ /____     ( _ )      / ____/ /_  ___  _____/ /__\n / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ _ \   / __ \/|   / /   / __ \/ _ \/ ___/ //_/\n/ /_/ /  __/ / / /  __/ /  / /_/ / /_/  __/  / /_/  <   / /___/ / / /  __/ /__/ ,<   \n\____/\___/_/ /_/\___/_/   \__,_/\__/\___/   \____/\/   \____/_/ /_/\___/\___/_/|_|  \n                                                                                     \n ( 1 ) --> Generate Random Number \n ( 2 ) --> Generate Random Text \n ( 3 ) --> Check Random Number \n ( 4 ) --> Check Random Text \n What do you want? $: "))
match lehetoseg:
    case 1:
        hatar1_case1 = int(input("Specify the starting number: "))
        hatar2_case1 = int(input("Specify the ending number: "))
        db1_case1 = int(input("Specify how many numbers there should be: "))

        random_szamok_case1 = [random.randint(hatar1_case1, hatar2_case1) for _ in range(db1_case1)]

        with open("ki.txt", "w") as f:
            for idx_case1, szam_case1 in enumerate(random_szamok_case1):
                if idx_case1 < len(random_szamok_case1) - 1:
                    f.write(f"{szam_case1};")
                else:
                    f.write(f"{szam_case1}")

        prGreen("The Random Generated Number file writing was successful!")

    case 2:
        abc_case2 = string.ascii_lowercase + string.ascii_uppercase

        number_of_strings_case2 = int(input("Specify how many strings there should be: "))

        random_strings_case2 = []
        for _ in range(number_of_strings_case2):
            string_length_case2 = random.randint(1, 20)
            random_string_case2 = ''.join(random.choice(abc_case2) for _ in range(string_length_case2))
            random_strings_case2.append(random_string_case2)

        with open("ki.txt", "w") as f:
            for i_case2, s_case2 in enumerate(random_strings_case2):
                if i_case2 == len(random_strings_case2) - 1:
                    f.write(f"{s_case2}")
                else:
                    f.write(f"{s_case2};")

        prGreen("The Random Generated Text file writing was successful!")

    case 3:
        fajl_nev = 'ki.txt'
        min_ertek = int(input("Specify the minimum limit: "))
        max_ertek = int(input("Specify the maximum limit: "))
        darabszam = int(input("Specify how many numbers there are: "))

        
        with open(fajl_nev, 'r') as file:
            sor = file.readline().strip()
            szamok = list(map(int, sor.split(';')))

            if len(szamok) != darabszam:
                prRed(f"The number of numbers does not match the required amount: there are {len(szamok)} instead of {darabszam}.")
            else:
                minden_megfelel = True
                for szam in szamok:
                    if szam < min_ertek or szam > max_ertek:
                        minden_megfelel = False
                        prRed(f"The number {szam} does not meet the limits ({min_ertek}, {max_ertek}).")

                if minden_megfelel:
                    prGreen(f"All numbers are within {min_ertek} and {max_ertek}.")

    case 4:
        number_of_strings = int(input("Specify how many strings there are: "))

        with open("ki.txt", "r", encoding="utf-8") as file:
            strings = [s.strip() for s in file.read().split(";",) if not s.strip().isdigit()]  # Csak a nem szám karakterláncokat vizsgálja

            if len(strings) != number_of_strings:
                prRed(f"The number of strings does not match the required amount: there are {len(strings)} instead of {number_of_strings}.")
            else:
                for s in strings:
                    if not (0 <= len(s) <= 20):
                        prRed(f"String: '{s}' is not valid -- It is not between 0 and 20 characters long")
                    else:
                        prGreen(f"String: '{s}' is valid")
