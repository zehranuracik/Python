class okul:
    def __init__(self,ad,soyad,okul_no,vize,final):
        self.ad = ad
        self.soyad = soyad
        self.okul_no = okul_no
        self.vize = vize
        self.final = final
        self.ders_notu = self.vize * 0.4 + self.final * 0.6

    def bilgileri_goster(self):
        print(f"""Öğrenci Bilgileri
        Ad: {self.ad}
        Soyad: {self.soyad}
        Öğrenci no: {self.okul_no}
        Vize notu: {self.vize}
        Final notu: {self.final}
        Ders geçme notu: {self.ders_notu}""")

class birinci_sinif(okul):
    def ders_baslangic(self,ders_baslangici):
        print("1. Sınıfların ders baslangic tarihi:",ders_baslangici)

class son_sinif(okul):
    def mezuniyet(self,mezuniyet_tarihi):
        print("Son sınıfların mezuniyet tarihi:",mezuniyet_tarihi)


ogr1 = birinci_sinif("Emin","Erol",20370031021,50,78)
ogr1.bilgileri_goster()
print("")
ogr1.ders_baslangic("11.09.2021")
ogr2 = son_sinif("Zehra Nur","Açık",20370031001,85,42)
print("")
ogr2.bilgileri_goster()
print("")
ogr2.mezuniyet("28.06.2021")
