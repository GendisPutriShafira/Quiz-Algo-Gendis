print("=== PROGRAM KELULUSAN UJIAN MATEMATIKA ===")

# Data mahasiswa dan target nilai
mahasiswa = [
    ("Andi", 70),
    ("Budi", 75),
    ("Citra", 80)
]

# Perulangan untuk setiap mahasiswa
for nama, target in mahasiswa:

    print("\nNama Mahasiswa:", nama)
    print("Target Nilai:", target)

    percobaan = 1
    lulus = False

    # Perulangan maksimal 3 kali
    while percobaan <= 3:

        print("\nPercobaan ke-", percobaan)
        nilai = int(input("Masukkan nilai ujian: "))

        if nilai >= target:
            lulus = True
            print("Nilai mencapai target!")
            break
        else:
            print("Nilai belum mencapai target.")

        percobaan += 1

    # Hasil masing-masing mahasiswa
    print("\nHasil", nama, ":")

    if lulus:
        print(nama, "BERHASIL LULUS!")
        print("Lulus pada percobaan ke-", percobaan)
    else:
        print(nama, "DINYATAKAN TIDAK LULUS setelah 3 kali percobaan.")

    print("--------------------------------")
    
print("\n=== SEMUA MAHASISWA SELESAI DIUJI ===")