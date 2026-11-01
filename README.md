# WeatherTunes

WeatherTunes, kullanıcının seçtiği şehrin güncel hava durumunu analiz ederek hava koşullarına uygun müzik türleri öneren bir Python projesidir.

## Kullanılan Teknolojiler 

- Python
- Requests
- Open-Meteo API
- YTMusicAPI

## Özellikler

- Kullanıcıdan şehir adı alma
- Open-Meteo API ile şehir koordinatlarını bulma
- Güncel sıcaklık ve hava durumu kodunu alma
- Hava durumunu Türkçe açıklamaya dönüştürme
- Hava durumuna göre müzik türü önerme
- YouTube Music üzerinden şarkı arama
- Rastgele 5 şarkı önerme
- API hatalarını kontrol etme

## Kurulum ve Çalıştırma 

1. Projeyi bilgisayarınıza indirin.
2. Proje klasörünü açın.
3. Gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

4. Programı çalıştırın:

```bash
python main.py
```

## Örnek Kullanım 

```text
Şehir adı: İstanbul

Şehir bulundu!
Ülke: Türkiye
Şehir: İstanbul
Enlem: 41.01
Boylam: 28.97

Sıcaklık: 18.5 °C
Hava kodu: 2

Hava durumu: Bulutlu
Önerilen müzik türü: Indie ve Alternatif

Şarkı: Örnek Şarkı
Sanatçı: Örnek Sanatçı
Bağlantı: YouTube Music bağlantısı
```

