menu = input("Massukan daftar pesanan :")
hasil = menu.title()
print("Daftar pesanan :", hasil.split(","))
tambahan = input("Masukkan pesanan yang ingin ditambahkan :")
result = tambahan.upper()
if tambahan in menu:
    print(result, "sudah berada dalam daftar pesanan.")
else:
    print("Hasil penambahan pada daftar pesanan :", result.split(","))
    
    



