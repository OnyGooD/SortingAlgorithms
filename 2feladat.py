# Fájl beolvasása
data = []
with open("ki.txt", "r", encoding="utf-8") as f:
    for line in f:
        # Sorok feldolgozása, az adatok pontosvesszővel (;) vannak elválasztva
        data.extend(line.strip().split(';'))

# Típus eldöntése
if all(item.replace('.', '', 1).isdigit() for item in data):
    data = list(map(float, data))  # Számok esetén lebegőpontosra konvertálás
    data_type = 'numbers'
elif all(item.isalpha() for item in data):
    data_type = 'strings'  # Szövegek esetén
else:
    print("Hibás adat az állományban!")
    exit()

# Rendezési irány választása
order = input("Rendezés növekvő (n) vagy csökkenő (c) sorrendben? (n/c): ")

if order == 'n':
    reverse = False
elif order == 'c':
    reverse = True
else:
    print("Érvénytelen választás!")
    exit()

# Rendezési algoritmus választása
alg_choice = input("Válassz rendezési algoritmust (1: Cserés, 2: Buborék, 3: Beszúrásos, 4: Minimumkiválasztás, 5: Merge Sort): ")

# Cserés rendezés
if alg_choice == '1':
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if (data[i] > data[j] and not reverse) or (data[i] < data[j] and reverse):
                data[i], data[j] = data[j], data[i]

# Buborékrendezés
elif alg_choice == '2':
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if (data[j] > data[j + 1] and not reverse) or (data[j] < data[j + 1] and reverse):
                data[j], data[j + 1] = data[j + 1], data[j]

# Beszúrásos rendezés
elif alg_choice == '3':
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and ((data[j] > key and not reverse) or (data[j] < key and reverse)):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

# Minimumkiválasztásos rendezés
elif alg_choice == '4':
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if (data[j] < data[min_idx] and not reverse) or (data[j] > data[min_idx] and reverse):
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]

# Merge sort
elif alg_choice == '5':
    def merge_sort_internal(lst):
        if len(lst) > 1:
            mid = len(lst) // 2
            left_half = lst[:mid]
            right_half = lst[mid:]

            merge_sort_internal(left_half)
            merge_sort_internal(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if (left_half[i] < right_half[j] and not reverse) or (left_half[i] > right_half[j] and reverse):
                    lst[k] = left_half[i]
                    i += 1
                else:
                    lst[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                lst[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                lst[k] = right_half[j]
                j += 1
                k += 1

    merge_sort_internal(data)
else:
    print("Érvénytelen algoritmusválasztás!")
    exit()

print("Rendezett lista:", data)

# Új elem beillesztése
new_item = input("Adj meg egy új elemet, amit be szeretnél illeszteni: ")

if data_type == 'numbers':
    try:
        new_item = float(new_item)
    except ValueError:
        print("Érvénytelen szám!")
        exit()
elif data_type == 'strings':
    if not new_item.isalpha():
        print("Érvénytelen szöveg!")
        exit()

# Új elem beillesztése a megfelelő helyre
for i in range(len(data)):
    if (new_item < data[i] and not reverse) or (new_item > data[i] and reverse):
        data.insert(i, new_item)
        break
else:
    data.append(new_item)

print("Lista az új elem beillesztése után:", data)
