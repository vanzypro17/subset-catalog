# sub.set kataloğu

sub.set uygulamasının servis kataloğu: fiyatlar, planlar, iptal rehberleri. Uygulama bu dosyayı günde bir kez çeker.

## Fiyat güncellemek

1. `catalog.json` içinde servisi bul, `plans` altındaki `price` değerini düzelt.
2. `asOf` alanını fiyatın geçerli olduğu aya çek: `"2026-09"`.
3. Commit at. Doğrulama otomatik çalışır; dosya bozuksa yayına girmez.

## Alanlar

| Alan | Anlam |
|---|---|
| `id` | değişmez kimlik |
| `name`, `category`, `color` | görünen ad, kategori, marka rengi (`#RRGGBB`) |
| `plans[]` | `name`, `price`, `currency` (TRY/USD/EUR/GBP), `period` (weekly/monthly/yearly) |
| `customPrice` | true ise fiyatı kullanıcı girer (operatör, spor salonu) |
| `cancelUrl`, `cancelSteps[]` | iptal linki ve adımları |
| `keywords[]` | aramada eşleşen ek kelimeler |
| `logo` | `assets/logos/<logo>.svg` (uygulamada gömülü; yoksa monogram) |

Kategoriler: Video, Müzik, Oyun, Yazılım & AI, Bulut, Telekom, Spor & Sağlık, Alışveriş & Yemek, Eğitim, Diğer.
