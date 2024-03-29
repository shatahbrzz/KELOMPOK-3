class TokoPakaian:
  def __init__(self):
    self.bayar = 0
    self.kembalian = 0
    self.total bayar = 0
  def cost(self, produk, jumlah):
    pakaian = {
      'kaos' : 200000,
      'celana': 350000,
      'jaket': 400000,
      'rok': 350000,
      'kemeja': 250000,
      'hoodie': 350000,
      'blazer': 550000,
      'gamis': 600000,
      'dress': 450000
    }
    harga = pakaian.get(produk.lower(), 0)
    return harga * jumlah
  def tampilkanproduk(self):
    print("Daftar Produk:")
    pakaian = {
      'kaos' : 200000,
      'celana': 350000,
      'jaket': 400000,
      'rok': 350000,
      'kemeja': 250000,
      'hoodie': 350000,
      'blazer': 550000,
      'gamis': 600000,
      'dress': 450000
    }
    for produk, harga in pakaian.items():
      print(f"{produk.capitalize()}: Rp {harga}")
      
