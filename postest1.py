print("Postest1 Nim ganjil, \n")
#Login sederhana
nama = input("masukkan nama: ")
nim  = int(input("masukkan nim: "))
print(nama, ",", nim, "\n")
print(f"perkenalkan nama saya {nama}.nim saya {nim}. saya dari kelas B sistem informasi angkatan 23,\n")

#fungsi menghitung nilai tukar mata uang rupiah ke mata uang USD, Yen, dan MYR
def rupiah_ke_usd(nilairupiah):
    return nilairupiah * 0.000065  # Nilai tukar 1 rupiah ke USD

def rupiah_ke_yen(nilairupiah):
    return nilairupiah * 0.0097  # Nilai tukar 1 rupiah ke JPY

def rupiah_ke_ringgit(nilairupiah):
    return nilairupiah * 0.00031  # Nilai tukar 1 rupiah ke MYR

nilairupiah = float(input("Masukkan nilai uang Rupiah: "))

#Konversi mata uang rupiah ke USD,Yen, dan MYR
print("Pilih mata uang untuk dikonversi:")
print("1. Dolar Amerika (USD)")
print("2. Yen (JPY)")
print("3. Ringgit Malaysia (MYR),\n")

#Memasukkan pilihan konversi Mata uang
pilihan = int(input("Masukkan pilihan (1/2/3): "))

#Percabangan untuk mengambil keputusan pilihan mata uang yang dikonversi

if pilihan == 1:
    jumlahkonversi = rupiah_ke_usd(nilairupiah)
    print(f"uang dollar saya sebesar: {jumlahkonversi}, USD")
    
elif pilihan == 2:
    jumlahkonversi = rupiah_ke_yen(nilairupiah)
    print(f"uang yen saya sebesar: {jumlahkonversi}, Yen")
elif pilihan == 3:
    jumlahkonversi = rupiah_ke_ringgit(nilairupiah)
    print(f"uang ringgit saya sebesar: {jumlahkonversi}, MYR")
else:
    print("Pilihan tidak valid. Silakan pilih antara 1, 2, atau 3.,\n")
