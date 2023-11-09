class Kumanda():
    def __init__(self,tvDurum = "Kapalı", tvSes = 0, kanalListesi = [], kanal = ""):
        self.tvDurum = tvDurum
        self.tvSes = tvSes
        self.kanalListesi = kanalListesi
        self.kanal = kanal
    
    def tvAc(self):
        if (self.tvDurum == "Açık"):
            print("Televizyon zaten açık.")
        elif (self.tvDurum == "Kapalı"):
            print("Televizyon açıldı.")
            self.tvDurum = "Açık"
    
    def tvKapat(self):
        if (self.tvDurum == "Kapalı"):
            print("Televizyon zaten kapalı.")
        elif (self.tvDurum == "Açık"):
            print("Televiyon kapandı.")
            self.tvDurum = "Kapalı"
    
    def sesAyarla(self):
        while (True):
            sesCevap = input("Sesi arttirmak icin +, azaltmak icin -, cikis icin q\n")
            if (sesCevap == "q"):
                print("Ses güncellendi: {}".format(self.tvSes))
                break
            elif (sesCevap == "+"):
                if (self.tvSes != 64):
                    print("Ses arttırıldı.")
                    self.tvSes += 1
            elif (sesCevap == "-"):
                if (self.tvSes != 0):
                    print("Ses azaltıldı.")
                    self.tvSes -= 1
      
    def kanalEkle(self):
        while (True):
            eklenecekKanal = input("Eklemek istediginiz kanal ismini giriniz, çıkış için q: ")
            if (eklenecekKanal == "q"):
                print("Kanal ekleme işlemi iptal edildi.")
                break
            else:
                print("{} isimli kanal eklendi.".format(eklenecekKanal))
                self.kanalListesi.append(eklenecekKanal)
    
    def kanalDegistir(self):
        print("Mevcut kanallar: ")
        for kanal in self.kanalListesi:
            print(kanal)
        kanal = int(input("Açmak istediğiniz kanalın numarasını giriniz: 1 - {}: ".format(len(self.kanalListesi))))
        self.kanal = self.kanalListesi[kanal-1]
        print("{} kanalı açıldı.".format(self.kanal))

kumanda = Kumanda()

print("""
KUMANDA UYGULAMASI
    
1 - Televizyonu aç
2 - Televizyonu kapat
3 - Ses seviyesini ayarla
4 - Kanal ekle
5 - Kanal değiştir
      
q - Çıkış
      """)

while (True):
    islem = input("Yapacağınız işlemi seçin: ")
    if (islem == "1"):
        kumanda.tvAc()
    elif (islem == "2"):
        kumanda.tvKapat()
    elif (islem == "3"):
        kumanda.sesAyarla()
    elif (islem == "4"):
        kumanda.kanalEkle()
    elif (islem == "5"):
        kumanda.kanalDegistir()
    elif (islem == "q"):
        print("Çıkış yapıldı.")
        break
