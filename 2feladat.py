# 1. Beolvasás
file_name = 'ki.txt'

try:
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.read().split(';')  # A ';' karakter alapján választjuk szét az adatokat
        data = [item.strip() for item in data]  # Eltávolítjuk a felesleges szóközöket
except FileNotFoundError:
    print(f"A {file_name} fájl nem található!")
    data = None

if data is not None:
    # 2. Adattípus eldöntése
    if all(item.isdigit() for item in data):
        adat_tipus = 'szamok'
    elif all(item.isalpha() for item in data):
        adat_tipus = 'szovegek'
    else:
        print("Hiba: A fájl vegyesen tartalmaz számokat és szövegeket, vagy helytelen formátumú adatokat!")
        adat_tipus = None

    if adat_tipus is not None:
        # 3. Rendezési irány kiválasztása
        irany = input("Kérem válassza ki a rendezés irányát (n - növekvő, c - csökkenő): ").lower()
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

        print("Rendezett lista:", data)

        # 5. Új elem beillesztése
        uj_elem = input("Adjon meg egy új elemet (szám vagy szöveg): ")

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
                print("Hiba: A megadott új elem nem szám!")
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
                print("Hiba: A megadott új elem nem szöveg!")

        print("Új rendezett lista:", data)

        # 6. Visszaírás a fájlba
        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(';'.join(str(item) for item in data))  # A listát ';' karakterrel választjuk el
            print(f"A rendezett lista sikeresen kiírva a {file_name} fájlba!")
        except Exception as e:
            print(f"Hiba történt a fájl írásakor: {e}")
