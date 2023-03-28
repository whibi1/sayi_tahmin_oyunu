import random
import time
print(f"Sayı Tahmin Oyunu \n 1 ile 100 arasında bir sayı tahmin edin.")

rastgele_sayi=random.randint(1,100)
tahmin_hakki=10
while True:
    tahmin=int(input("Tahmininiz:\n"))
    if (tahmin<rastgele_sayi):
        print(f"bilgiler sorgulanıyor...")
        time.sleep(1)
        print(f"Daha yüksek bir sayı söyleyin...")
        tahmin_hakki-=1
    elif (tahmin>rastgele_sayi):
        print(f"bilgiler sorgulanıyor...")
        time.sleep(1)
        print(f"Daha düşük bir sayı söyleyin...")
        tahmin_hakki-=1

    else:
        print(f"bilgiler sorgulanıyor...")
        time.sleep(1)
        print(f"Tebrikler doğru cevap, sayımız: {rastgele_sayi}")
        tahmin_hakki-=1
    if (tahmin_hakki==0):
        print(f"Tahmin hakkınız bitti...\n sayımız:{rastgele_sayi}")
        break
