import random

# MUTASI
# Melakukan perubahan kecil secara acak pada kromosom individu.
# Tujuannhya untuk menjaga keragmana genetik populasi agar algoritma tidak terjebak pada solusi lokal yang tidak optimal (premature convergence).
#
# Tiga metode mutasi yang diimplementasikan:
# 1. Swap Mutation      -> tukar posisi dua gen secara acak
# 2. Inversion Mutation -> balik urutan gen dalam segmen tertentu
# 3. Uniform Mutation   -> setiap gen berpeluang dibalik nilainya (0->1 atau 1->0)

# Swap Mutation
def swap_mutation(kromosom):
    # Menukar nilai dua gen yang dipilih secara acak dalam kromosom.
    # Pastikan kromosom adalah list
    kromosom = list(kromosom)  # Konversi ke list jika perlu

    # Pilih dua posisi yang berbeda untuk swap
    posisi1, posisi2 = random.sample(range(len(kromosom)), 2)

    # Melakukan swap (tukar nilai kedua posisi tersebut)
    kromosom[posisi1], kromosom[posisi2] = kromosom[posisi2], kromosom[posisi1]
    return kromosom

# Inversion Mutation
def inversion_mutation(kromosom):
    # Memilih segmen secara acak, lalu membalik urutan gen dalam segmen tersebut.
    posisi1 = random.randint(0, len(kromosom) - 2)
    posisi2 = random.randint(posisi1 + 1, len(kromosom) - 1)

    # Konversi hasil reversed ke list
    kromosom[posisi1:posisi2] = list(reversed(kromosom[posisi1:posisi2]))
    return kromosom

# Uniform Mutation
def uniform_mutation(kromosom, mutation_rate=0.1):
    """
    Setiap gen dalam kromosom memiliki peluang sebesar mutation_rate untuk dibalik.
    - Jika gen = 1 -> menjadi 0 (barang tidak jadi dipilih)
    - Jika gen = 0 -> menjadi 1 (barang jadi dipilih)
    Default mutation_rate = 0.1 (10% peluang tiap gen mengalami mutasi)
    """

    # Pastikan kromosom adalah list
    kromosom = list(kromosom)  # Konversi ke list jika perlu

    for i in range(len(kromosom)):
        if random.random() < mutation_rate:
            kromosom[i] = 1 - kromosom[i]  # Membalik nilai gen (0->1 atau 1->0)
    return kromosom

# Definisikan anak1 sebelum digunakan
anak1 = [0, 1, 1, 0, 1]  # Contoh kromosom, sesuaikan dengan kebutuhan Anda

# Contoh penggunaan
mutasi_anak1 = swap_mutation(anak1.copy())       # Swap Mutation
mutasi_anak2 = inversion_mutation(anak1.copy())  # Inversion Mutation
mutasi_anak3 = uniform_mutation(anak1.copy())    # Uniform Mutation

# Menampilkan hasil setelah mutasi
print("\nAnak Setelah Mutasi:")
print(f"Anak 1 (Swap Mutation): {mutasi_anak1}")
print(f"Anak 2 (Inversion Mutation): {mutasi_anak2}")
print(f"Anak 3 (Uniform Mutation): {mutasi_anak3}")