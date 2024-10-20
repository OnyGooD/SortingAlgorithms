# 1. Beolvasás
file_name = 'ki.txt'

def prGreen(szoveg): print("\033[92m {}\033[00m".format(szoveg))
#def prYellow(szoveg): print("\033[93m {}\033[00m".format(szoveg))
def prRed(szoveg): print("\033[91m {}\033[00m".format(szoveg))

try:
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.read().split(';')  # A ';' karakter alapján választjuk szét az adatokat
        data = [item.strip() for item in data]  # Eltávolítjuk a felesleges szóközöket
except FileNotFoundError:
    prRed(f"File {file_name} not found!")
    data = None

if data is not None:
    # 2. Adattípus eldöntése
    if all(item.isdigit() for item in data):
        adat_tipus = 'szamok'
    elif all(item.isalpha() for item in data):
        adat_tipus = 'szovegek'
    else:
        prRed("Error: The file contains a mix of numbers and text, or data in an incorrect format!")
        adat_tipus = None

    if adat_tipus is not None:
        # 3. Rendezési irány kiválasztása
        irany = input("Please select the sorting order (a - ascending, d - descending): ").lower()
        novekvo = True if irany == 'n' else False

        # 4. Rendezés elvégzése
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

        prGreen("Ordered list: ", data)

        # 5. Új elem beillesztése
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

        prGreen("New ordered list: ", data)

        # 6. Visszaírás a fájlba
        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(';'.join(str(item) for item in data))  # A listát ';' karakterrel választjuk el
            prGreen(f"The sorted list has been successfully written to the {file_name} file!")
        except Exception as e:
            prRed(f"An error occurred while writing the file: {e}")
