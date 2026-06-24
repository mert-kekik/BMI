# Vücut Kitle İndeksi (VKİ) ve İdeal Kilo Analizcisi

Bu program, kullanıcının boy ve kilo bilgilerini alarak Vücut Kitle İndeksini (VKİ) hesaplar, ağırlık durumunu analiz eder ve boyuna göre olacağı sağlıklı ideal kilo aralığını dinamik olarak hesaplar.

[🚀 Google Colab'da Doğrudan Çalıştır](https://colab.research.google.com/github/mert-kekik/BMI/blob/main/vki_analyzer.ipynb)

## Kullanım
Programı başlattıktan sonra sırasıyla şunlar sorulur:
- Boyunuz (Santimetre cinsinden, Örn: 175)
- Kilonuz (Kilogram cinsinden, Örn: 70.5)

Program girdiğiniz değerleri analiz eder ve size özel şu raporu sunar:
- Mevcut VKİ değeriniz ve durumunuz (Zayıf, Normal, Fazla Kilolu, Obez)
- Boyunuza göre sağlıklı alt ve üst kilo sınırları
- İdeal kilonuza ulaşmak için almanız veya vermeniz gereken net kilo miktarı

## Dosyalar
- `vki_analyzer.py`: Doğrudan terminal veya IDE üzerinden çalıştırmak için Python betiği.
- `vki_analyzer.ipynb`: Jupyter Notebook ve Google Colab uyumlu format.
