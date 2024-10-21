#Beolvasás
file_name = 'ki.txt'

def prGreen(szoveg): print("\033[92m {}\033[00m".format(szoveg))
def prYellow(szoveg): print("\033[93m {}\033[00m".format(szoveg))
def prRed(szoveg): print("\033[91m {}\033[00m".format(szoveg))

try:
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.read().split(';')  # A ';' karakter alapján választjuk szét az adatokat
        data = [item.strip() for item in data]  # Eltávolítjuk a felesleges szóközöket
except FileNotFoundError:
    prRed(f"File {file_name} not found!")
    data = None

if data is not None:
    #Adattípus eldöntése
    if all(item.isdigit() for item in data):
        adat_tipus = 'szamok'
        prYellow("   _   __                __                 _____            __  _            \n   / | / /_  ______ ___  / /_  ___  _____   / ___/____  _____/ /_(_)___  ____ _\n  /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/   \__ \/ __ \/ ___/ __/ / __ \/ __ `/\n / /|  / /_/ / / / / / / /_/ /  __/ /      ___/ / /_/ / /  / /_/ / / / / /_/ / \n/_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/      /____/\____/_/   \__/_/_/ /_/\__, /  \n                                                                      /____/   \n")
    elif all(item.isalpha() for item in data):
        adat_tipus = 'szovegek'
        prYellow(" ______          __     _____            __  _            \n /_  __/__  _  __/ /_   / ___/____  _____/ /_(_)___  ____ _\n  / / / _ \| |/_/ __/   \__ \/ __ \/ ___/ __/ / __ \/ __ `/\n / / /  __/>  </ /_    ___/ / /_/ / /  / /_/ / / / / /_/ / \n/_/  \___/_/|_|\__/   /____/\____/_/   \__/_/_/ /_/\__, /  \n                                                  /____/   \n")
    else:
        prRed("Error: The file contains a mix of numbers and text, or data in an incorrect format!")
        adat_tipus = None

    if adat_tipus is not None:
        #Rendezési irány kiválasztása
        irany = input("Please select the sorting order (a - ascending, d - descending): ").lower()
        novekvo = True if irany == 'a' else False

        #Rendezés elvégzése
        if adat_tipus == 'szamok':
            data = [int(x) for x in data]  # Konvertáljuk számokká

            n = len(data)
            for i in range(n-1):
                for j in range(i+1, n):
                    if novekvo:
                        if data[i] > data[j]:
                            data[i], data[j] = data[j], data[i]
                    else:
                        if data[i] < data[j]:
                            data[i], data[j] = data[j], data[i]
        else:
            n = len(data)
            for i in range(n-1):
                for j in range(i+1, n):
                    if novekvo:
                        if len(data[i]) > len(data[j]) or (len(data[i]) == len(data[j]) and data[i] > data[j]):
                            data[i], data[j] = data[j], data[i]
                    else:
                        if len(data[i]) < len(data[j]) or (len(data[i]) == len(data[j]) and data[i] < data[j]):
                            data[i], data[j] = data[j], data[i]

        prGreen(f"Ordered list:  {data}")

        #Új elem beillesztése
        uj_elem = input("Please enter a new item (number or text): ")

        if adat_tipus == 'szamok':
            if uj_elem.isdigit():
                uj_elem = int(uj_elem)
                data.append(uj_elem)
                
                n = len(data)
                for i in range(n-1):
                    for j in range(i+1, n):
                        if novekvo:
                            if data[i] > data[j]:
                                data[i], data[j] = data[j], data[i]
                        else:
                            if data[i] < data[j]:
                                data[i], data[j] = data[j], data[i]
            else:
                prRed("Error: The specified new item is not a number!")
        else:
            if uj_elem.isalpha():
                data.append(uj_elem)

                n = len(data)
                for i in range(n-1):
                    for j in range(i+1, n):
                        if novekvo:
                            if len(data[i]) > len(data[j]) or (len(data[i]) == len(data[j]) and data[i] > data[j]):
                                data[i], data[j] = data[j], data[i]
                        else:
                            if len(data[i]) < len(data[j]) or (len(data[i]) == len(data[j]) and data[i] < data[j]):
                                data[i], data[j] = data[j], data[i]
            else:
                prRed("Error: The specified new item is not text!")

        prGreen(f"New ordered list:  {data}")

        #Visszaírás a fájlba
        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(';'.join(str(item) for item in data))  # A listát ';' karakterrel választjuk el
            prGreen(f"The sorted list has been successfully written to the {file_name} file!")
        except Exception as e:
            prRed(f"An error occurred while writing the file: {e}")
