# Define symptom and disease codes
kode_penyakit = ["K1", "K2", "K3", "K4"]
gejala_codes = [
    "J01", "J02", "J03", "J04", "J05", "J06", "J07", "J08", "J09", "J10", "J11", 
    "J12", "J13", "J14", "J15", "J16", "J17", "J18", "J19", "J20"
]

# Rules dictionary for disease and corresponding symptoms with their MB values
rules = {
    "K1": ["J01", "J03", "J08", "J09", "J10", "J11", "J12", "J14", "J15", "J16", "J17", "J18", "J19"],
    "K2": ["J04", "J05", "J06", "J16"],
    "K3": ["J01", "J07", "J19"],
    "K4": ["J03", "J08", "J13", "J18", "J20"]
}

# User input dictionary for symptoms and their certainty responses
user_input = {
    "J01": ["Apakah anda sering menderita sakit kepala?", "Mungkin", 0.4],
    "J02": ["Apakah anda kehilangan nafsu makan?", "Pasti", 1],
    "J03": ["Apakah tidur anda tidak lelap?", "Mungkin", 0.4],
    "J04": ["Apakah anda mudah menjadi takut?", "Hampir Pasti", 0.8],
    "J05": ["Apakah anda merasa cemas, tegang, dan khawatir?", "Mungkin", 0.4],
    "J06": ["Apakah tangan anda gemetar?", "Mungkin", 0.4],
    "J07": ["Apakah anda mengalami gangguan pencernaan?", "Pasti", 1],
    "J08": ["Apakah anda merasa sulit berpikir jernih?", "Kemungkinan Besar", 0.6],
    "J09": ["Apakah anda merasa tidak bahagia?", "Kemungkinan Besar", 0.6],
    "J10": ["Apakah anda sering menangis?", "Pasti", 1],
    "J11": ["Apakah anda sulit untuk menikmati aktivitas sehari-hari?", "Kemungkinan Besar", 0.6],
    "J12": ["Apakah anda mengalami kesulitan untuk mengambil keputusan?", "Mungkin", 0.4],
    "J13": ["Apakah pekerjaan sehari-hari terganggu?", "Kemungkinan Besar", 0.6],
    "J14": ["Apakah anda merasa tidak mampu berperan dalam kehidupan ini?", "Pasti", 1],
    "J15": ["Apakah anda kehilangan minat terhadap banyak hal?", "Mungkin", 0.4],
    "J16": ["Apakah anda merasa tidak berharga?", "Kemungkinan Besar", 0.6],
    "J17": ["Apakah anda mempunyai pikiran untuk mengakhiri hidup anda?", "Hampir Pasti", 0.8],
    "J18": ["Apakah anda merasa lelah sepanjang waktu?", "Kemungkinan Besar", 0.6],
    "J19": ["Apakah anda merasa tidak enak perut?", "Pasti", 1],
    "J20": ["Apakah anda mudah lelah?", "Kemungkinan Besar", 0.6]
}

pakar_input = {
    "K1": [
        ("J02", "Apakah anda kehilangan nafsu makan?", 1.0),
        ("J03", "Apakah tidur anda tidak lelap?", 0.6),
        ("J08", "Apakah anda merasa sulit berpikir jernih?", 0.4),
        ("J09", "Apakah anda merasa tidak bahagia?", 1.0),
        ("J10", "Apakah anda sering menangis?", 1.0),
        ("J11", "Apakah anda sulit untuk menikmati aktivitas sehari-hari?", 0.4),
        ("J12", "Apakah anda mengalami kesulitan untuk mengambil keputusan?", 0.0),
        ("J14", "Apakah anda merasa tidak mampu berperan dalam kehidupan ini?", 0.8),
        ("J15", "Apakah anda kehilangan minat terhadap banyak hal?", 0.0),
        ("J16", "Apakah anda merasa tidak berharga?", 1.0),
        ("J17", "Apakah anda mempunyai pikiran untuk mengakhiri hidup anda?", 0.0),
        ("J18", "Apakah anda merasa lelah sepanjang waktu?", 0.8),
        ("J19", "Apakah anda merasa tidak enak perut?", 0.0)
    ],
    "K2": [
        ("J04", "Apakah anda mudah menjadi takut?", 0.6),
        ("J05", "Apakah anda merasa cemas, tegang, dan khawatir?", 0.4),
        ("J06", "Apakah tangan anda gemetar?", 0.4),
        ("J16", "Apakah anda merasa tidak berharga?", 1.0)
    ],
    "K3": [
        ("J01", "Apakah anda sering menderita sakit kepala?", 0.8),
        ("J07", "Apakah anda mengalami gangguan pencernaan?", 0.6),
        ("J19", "Apakah anda merasa tidak enak perut?", 0.6)
    ],
    "K4": [
        ("J03", "Apakah tidur anda tidak lelap?", 0.4),
        ("J08", "Apakah anda merasa sulit berpikir jernih?", 0.0),
        ("J13", "Apakah pekerjaan sehari-hari terganggu?", 0.0),
        ("J18", "Apakah anda merasa lelah sepanjang waktu?", 0.8),
        ("J20", "Apakah anda mudah lelah?", 1.0)
    ]
}

hitung_cf = {
    "K1": [
        ("J02", "Apakah anda kehilangan nafsu makan?", 1.0, 1.0),
        ("J03", "Apakah tidur anda tidak lelap?", 0.4, 0.6),
        ("J08", "Apakah anda merasa sulit berpikir jernih?", 0.6, 0.4),
        ("J09", "Apakah anda merasa tidak bahagia?", 0.6, 1.0),
        ("J10", "Apakah anda sering menangis?", 1.0, 1.0),
        ("J11", "Apakah anda sulit untuk menikmati aktivitas sehari-hari?", 0.6, 0.4),
        ("J12", "Apakah anda mengalami kesulitan untuk mengambil keputusan?", 0.4, 0.0),
        ("J14", "Apakah anda merasa tidak mampu berperan dalam kehidupan ini?", 1.0, 0.8),
        ("J15", "Apakah anda kehilangan minat terhadap banyak hal?", 0.4, 0.0),
        ("J16", "Apakah anda merasa tidak berharga?", 0.6, 1.0),
        ("J17", "Apakah anda mempunyai pikiran untuk mengakhiri hidup anda?", 0.8, 0.0),
        ("J18", "Apakah anda merasa lelah sepanjang waktu?", 0.6, 0.8),
        ("J19", "Apakah anda merasa tidak enak perut?", 1.0, 0.0)
    ],
    "K2": [
        ("J04", "Apakah anda mudah menjadi takut?", 0.8, 0.6),
        ("J05", "Apakah anda merasa cemas, tegang, dan khawatir?", 0.4, 0.4),
        ("J06", "Apakah tangan anda gemetar?", 0.4, 0.4),
        ("J16", "Apakah anda merasa tidak berharga?", 0.4, 1.0)
    ],
    "K3": [
        ("J01", "Apakah anda sering menderita sakit kepala?", 0.4, 0.8),
        ("J07", "Apakah anda mengalami gangguan pencernaan?", 1.0, 0.6),
        ("J19", "Apakah anda merasa tidak enak perut?", 1.0, 0.6)
    ],
    "K4": [
        ("J03", "Apakah tidur anda tidak lelap?", 0.4, 0.4),
        ("J08", "Apakah anda merasa sulit berpikir jernih?", 0.6, 0.0),
        ("J13", "Apakah pekerjaan sehari-hari terganggu?", 0.6, 0.0),
        ("J18", "Apakah anda merasa lelah sepanjang waktu?", 0.6, 0.8),
        ("J20", "Apakah anda mudah lelah?", 0.6, 1.0)
    ]
}

def calculate_combination_cf(penyakit):
    cf_combination = 1
    for gejala in user_input.keys():
        for data in hitung_cf[penyakit]:
            if gejala == data[0]:
                cf_combination *= data[2] * data[3]
                break
    return cf_combination

def calculate_aggregated_cf(penyakit):
    cf_combinations = []
    for gejala in user_input.keys():
        for data in hitung_cf[penyakit]:
            if gejala == data[0]:
                cf_combinations.append(data[2] * data[3])
                break

    cf_aggregated = cf_combinations[0]
    for cf in cf_combinations[1:]:
        cf_aggregated = cf_aggregated + cf - (cf_aggregated * cf)

    return cf_aggregated

def calculate_percentage(cf_combination, cf_aggregated):
    return cf_aggregated * 100

def calculate_cf(penyakit):
    cf_combination = calculate_combination_cf(penyakit)
    cf_aggregated = calculate_aggregated_cf(penyakit)
    percentage = calculate_percentage(cf_combination, cf_aggregated)
    
    return percentage

print("\nCertainty Factor Gabungan:")
print("Kode Penyakit   |       CF Gabungan")
print("-----------------------------------")
for penyakit in rules.keys():
    i = kode_penyakit.index(penyakit)
    cf_percentage = calculate_cf(penyakit)
    print(f"{penyakit}\t\t|\t{cf_percentage:.2f}%")