#Json dosyasınndaki veriyi güncelleme

import json

n = {"id": 1,
    "name": "nk",
    "sehir": "adana"
    }


with open('info.json', 'r+', encoding="utf-8") as dosya:
    veri = json.load(dosya)

aranan_id = 26
yeni_name = "Leo4Code"

for ticket in veri.get("info", []):
    if ticket.get("id") == aranan_id:
        print("İstenilen veri bulundu!")
        ticket["name"] = yeni_name
        with open('info.json', 'w', encoding="utf-8") as dosya:
            json.dump(veri, dosya, ensure_ascii=False, indent=2)
            print(f"Datadaki {aranan_id} id'sine sahip verinin (name) değişkeni {yeni_name} olarak güncellendi")
        break 
else:
    print("istenilen id'ye sahip veri bulunamadı")
        
#Leo4Bey - Leo4Code tarafından yapılmıştır
# https://leo4bey.net