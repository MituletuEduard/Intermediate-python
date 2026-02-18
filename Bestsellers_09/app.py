import csv

# File paths
input_path = "C:\\Python course\\Intermediate python\\Bestsellers_09\\Bestseller - Sheet1.csv"
output_path = "C:\\Python course\\Intermediate python\\Bestsellers_09\\bestseller_info.csv"

best_selling_book = None
max_sales = -1

# Read the CSV file
with open(input_path, 'r', encoding='utf8') as file:
    csv_reader = csv.reader(file)

    # Skip the header row
    header = next(csv_reader)
    # Iterate through the rows to find the best-selling book
    for row in csv_reader:
        try:
            current_sales = float(row[4])
            if current_sales > max_sales:
                max_sales = current_sales
                best_selling_book = row
        except (ValueError, IndexError):
            continue

# Write the best-selling book information to a new CSV file
if best_selling_book:
    data_to_write = [
        ["Title", "Author", "Genre", "Sales"],
        [best_selling_book[0], best_selling_book[1],
            best_selling_book[2], best_selling_book[4]]
    ]
    # Write the data to the output CSV file
    with open(output_path, 'w', newline='', encoding='utf8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data_to_write)

    print(f"Gata! Bestseller-ul a fost salvat: {best_selling_book[0]}")
