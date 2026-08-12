def bolme_islemi(bolunen, bolen):
    try:
        sonuc = bolunen / bolen
        print(f"İşlem başarılı, sonuç: {sonuc}")
        return sonuc
        
    except ZeroDivisionError:
        print("HATA: Bir sayı sıfıra bölünemez!")
        return None
        
    finally:
        # try'da return ile fonksiyondan çıkılsa bile, 
        # except'te hata yakalanıp return ile çıkılsa bile,
        # sistem fonksiyondan tamamen çıkmadan BİR SANİYE ÖNCE burayı kesin çalıştırır.
        print("--- İşlem denemesi bitti ---\n")

# Hata olmayan durum:
bolme_islemi(10, 2)
# Hata olan durum:
bolme_islemi(10, 0)