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

  def diskon(self, produk, jumlah, harga):
    potongan = 0
    if produk.lower() == "celana" and jumlah >= 2:
      potongan = 0.1 * harga * jumlah
      if jumlah >= 4:
        potongan = 0.2 * harga * jumlah
    elif produk.lower() == "kemeja" and jumlah >= 3:
      potongan = 0.2 * harga * jumlah
      if jumlah >= 5:
        potongan = 0.3 * harga * jumlah
    elif produk.lower() == "jaket" and jumlah >= 2:
      potongan = 0.15 * harga * jumlah
      if jumlah >= 3:
        potongan = 0.25 * harga * jumlah
    elif produk.lower() == "hoodie" and jumlah >= 2:
      potongan = 0.1 * harga * jumlah
      if jumlah >= 4:
        potongan = 0.2 * harga * jumlah
    elif produk.lower() == "blazer" and jumlah >= 2
      potongan = 0.1 * harga * jumlah
      if jumlah >= 4:
        potongan = 0.15 * harga * jumlah
    elif produk.lower() == "gamis" and jumlah >= 2:
      potongan = 0.1 * harga * jumlah
      if jumlah >= 4:
        potongan = 0.15 * harga * jumlah
    elif produk.lower() == "dress" and jumlah >= 2:
      potongan = 0.1 * harga * jumlah
      if jumlah >= 4:
        potongan = 0.2 * harga * jumlah
    return potongan
