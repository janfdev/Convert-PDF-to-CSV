import pdfplumber
import csv

# Nama file PDF yang akan dikonversi
pdf_file = "data.pdf"
# Nama file CSV hasil output
csv_file = "data.csv"

# Membuka file PDF menggunakan pdfplumber
with pdfplumber.open(pdf_file) as pdf:
    # Menyiapkan list untuk menyimpan data tabel
    data = []

    # Loop melalui setiap halaman PDF
    for page in pdf.pages:
        # Mendeteksi tabel di halaman
        table = page.extract_table()
        
        # Menambahkan data tabel ke list jika ada
        if table:
            data.extend(table)

# Menyimpan data ke dalam file CSV
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Konversi selesai! File CSV disimpan sebagai '{csv_file}'.")
