import random
import matplotlib.pyplot as plt
import numpy as np

# Mengimpor fungsi-fungsi dari file lain
from inisiasipopulasi import inisialisasi_populasi
from EvaluasiFitness import hitung_fitness
from selection import roulette_wheel_selection, tournament_selection
from crossover import one_point_crossover, two_point_crossover, uniform_crossover
from mutation import swap_mutation, inversion_mutation, uniform_mutation

# MAIN bertujuan untuk menyelesaikan Knapsack Problem.
#
# Alur kerja Algoritma Genetika:
# 1. Inisialisasi populasi awal secara acak
# 2. Evaluasi fitness setiap individu
# 3. Seleksi parent (Roulette Wheel Selection)
# 4. Crossover -> menghasilkan anak baru (One-Point Crossover)
# 5. Mutasi    -> menjaga keragaman populasi (Swap Mutation)
# 6. Bentuk populasi baru, ulangi dari langkah 2 selama N generasi
# 7. Tampilkan hasil terbaik (barang terpilih + grafik perkembangan fitness)

# Data barang: (nama, nilai, berat)
# Setiap tuple berisi: nama barang, nilai/harga, dan berat/bobot
barang = [
    ("Barang1", 60, 10),
    ("Barang2", 100, 20),
    ("Barang3", 120, 30),
    ("Barang4", 90, 25),
    ("Barang5", 69, 11),
    ("Barang6", 70, 9),
    ("Barang7", 80, 15),
    ("Barang8", 90, 10),
    ("Barang9", 25, 3)
]

def run_ga(jumlah_generasi, jumlah_populasi, prob_crossover, prob_mutasi, kapasitas_tas):
    """
    Menjalankan Algoritma Genetika untuk Knapsack Problem.

    Parameter:
    - jumlah_generasi : berapa kali populasi akan berevolusi
    - jumlah_populasi : jumlah individu (solusi) dalam setiap generasi
    - prob_crossover  : probabilitas crossover terjadi (0.0 - 1.0)
    - prob_mutasi     : probabilitas mutasi terjadi pada setiap anak (0.0 - 1.0)
    - kapasitas_tas   : batas maksimum bobot yang bisa dibawa (penalti jika terlampaui)
    """

    # TAHAP 1: INISIALISASI
    # Menentukan jumlah gen berdasarkan jumlah barang
    jumlah_gen = len(barang)

    # Buat populasi awal secara acak (setiap individu = kromosom biner)
    populasi = inisialisasi_populasi(jumlah_populasi, jumlah_gen)

    # Hitung fitness awal untuk setiap individu
    fitness_populasi = [hitung_fitness(individu, barang, kapasitas_tas) for individu in populasi]

    # List untuk menyimpan nilai fitness terbaik, terburuk, dan rata-rata setiap generasi
    # (digunakan untuk membuat grafik perkembangan fitness)
    best_fitness_list = []
    worst_fitness_list = []
    avg_fitness_list = []
    all_fitness = []  # Menyimpan semua nilai fitness tiap generasi (untuk scatter plot)

    # Variabel untuk menyimpan individu terbaik secara keseluruhan (lintas generasi)
    best_individu = None
    best_fitness_overall = 0

    # TAHAP 2: PROSES EVOLUSI (diulang sebanyak jumlah_generasi)
    for generasi in range(jumlah_generasi):

        # Hitung ulang fitness populasi saat ini
        fitness_populasi = [hitung_fitness(individu, barang, kapasitas_tas) for individu in populasi]

        # Catat statistik fitness generasi ini untuk grafik
        best_fitness = max(fitness_populasi)
        worst_fitness = min(fitness_populasi)
        avg_fitness = sum(fitness_populasi) / len(fitness_populasi)
        best_fitness_list.append(best_fitness)
        worst_fitness_list.append(worst_fitness)
        avg_fitness_list.append(avg_fitness)
        all_fitness.append(fitness_populasi.copy())

        # Simpan individu terbaik dari seluruh generasi yang sudah berjalan
        if best_fitness > best_fitness_overall:
            best_fitness_overall = best_fitness
            index_best = fitness_populasi.index(best_fitness)
            best_individu = populasi[index_best]

        # TAHAP 3: PEMBENTUKAN POPULASI BARU
        new_populasi = []
        used_indices = []

        while len(new_populasi) < jumlah_populasi:

            # SELEKSI: Pilih parent1 menggunakan Roulette Wheel Selection
            # Individu dengan fitness lebih tinggi lebih berpeluang terpilih
            parent1, idx1 = roulette_wheel_selection(populasi, fitness_populasi)
            used_indices.append(idx1)

            # Pastikan parent2 berbeda dari parent1
            available_indices = [i for i in range(len(populasi)) if i not in used_indices]
            if not available_indices:
                # Reset jika semua indeks sudah terpakai
                used_indices = [idx1]
                available_indices = [i for i in range(len(populasi)) if i != idx1]

            # SELEKSI: Pilih parent2 dari sisa individu yang belum dipilih
            parent2, _ = roulette_wheel_selection(
                [populasi[i] for i in available_indices],
                [fitness_populasi[i] for i in available_indices]
            )
            used_indices.append(available_indices[_])

            # CROSSOVER: Gabungkan parent1 & parent2 untuk hasilkan anak
            # Jika bilangan acak < prob_crossover -> lakukan crossover
            # Jika tidak -> anak adalah salinan langsung dari parent
            if random.random() < prob_crossover:
                anak1, anak2 = one_point_crossover(parent1, parent2)
            else:
                anak1, anak2 = parent1[:], parent2[:]

            # MUTASI: Terapkan mutasi pada anak dengan probabilitas prob_mutasi
            # Swap Mutation: tukar dua gen secara acak -> menjaga keragaman populasi
            if random.random() < prob_mutasi:
                anak1 = swap_mutation(anak1)
            if random.random() < prob_mutasi:
                anak2 = swap_mutation(anak2)

            # Tambahkan kedua anak ke populasi baru
            new_populasi.extend([anak1, anak2])

        # Ganti populasi lama dengan populasi baru (generasi berikutnya)
        populasi = new_populasi[:jumlah_populasi]

    # TAHAP 4: VISUALISASI GRAFIK PERKEMBANGAN FITNESS
    # Grafik menunjukkan bagaimana kualitas solusi berkembang dari generasi ke generasi
    plt.figure(figsize=(12, 7))

    # Plot semua nilai fitness individu (titik abu-abu) per generasi
    # Semakin gelap = semakin banyak individu dengan fitness serupa di titik itu
    for i in range(jumlah_generasi):
        x = [i + 1] * len(all_fitness[i])
        y = all_fitness[i]
        plt.scatter(x, y, color='gray', alpha=0.1)

    # Plot garis fitness terbaik (biru), terendah (kuning), dan rata-rata (merah)
    plt.plot(range(1, jumlah_generasi + 1), best_fitness_list, color='blue', label='Fitness Tertinggi')
    plt.plot(range(1, jumlah_generasi + 1), worst_fitness_list, color='yellow', label='Fitness Terendah')
    plt.plot(range(1, jumlah_generasi + 1), avg_fitness_list, color='red', label='Fitness Rata-rata')

    plt.title('Perkembangan Nilai Fitness')
    plt.xlabel('Generasi')
    plt.ylabel('Nilai Fitness')
    plt.legend()
    plt.grid(True)
    plt.show()

    # TAHAP 5: TAMPILKAN HASIL TERBAIK
    # Barang-barang yang terpilih oleh individu terbaik
    selected_items = [barang[i][0] for i in range(len(best_individu)) if best_individu[i] == 1]

    # Hitung nilai fitness dan total bobot dari solusi terbaik
    selected_value = hitung_fitness(best_individu, barang, kapasitas_tas)
    selected_weight = sum([barang[i][2] for i in range(len(best_individu)) if best_individu[i] == 1])

    print(f"Nilai Fitness Terbaik: {selected_value}")
    print(f"Total Bobot: {selected_weight}")
    print("Barang Terpilih:")
    for item in selected_items:
        print(f"- {item}")

# Menjalankan GA dengan konfigurasi parameter berikut:
# - 50 generasi evolusi
# - 20 individu per generasi
# - Peluang crossover 50%
# - Peluang mutasi 10%
# - Kapasitas tas maksimum 50

run_ga(
    jumlah_generasi=50,
    jumlah_populasi=20,
    prob_crossover=0.5,
    prob_mutasi=0.1,
    kapasitas_tas=50
)