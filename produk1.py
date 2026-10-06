class Produk1:
    def __init__(self, nama_produk, harga_produk):
        self.nama = nama_produk
        self.harga = harga_produk

    def tampilkan_info(self):
        print(f'Nama Produk : {self.nama}\nHarga Produk : Rp{self.harga}')

    def hitung_total(self, jumlah):
        return self.harga * jumlah

    def hitung_diskon(total_semua):
        if total_semua > 5000:
            return total_semua * 0.05
        return 0