
print("Lütfen hesap oluşturun.\n")

sys_isim = input("Adınız: ")
sys_soyisim = input("Soyadınız: ")
sys_parola = input("Banka sifreniz: ")

bakiye = 1000

print("Hesap oluşturma başarılı.\n")
print("Lütfen giriş yapın.\n")

denemeHakki = 3

while True:
    parola = input("Merhaba {}, lütfen parolanı gir: ".format(sys_isim))
    
    if (parola == sys_parola):
        
        print("""
Hoşgeldin, {} {}.
*************************************
ABC ATM

İşlemler:

1- Bakiye Sorgulama
2- Para Yatırma
3- Para Çekme

Programdan çıkmak için 'q'ya basınız.
*************************************\n
      """.format(sys_isim, sys_soyisim))
        
        while True:
            islem = input("Yapacağınız işlemi seçin: ")
            if (islem == "q"):
                break
            elif (islem == "1"):
                print("Bakiyeniz: {}".format(bakiye))
            elif (islem == "2"):
                yatirilacakTutar = int(input("Yatiralacak tutar: "))
                if (yatirilacakTutar < 1):
                    print("Geçersiz tutar.")
                else:
                    print("Para yatırma başarılı.")
                    bakiye += yatirilacakTutar
            elif (islem == "3"):
                cekilecekTutar = int(input("Çekilecek tutar: "))
                if (cekilecekTutar > bakiye):
                    print("Bu işlem için bakiyeniz yetersiz.")
                elif (cekilecekTutar < 1):
                    print("Geçersiz tutar.")
                else:
                    print("Para çekme başarılı.")
                    bakiye -= cekilecekTutar
            if (islem == "q"):
                break
    else: 
        denemeHakki -= 1
        print("Yanlış parola. Kalan deneme hakkı: {}".format(denemeHakki))
    if (denemeHakki == 0):
        print("3 kere yanlış parola girildi. Sisteme giriş başarısız.")
        break
    if (islem == "q"):
        print("Çıkış yapıldı.")
        break
        


