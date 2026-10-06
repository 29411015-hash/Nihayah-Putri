from produk1 import Produk1

jumlah_produk = int(input('Masukkan Jumlah Produk:'))
total_semua = 0

for i in range(jumlah_produk):
    print(f'Produk ke-{i+1}')
    nama_produk = input('Masukkan Nama Barang:')
    harga_produk = float(input('Masukkan Harga Barang:'))
    jumlah_beli = int(input('Masukkan Jumlah Beli:'))

    produk = Produk1(nama_produk, harga_produk)
    produk.tampilkan_info()

    Total = produk.hitung_total(jumlah_beli)
    print(f'Total Pembelian {produk.nama} : {Total}')

    total_semua += Total

diskon = Produk1.hitung_diskon(total_semua)
total_bayar = total_semua - diskon

print('\n=== HASIL PEMBELIAN ===')
print(f'Total Pembelian : {total_semua}')
print(f'Diskon 5%       : {diskon}')
print(f'Total Bayar     : {total_bayar}')