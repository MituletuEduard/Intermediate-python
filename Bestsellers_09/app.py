import csv

# Calea către fișierele tale
input_path = "C:\\Python course\\Intermediate python\\Bestsellers_09\\Bestseller - Sheet1.csv"
output_path = "C:\\Python course\\Intermediate python\\Bestsellers_09\\bestseller_info.csv"

best_selling_book = None
max_sales = -1

# 1. Citim datele și găsim cel mai bine vândută carte
with open(input_path, 'r', encoding='utf8') as file:
    csv_reader = csv.reader(file)

    # Sărim peste header (prima linie)
    header = next(csv_reader)

    for row in csv_reader:
        # Presupunem că 'Sales in millions' este pe coloana cu indexul 4
        # Curățăm datele în caz că există spații libere
        try:
            current_sales = float(row[4])
            if current_sales > max_sales:
                max_sales = current_sales
                best_selling_book = row
        except (ValueError, IndexError):
            continue

# 2. Scriem rezultatul în noul fișier
if best_selling_book:
    # Pregătim datele (Titlu, Autor, Gen, Vânzări)
    # Extrage indexurile corespunzătoare din structura CSV-ului tău
    data_to_write = [
        ["Title", "Author", "Genre", "Sales"],
        [best_selling_book[0], best_selling_book[1],
            best_selling_book[2], best_selling_book[4]]
    ]

    with open(output_path, 'w', newline='', encoding='utf8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data_to_write)

    print(f"Gata! Bestseller-ul a fost salvat: {best_selling_book[0]}")
