import random

# CROSSOVER (Rekombinasi)
# Menggabungkan dua kromosom parent untuk menghasilkan dua kromosom anak (offspring).
# Tujuannya untuk menghasilkan populasi keturunan yang lebih baik dari generasi sebelumnya.
#
# Tiga metode crossover yang diimplementasikan:
# 1. One-Point Crossover  -> potong di 1 titik, tukar bagian belakang
# 2. Two-Point Crossover  -> potong di 2 titik, tukar segmen tengah
# 3. Uniform Crossover    -> setiap gen dipilih dari parent mana berdasarkan mask acak
# ============================================================

# One-Point Crossover
def one_point_crossover(parent1, parent2):
    # Memotong kromosom di satu titik potong acak, lalu menukar bagian setelah titik tersebut.
    titik_potong = random.randint(1, len(parent1) - 1)
    anak1 = parent1[:titik_potong] + parent2[titik_potong:]
    anak2 = parent2[:titik_potong] + parent1[titik_potong:]
    return anak1, anak2

# Two-Point Crossover
def two_point_crossover(parent1, parent2):
    # Memotong kromosom di DUA titik potong acak, lalu menukar segmen di antara kedua titik.
    titik1 = random.randint(1, len(parent1) - 2)
    titik2 = random.randint(titik1 + 1, len(parent1) - 1)
    anak1 = parent1[:titik1] + parent2[titik1:titik2] + parent1[titik2:]
    anak2 = parent2[:titik1] + parent1[titik1:titik2] + parent2[titik2:]
    return anak1, anak2

# Uniform Crossover
def uniform_crossover(parent1, parent2):
    """
    Setiap gen pada anak ditentukan oleh mask acak (array 0 dan 1).
    Aturan mask:
      - Mask[i] = 0 -> Anak1 ambil dari Parent1, Anak2 ambil dari Parent2
      - Mask[i] = 1 -> Anak1 ambil dari Parent2, Anak2 ambil dari Parent1
    """
    # Membuat mask acak
    mask = [random.randint(0, 1) for _ in range(len(parent1))]
    anak1 = []
    anak2 = []
    for i in range(len(parent1)):
        if mask[i] == 0:
            # Jika mask bernilai 0, ambil gen dari parent1 untuk anak1, dan parent2 untuk anak2
            anak1.append(parent1[i])
            anak2.append(parent2[i])
        else:
            # Jika mask bernilai 1, ambil gen dari parent2 untuk anak1, dan parent1 untuk anak2
            anak1.append(parent2[i])
            anak2.append(parent1[i])
    return anak1, anak2

# Contoh penggunaan
parent1 = [1, 0, 1, 1, 0]  # Contoh parent1
parent2 = [0, 1, 0, 0, 1]  # Contoh parent2

anak1, anak2 = one_point_crossover(parent1, parent2)

print("\nAnak Hasil Crossover:")
print(f"Anak 1: {anak1}")
print(f"Anak 2: {anak2}")