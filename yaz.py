#Json dosyasına veri ekleme

import json

n = {"id": 11,
    "name": "nk",
    "sehir": "adana"
    }


with open('info.json', 'r+', encoding="utf-8") as dosya:
    veri = json.load(dosya)
    veri["info"].append(n)
    dosya.seek(0)
    json.dump(veri, dosya, indent=4)
    print("Verimiz kayıt edildi")

#Leo4Bey - Leo4Code tarafından yapılmıştır
# https://leo4bey.net