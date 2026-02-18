import csv

filename = "packing_list.csv"

data = [
    ['Item', 'Quantity'],
    ['Blender', 2],
    ['Posters', 30],
    ['Shoes', 2]
]

try:
    # Încercăm să deschidem și să citim fișierul
    with open(filename, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        print("--- Conținutul Listei de Împachetat ---")
        for row in csv_reader:
            print(row)

except FileNotFoundError:
    # Dacă fișierul nu există, îl creăm
    print("Packing list file not found. Creating a new one.")

    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        # Folosim .writerows() pentru a scrie toată lista 'data' deodată
        csv_writer.writerows(data)

    print("Fișierul a fost creat cu succes!")
