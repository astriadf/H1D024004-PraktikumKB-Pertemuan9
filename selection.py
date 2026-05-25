import random

# SELEKSI
# Memilih individu terbaik dari populasi untuk menjadi "orang tua" (parent)yang akan menghasilkan keturunan di generasi berikutnya.
#
# Dua metode seleksi yang digunakan:
# 1. Roulette Wheel Selection -> probabilitas dipilih proporsional terhadap fitness
# 2. Tournament Selection     -> k individu acak bertanding, fitness tertinggi menang

# Fungsi untuk Roulette Wheel Selection
def roulette_wheel_selection(populasi, fitness_populasi):
    """
    Memilih individu seperti memutar roda roulette.
    - Individu dengan fitness lebih tinggi = sektor lebih besar di roda
    - Semakin besar sektor = semakin besar peluang terpilih
    - Tetapi individu dengan fitness rendah tetap punya kesempatan terpilih

    Langkah:
    1. Hitung total fitness semua individu
    2. Hitung probabilitas masing-masing individu (fitness / total_fitness)
    3. Buat probabilitas kumulatif
    4. Buat bilangan acak r antara 0-1
    5. Pilih individu pertama yang probabilitas kumulatifnya >= r
    """
    total_fitness = sum(fitness_populasi)

    # Jika semua fitness = 0, pilih individu secara acak (hindari pembagian nol)
    if total_fitness == 0:
        idx = random.randrange(len(populasi))
        return populasi[idx], idx  # Mengembalikan individu dan indeksnya

    # Hitung probabilitas seleksi setiap individu
    probabilitas = [fitness / total_fitness for fitness in fitness_populasi]

    # Hitung probabilitas kumulatif (akumulasi dari kiri ke kanan)
    kumulatif_prob = []
    kumulatif = 0
    for p in probabilitas:
        kumulatif += p
        kumulatif_prob.append(kumulatif)

    # Putar "roda" dengan bilangan acak
    r = random.random()
    for i, kum_prob in enumerate(kumulatif_prob):
        if r <= kum_prob:
            return populasi[i], i  # Mengembalikan individu dan indeksnya

    # Fallback: kembalikan individu terakhir jika tidak ada yang terpilih
    return populasi[-1], len(populasi) - 1


# Fungsi untuk Tournament Selection
def tournament_selection(populasi, fitness_populasi, k=3):
    """
    Memilih individu melalui mekanisme turnamen.
    - Pilih k individu secara acak dari populasi sebagai peserta turnamen
    - Individu dengan fitness tertinggi di antara peserta = pemenang = parent
    - Semakin besar k -> tekanan seleksi semakin tinggi (yang terkuat lebih sering menang)
    """
    # Sesuaikan k jika populasi lebih kecil dari k
    if len(populasi) < k:
        k = len(populasi)

    # Pilih k peserta secara acak (tanpa pengulangan)
    peserta_indices = random.sample(range(len(populasi)), k)
    peserta = [(populasi[i], fitness_populasi[i], i) for i in peserta_indices]

    # Urutkan peserta dari fitness tertinggi ke terendah
    peserta.sort(key=lambda x: x[1], reverse=True)

    # Kembalikan pemenang (fitness tertinggi)
    return peserta[0][0], peserta[0][2]  # Mengembalikan individu dan indeksnya


# Definisikan populasi awal dan fitness_populasi
populasi_awal = ['individu1', 'individu2', 'individu3', 'individu4']
fitness_populasi = [10, 20, 30, 40]

# Membuat salinan populasi dan fitness untuk dimodifikasi
available_populasi = populasi_awal.copy()
available_fitness = fitness_populasi.copy()

# Contoh penggunaan
# Memilih Parent 1 menggunakan Roulette Wheel Selection
parent1, idx1 = roulette_wheel_selection(available_populasi, available_fitness)

# Menghapus parent1 dari daftar available_populasi dan available_fitness
del available_populasi[idx1]
del available_fitness[idx1]

# Memilih Parent 2 menggunakan Tournament Selection
parent2, idx2 = tournament_selection(available_populasi, available_fitness)

# Menghapus parent2 dari daftar available_populasi dan available_fitness
del available_populasi[idx2]
del available_fitness[idx2]

print("\nParent Terpilih:")
print(f"Parent 1: {parent1}")
print(f"Parent 2: {parent2}")