import pdfplumber
import csv

# Nama file PDF yang akan dikonversi
pdf_file = "Aljabar_Linear_Matriks.pdf"

# Membuka file PDF menggunakan pdfplumber
with pdfplumber.open(pdf_file) as pdf:
    # Variabel untuk memberi nomor pada file CSV
    table_count = 1
    
    # Loop melalui setiap halaman PDF
    for page_num, page in enumerate(pdf.pages, start=1):
        # Mendeteksi tabel di halaman
        table = page.extract_table()
        
        # Jika ada tabel, buat file CSV baru untuk setiap tabel
        if table:
            csv_filename = f"Aljabar_Linear_Matriks_{table_count}.csv"  # Nama file CSV berdasarkan urutan tabel
            table_count += 1

            # Pastikan header tabel tetap horizontal dengan mengganti newline (\n) dengan spasi
            header = [col.replace("\n", " ") if col else "" for col in table[0]]  # Header diperbaiki
            rows = table[1:]  # Data tabel tanpa header

            # Menulis ke file CSV
            with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                
                # Tulis header yang sudah diperbaiki
                writer.writerow(header)
                
                # Tulis data tabel
                writer.writerows(rows)

            print(f"Tabel dari halaman {page_num} disimpan sebagai '{csv_filename}'.")

print("Konversi selesai!")
