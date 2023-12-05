#Json dosyasından veri çekme

import json

with open('info.json', 'r+', encoding="utf-8") as dosya:
    veri = json.load(dosya)

aranan_id = 26
yeni_name = "Leo4Code"

for ticket in veri.get("info", []):
    if ticket.get("id") == aranan_id:
        print("İstenilen veri bulundu!")
        print(ticket)
        break 
else:
    print("istenilen id'ye sahip veri bulunamadı")
 
#Leo4Bey - Leo4Code tarafından yapılmıştır
# https://leo4bey.net