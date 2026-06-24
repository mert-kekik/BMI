def get_valid_input(prompt, val_type, min_val=None, max_val=None):
    """Kullanıcıdan geçerli veri alana kadar soran yardımcı fonksiyon."""
    while True:
        try:
            value = val_type(input(prompt))
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                print(f"Lütfen {min_val} ile {max_val} arasında bir değer gir.")
                continue
            return value
        except ValueError:
            print("Geçersiz giriş! Lütfen doğru formatta tekrar dene.")

def vki_ve_ideal_kilo_motoru():
    print("--- Vücut Kitle İndeksi (VKİ) ve İdeal Kilo Analizcisi ---")
    
    boy_cm = get_valid_input("Boyunuzu santimetre cinsinden girin (Örn: 175): ", float, 50.0, 250.0)
    kilo = get_valid_input("Kilonuzu kilogram cinsinden girin (Örn: 70.5): ", float, 20.0, 300.0)
    
    boy_m = boy_cm / 100.0
    vki = kilo / (boy_m ** 2)
    
    print(f"\n--- Analiz Sonuçları ---")
    print(f"Vücut Kitle İndeksiniz (VKİ): {vki:.1f}")
    
    if vki < 18.5:
        durum = "Zayıf"
    elif 18.5 <= vki < 25.0:
        durum = "Normal Kilolu (Sağlıklı)"
    elif 25.0 <= vki < 30.0:
        durum = "Fazla Kilolu"
    else:
        durum = "Obez"
        
    print(f"Genel Durumunuz: {durum}")
    
    min_ideal = 18.5 * (boy_m ** 2)
    max_ideal = 24.9 * (boy_m ** 2)
    tam_ideal_nokta = 21.7 * (boy_m ** 2)
    
    print("-" * 50)
    print(f"Boyunuza ({boy_cm} cm) göre sağlıklı kilo aralığınız: {min_ideal:.1f} kg - {max_ideal:.1f} kg")
    print(f"Tam ortalama ideal kilonuz: {tam_ideal_nokta:.1f} kg")
    
    if kilo < min_ideal:
        fark = min_ideal - kilo
        print(f"[!] Sağlıklı aralığa ulaşmak için en az {fark:.1f} kg almalısınız.")
    elif kilo > max_ideal:
        fark = kilo - max_ideal
        print(f"[!] Sağlıklı aralığa ulaşmak için en az {fark:.1f} kg vermelisiniz.")
    else:
        print("[!] Harika! Tam olarak sağlıklı kilo aralığındasınız, bunu korumaya çalışın.")

if __name__ == "__main__":
    vki_ve_ideal_kilo_motoru()
