import json, sys
cats = {"Video","Müzik","Oyun","Yazılım & AI","Bulut","Telekom","Spor & Sağlık","Alışveriş & Yemek","Eğitim","Diğer"}
d = json.load(open("catalog.json", encoding="utf-8"))
ids = set()
for s in d:
    assert s["id"] not in ids, f"tekrar eden id: {s['id']}"; ids.add(s["id"])
    assert s["category"] in cats, f"{s['id']}: bilinmeyen kategori {s['category']}"
    assert s["color"].startswith("#") and len(s["color"]) == 7, f"{s['id']}: renk"
    for p in s.get("plans", []):
        assert p["price"] >= 0 and p["currency"] in ("TRY","USD","EUR","GBP") and p["period"] in ("weekly","monthly","yearly"), f"{s['id']}: plan {p}"
    assert s.get("plans") or s.get("customPrice"), f"{s['id']}: plan yok ve customPrice değil"
print(f"ok: {len(d)} servis")
