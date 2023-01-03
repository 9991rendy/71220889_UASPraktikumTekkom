print("==== Selamat datang di XXV ====")
Tanggal = int(input("Masukkan tanggal hari ini: "))

print("== Berikut genre film yang tersedia ==")
print("1. Horror")
print("2. Action")

pilihgenrefilm = int(input("Silahkan pilih mau nonton film bergenre apa : "))

if pilihgenrefilm == 1:
    print("== Berikut pilihan film horror yang sedang tayang ==")
    print("1. The Devil's Light")
    print("2. Pengabdi setan")
    banyaktiket = int(input("Mau memesan tiket sebanyak : "))
    harga = 25.000*banyaktiket
    print("Total yang harus dibayar adalah Rp. ", harga)

elif pilihgenrefilm == 2:
    print("== Berikut pilihan film horror yang sedang tayang ==")
    print("1. Black Panther: Wakanda Forever")
    print("2. Avatar: The Way of Water")
    pilihfilm = int(input("Silahkan pilih mau nonton film apa : "))

    banyaktiket = int(input("Mau memesan tiket sebanyak : "))
    harga = 25.000*banyaktiket
    print("Total yang harus dibayar adalah Rp. ", harga)

else:
    print("Pilihan yang anda pilih tidak tersedia di bioskop ini")