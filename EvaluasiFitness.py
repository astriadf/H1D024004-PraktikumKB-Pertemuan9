# EVALUASI FITNESS
# Mengukur seberapa "baik" setiap individu (kromosom) sebagai solusi.
# Dalam Knapsack Problem:
#   - Fitness = total HARGA barang yang dipilih
#   - Jika total BOBOT melebihi kapasitas tas -> fitness = 0 (penalti)

# Data barang (nama, harga, bobot)
barang = [
    ("Barang1", 60, 10),
    ("Barang2", 100, 20),
    ("Barang3", 120, 30),
    ("Barang4", 90, 25),
    ("Barang5", 70, 15)
]

kapasitas_tas = 50  # Kapasitas maksimum tas (dalam satuan bobot)

# Fungsi untuk menghitung nilai fitness
def hitung_fitness(kromosom, barang, kapasitas_tas):
    """
    Menghitung nilai fitness sebuah kromosom.
    - Jika gen[i] == 1, barang ke-i dimasukkan ke tas
    - Akumulasi total harga dan total bobot barang yang dipilih
    - Jika total bobot > kapasitas -> return 0 (solusi tidak valid)
    - Jika total bobot <= kapasitas -> return total harga (solusi valid)
    """
    total_harga = 0
    total_bobot = 0

    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_harga += barang[i][1]   # Tambahkan harga barang ke-i
            total_bobot += barang[i][2]   # Tambahkan bobot barang ke-i

    if total_bobot > kapasitas_tas:
        return 0  # Penalti jika melebihi kapasitas
    else:
        return total_harga

# Definisi contoh populasi awal
populasi_awal = [
    [1, 0, 1, 0, 1],  # Contoh kromosom individu
    [0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1],
    # Tambahkan lebih banyak individu sesuai kebutuhan
]

# Contoh penggunaan
fitness_populasi = [hitung_fitness(individu, barang, kapasitas_tas) for individu in populasi_awal]

# Menampilkan nilai fitness
print("\nNilai Fitness:")
for idx, fitness in enumerate(fitness_populasi):
    print(f"Individu {idx+1}: Fitness = {fitness}")