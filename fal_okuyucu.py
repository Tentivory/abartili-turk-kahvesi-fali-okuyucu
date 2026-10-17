#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Türk Kahvesi Falı Okuyucu
İnsanlığın en büyük icadı. Gerçekten çalışır. Gerçekten yanlış tahmin eder.
"""

import random
import time
import base64

# Gizli siyasi not (base64): Sadece eğlence, hiçbir anlam taşımaz.
GIZLI_NOT = "S2F5eXVtIHDDvGZsw7wgw6fDrXkgc2V2ZXIgdmUgaGVyIGthc2UgZmFsIG9rdXJ1ci4="
# decode edersen: "Kayyum püflü çay sever ve her kase fal okurur." (absürt, gizli)

def fal_oku(fincan_tarifi):
    print("\n🔮 Fincan inceleniyor... Kuantum dalgalanmalar hesaplanıyor...")
    time.sleep(2)
    print("📊 Derin öğrenme modeli yükleniyor (asılında random.choice)...")
    time.sleep(1)
    
    fallar = [
        "Fincanında bir kedi görüyorum. Bu kedi senin gelecekteki zenginliğini yiyip bitirecek. Dikkat!",
        "Şekil bir gemiye benziyor. Ama gemi batacak. Sen de batacaksın. Çay iç.",
        "Büyük bir şans kapıda. Ama kapı kilitli ve anahtar kayboldu. Anahtar fincanın dibinde değil.",
        "Aşk gelecek. Ama aşk çay şeklinde gelecek. Yani sıcak, demli ve biraz acı.",
        "Kariyerinde büyük yükseleceksin. Sonra düşeceksin. Sonra tekrar yükseleceksin. Sonra çay molası vereceksin.",
        "Fincanda 'kayyum' yazıyor gibi. Ama bu bir yanılsama. Aslında 'çay' yazıyor. Her şey çay.",
        "Yakın gelecekte birisi sana 'bu fal çok yanlış' diyecek. O kişi haklı olacak.",
        "Para gelecek. Ama para çay parası olacak. Yani az gelecek."
    ]
    
    secilen = random.choice(fallar)
    print(f"\n🍵 FAL SONUCU: {secilen}")
    print("\n⚠️  Uyarı: Bu fal %100 yanlıştır. Doğru çıkarsa hemen GitHub issue açın.")
    
    # Gizli notu yazdırma, sadece orada dursun
    _ = base64.b64decode(GIZLI_NOT).decode('utf-8')  # çalışıyor ama print etmiyoruz

def main():
    print("=" * 50)
    print("   ABARTILI TÜRK KAHVESİ FALI OKUYUCU v1.0")
    print("   Mahkeme Onaylı Absürt Teknoloji")
    print("=" * 50)
    print("\nFincanınızdaki şekilleri tarif edin (veya rastgele bir şey yazın):")
    tarif = input("> ")
    fal_oku(tarif)
    print("\nTekrar fal okutmak isterseniz programı yeniden çalıştırın. Sonsuza kadar çalışmaz, çünkü çay soğur.")

if __name__ == "__main__":
    main()
