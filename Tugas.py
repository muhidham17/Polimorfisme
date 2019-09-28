class FakultasTeknik(object):
  def __init__(self, u, f, t):
    self.univ = u
    self.fak = f
    self.tahunajar = t
    
  def cetakData0(self):
    print("Universitas\t: ", self.univ)
    print("Fakultas\t: ", self.fak)
    print("Tahun Ajar\t: ", self.tahunajar)
    print(50 * "=")
    
class TeknikKomputer(FakultasTeknik):
  def __init__(self, u, f, t, ja):
    self.univ = u
    self.fak = f
    self.tahunajar = t
    self.jumlahangkatan = ja
  def cetakData1(self):
    print("Teknik Komputer")
    print("Universitas\t: ", self.univ)
    print("Fakultas\t: ", self.fak)
    print("Tahun Ajar\t: ", self.tahunajar)
    print("Jumlah Angkatan\t: ", self.jumlahangkatan)
    print(50 * "=")
    
class PTIK(FakultasTeknik):
  def __init__(self, u, f, j, t, ja):
    self.univ = u
    self.fak = f
    self.ju = j
    self.tahunajar = t
    self.jumlahangkatan = ja
  def cetakData2(self):
    print("Pendidikan Teknik Informatika dan Komputer")
    print("Universitas\t: ", self.univ)
    print("Fakultas\t: ", self.fak)
    print("Jurusan\t        : ", self.ju)
    print("Tahun Ajar\t: ", self.tahunajar)
    print("Jumlah Angkatan\t: ", self.jumlahangkatan)
    
class Mekatronika(FakultasTeknik):
  def __init__(self, u, f, t, ja):
    self.univ = u
    self.fak = f
    self.tahunajar = t
    self.jumlahangkatan = ja
  def cetakData3(self):
    print("Pendidikan Vokasional Mektronika")
    print("Universitas\t: ", self.univ)
    print("Fakultas\t: ", self.fak)
    print("Tahun Ajar\t: ", self.tahunajar)
    print("Jumlah Angkatan\t: ", self.jumlahangkatan)
    
def main():
  ft = FakultasTeknik ("Universitas Negeri Makassar", "Teknik", 2018)
  ft.cetakData0()
  
  tk = TeknikKomputer ("Universitas Negeri Makassar", "Teknik", 2018, 2)
  tk.cetakData1()
  
  ptik = PTIK ("Universitas Negeri Makassar", "Teknik", "Pendidikan Teknik Elektro", 2018, 10)
  ptik.cetakData2()
  
  me = Mekatronika ("Universitas Negeri Makassar", "Teknik", 2018, 2)
  me.cetakData3()
  
if __name__ == "__main__":
  main()
