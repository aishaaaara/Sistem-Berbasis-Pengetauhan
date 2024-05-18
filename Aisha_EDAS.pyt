import numpy as np
#AISHA RAHMADIA AQILAH SIB 2D (2241760098)
# Data kriteria, alternatif, dan evaluasi
kriteria = [
    ('Luas Lahan', 0.133, 'benefit'),
    ('Jarak ke Pusat Kota', 0.053, 'cost'),
    ('Sistem Informasi Pendukung', 0.080, 'benefit'),
    ('Keunggulan Transportasi Umum dibanding Angkutan Pribadi', 0.067, 'benefit'),
    ('Promosi oleh Institusi Umum', 0.027, 'benefit'),
    ('Frekuensi Angkutan Umum di lokasi', 0.093, 'benefit'),
    ('Harga Tempat Parkir', 0.187, 'cost'),
    ('Trafik Angkutan Umum di Lokasi', 0.107, 'cost'),
    ('Lokasi Parkir Gratis di Pusat Kota', 0.040, 'cost'),
    ('Total Biaya Parkir dan Angkutan Umum', 0.160, 'cost'),
]

alternatif = [
    'Lot 51', 'Petak 61', 'Petak 77', 'Area 51', 'Lot 61', 'Petak 57', 'Komplek 51'
]

evaluasi = [
    [4, 3, 7, 6, 8, 6, 4, 4, 5, 4],  # Lot 51
    [2, 4, 4, 8, 5, 6, 5, 2, 3, 3],  # Petak 61
    [4, 3, 7, 9, 7, 4, 5, 3, 4, 3],  # Petak 77
    [4, 5, 8, 8, 8, 3, 5, 4, 3, 3],  # Area 51
    [4, 4, 4, 9, 6, 3, 3, 3, 5, 3],  # Lot 61
    [2, 3, 6, 8, 7, 3, 3, 4, 5, 3],  # Petak 57
    [4, 5, 4, 9, 5, 6, 4, 3, 3, 4]   # Komplek 51
]

# Konversi ke numpy array
evaluasi = np.array(evaluasi)

# Menghitung nilai solusi rata-rata (AV)
AV = evaluasi.mean(axis=0)

# Inisialisasi array untuk PDA dan NDA
PDA = np.zeros_like(evaluasi, dtype=float)
NDA = np.zeros_like(evaluasi, dtype=float)

# Menghitung PDA dan NDA berdasarkan tipe kriteria (benefit/cost)
for j in range(len(kriteria)):
    if kriteria[j][2] == 'benefit':
        PDA[:, j] = np.maximum(0, (evaluasi[:, j] - AV[j]) / AV[j])
        NDA[:, j] = np.maximum(0, (AV[j] - evaluasi[:, j]) / AV[j])
    else:
        PDA[:, j] = np.maximum(0, (AV[j] - evaluasi[:, j]) / AV[j])
        NDA[:, j] = np.maximum(0, (evaluasi[:, j] - AV[j]) / AV[j])

# Menghitung jumlah terbobot PDA dan NDA
bobot = np.array([k[1] for k in kriteria])
SP = PDA @ bobot
SN = NDA @ bobot

# Normalisasi SP dan SN
NSP = SP / SP.max()
NSN = 1 - (SN / SN.max())

# Menghitung nilai skor penilaian (AS)
AS = 0.5 * (NSP + NSN)

# Mengurutkan alternatif berdasarkan nilai AS
ranking = np.argsort(-AS) + 1

# Buat array indeks alternatif
indeks_alternatif = np.arange(len(alternatif))

# Urutkan nilai AS dari yang terbesar ke terkecil
urutan_terbesar_ke_terkecil = np.argsort(AS)[::-1]

# Menampilkan PDA dan NDA 
print("Nilai PDA/NDA : ")
print("+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------+")
print("|                                 PDA                                         |                                 NDA                                           |")
print("+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------+")
for i in range(len(kriteria)):
    print("|", end=" ")
    for val in PDA[:, i]:
        print("{:<10.6f}".format(val), end=" ")
    print("|", end=" ")
    for val in NDA[:, i]:
        print("{:<10.6f}".format(val), end=" ")
    print("|")
print("+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------+")

# Menampilkan hasil SP, SN, NSP, NSN, dan AS dalam satu baris
# Menampilkan hasil SP, SN, NSP, NSN, dan AS dalam satu baris dengan tabel yang rapi
print("Menghitung jumlah terbobot PDA / NDA (SP / SN), nilai normalisasi SP / SN (NSP / NSN), dan nilai skor penilaian (AS) dalam satu baris:")
print("+----------------------+----------------------+----------------------+----------------------+----------------------+")
print("|         SP           |          SN          |          NSP         |          NSN         |          AS          |")
print("+----------------------+----------------------+----------------------+----------------------+----------------------+")
max_len = max(len(max(map(str, SP), key=len)), len(max(map(str, SN), key=len)), len(max(map(str, NSP), key=len)), len(max(map(str, NSN), key=len)), len(max(map(str, AS), key=len)))
for sp_val, sn_val, nsp_val, nsn_val, as_val in zip(SP, SN, NSP, NSN, AS):
    print(f"| {sp_val:<{max_len}} | {sn_val:<{max_len}} | {nsp_val:<{max_len}} | {nsn_val:<{max_len}} | {as_val:<{max_len}} |")
print("+----------------------+----------------------+----------------------+----------------------+----------------------+")



# Menampilkan hasil nilai solusi rata-rata (AV) dalam bentuk tabel
print("Nilai Rata-rata : ")
print("+--------------------------------------------------------------+---------+")
print("|                      Kriteria                                |   AV    |")
print("+------------------------------------------------------------- +---------+")
for i, nilai in enumerate(AV):
    print(f"| {kriteria[i][0]:<60} | {nilai:<7.4f} |")
print("+--------------------------------------------------------------+---------+")


# Tampilkan urutan alternatif berdasarkan indeks yang telah diurutkan
print("Hasil Perangkingan : ")
print("+----------+-----------------------------+-----------------------------+")
print("| Rangking |          Alternatif         |           NILAI AS          |")
print("+----------+-----------------------------+-----------------------------+")
for i, idx in enumerate(urutan_terbesar_ke_terkecil):
    print(f"|   {i+1:<6} | {alternatif[indeks_alternatif[idx]]:<27} | {AS[idx]:<27} |")
print("+----------+-----------------------------+-----------------------------+")


