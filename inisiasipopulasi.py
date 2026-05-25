import random

# INISIALISASI POPULASI
# Membuat sekumpulan solusi awal secara acak (populasi awal)
# Setiap individu = kromosom = array biner [0,1,0,1,...]
# Gen bernilai 1 = barang dipilih, Gen bernilai 0 = barang tidak dipilih

# Fungsi untuk inisialisasi populasi
def inisialisasi_populasi(jumlah_populasi, jumlah_gen):
    """
    Membuat populasi awal secara acak.
    - jumlah_populasi : banyaknya individu (solusi) yang dibuat
    - jumlah_gen      : panjang kromosom = jumlah barang yang tersedia
    """
    populasi = []
    for i in range(jumlah_populasi):
        # Setiap gen dibangkitkan secara acak: 0 (tidak pilih) atau 1 (pilih)
        kromosom = [random.randint(0, 1) for _ in range(jumlah_gen)]
        populasi.append(kromosom)
    return populasi

# Contoh penggunaan
jumlah_populasi = 10  # Jumlah individu dalam populasi
jumlah_gen = 5        # Jumlah barang (gen) dalam kromosom
populasi_awal = inisialisasi_populasi(jumlah_populasi, jumlah_gen)

# Menampilkan populasi awal
print("Populasi Awal:")
for idx, individu in enumerate(populasi_awal):
    print(f"Individu {idx+1}: {individu}")