import requests
from ytmusicapi import YTMusic
import sys
import random 

yt = YTMusic()


def sehir_bul(sehir):

  url = "https://geocoding-api.open-meteo.com/v1/search"

  parametreler= {
    "name" : sehir ,
    "count" : 1 ,   
    "language" : "tr" ,
    "format" : "json"
    }

  try:
     cevap = requests.get(url, params=parametreler,timeout=10)
     cevap.raise_for_status() #HTTP hatalarını kontrol eder.
     sehir_verileri = cevap.json()
  except Exception as e:
     print("Bir hata oluştu:" , e)
     return None
  
  return sehir_verileri

def hava_durumu_getir(enlem,boylam):
  hava_url = "https://api.open-meteo.com/v1/forecast"
  
  hava_parametreleri = {
       "latitude": enlem,
       "longitude": boylam,
       "current": "temperature_2m,weather_code"
        }
  try:
    hava_cevap = requests.get(hava_url, params=hava_parametreleri,timeout=10)
    hava_cevap.raise_for_status()
    hava_verileri = hava_cevap.json()
  except Exception as e:
    print("Bir hata oluştu:",e)
    return None
  
  return hava_verileri 

def hava_durumu(kod):
    if kod == 0:
      return "Güneşli"
    elif kod in [1,2,3]:
      return"Bulutlu"
    elif kod in [45,48 ] :
      return "Sisli"
    elif kod in [51,53,55]:
      return "Çisenti"
    elif kod in [61,63,65] :
      return "Yağmurlu"
    elif kod in [71,73,75] :
      return "Karlı"
    elif kod in [80,81,82]:
      return "Sağanak"
    else:
      return "Diğer hava koşulları"

def muzik_turu(durum):
  if durum == "Güneşli" :
    return "Pop ve Dance"
  elif durum == "Bulutlu" :
    return "Indie ve Alternatif"
  elif durum == "Sisli"  or durum == "Çisenti" :
    return "Lo-Fi ve Ambient"
  elif durum == "Yağmurlu" :
    return "Akustik ve Slow"
  elif durum == "Karlı" :
    return "Jazz ve Klasik"
  elif durum == "Sağanak":
    return "Rock ve Alternative"
  else:
    return "Genel müzik önerileri"

def sarki_ara(tur):
  try:
    sonuclar = yt.search(tur , filter="songs")
  except Exception as e:
    print("Bir hata oluştu:", e)
    return None
  if not sonuclar:
    print("Bu müzik türü için şarkı bulunamadı.")
    return

  rastgele_sarkilar= random.sample(sonuclar,min(5,len(sonuclar)))

  for sarki in rastgele_sarkilar:

    baslik = sarki.get("title")
    if baslik:
      print("Şarkı:", baslik)
    else:
      print("Şarkı adı bulunamadı.")

    sanatcilar = sarki.get("artists", [])
    if sanatcilar and sanatcilar[0].get("name"):
       print("Sanatçı:", sanatcilar[0]["name"])
    else:
       print("Sanatçı bilgisi bulunamadı.")


    video_id = sarki.get("videoId")

    if isinstance(video_id, str) and video_id:
      print("VideoID:", video_id)
      print("Bağlantı:","https://music.youtube.com/watch?v=" + video_id )
    else:
      print("Video ID bulunamadı.")

   
    print("-------------------")

def muzik_oner(kod):
  durum=hava_durumu(kod)
  tur = muzik_turu(durum)

  print(f"Hava durumu : {durum}")
  print(f"Önerilen müzik türü : {tur}")


  sarki_ara(tur)


while True:

  sehir = input("Şehir adı: ").strip()

  if sehir == "":
    print("Şehir adı boş bırakılamaz.")
  else:
    break

sehir_verileri=sehir_bul(sehir)

if sehir_verileri is None: 
  sys.exit()

if "results" in sehir_verileri and sehir_verileri["results"]:
   
   ulke = sehir_verileri["results"][0]["country"]
   enlem = sehir_verileri["results"][0]["latitude"]
   boylam = sehir_verileri["results"][0]["longitude"]
   sehir_adi = sehir_verileri["results"][0]["name"]

   print("Şehir bulundu!")
   print("Ülke:", ulke)
   print("Şehir:", sehir_adi)
   print("Enlem:", enlem)
   print("Boylam:", boylam)

   hava_verileri=hava_durumu_getir(enlem,boylam)

   if hava_verileri is None:
      sys.exit()
   if "current" not in hava_verileri:
      print("Hava durumu bilgileri alınamadı.")
      sys.exit()

   if "temperature_2m" not in hava_verileri["current"] or "weather_code" not in hava_verileri["current"]:
      print("Sıcaklık veya hava durumu kodu alınamadı.")
      sys.exit()

   sicaklik = hava_verileri["current"]["temperature_2m"]
   kod = hava_verileri["current"]["weather_code"]


   print("Sıcaklık:", sicaklik, "°C")
   print("Hava kodu:", kod)

   muzik_oner(kod)

else:
    print("Şehir bulunamadı!")
    sys.exit() 

