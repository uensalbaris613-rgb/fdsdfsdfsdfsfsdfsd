# 180 Günlük İngilizce Planı — Satır Satır, Kanıta Dayalı Değerlendirme

**Hedef:** Sıfırdan B2.2 → IELTS Academic 6.5 (180 gün)
**Değerlendirme tarihi:** 12 Ekim 2026

**İncelenen belgeler**

1. `Son ÜtücüIngilizce_Calisma_Plani_Derli_Toplu.docx` → bu raporda **"Ana Plan"**
2. `905601NİHAİ İNGİLİZCE MASTER PLAN.docx` → bu raporda **"Son Faz"**

**Yöntem.** Plandaki her iddia İngilizce kaynaklarla (Cambridge, IELTS, Avrupa Konseyi, hakemli dergi makaleleri, araçların kendi sayfaları) karşılaştırıldı. Anki iş yükü, Anki'nin kullandığı FSRS-6 algoritmasıyla 180 gün boyunca simüle edildi (betik: [`anki_fsrs_simulasyonu.py`](anki_fsrs_simulasyonu.py)). Çalışma ortamımın ağ kısıtı nedeniyle ielts.org, cambridge.org ve idp.com sayfalarını doğrudan açamadım; bu sitelerdeki bilgileri arama sonuçlarındaki alıntılardan doğruladım. Yalnızca ikincil kaynakla doğrulanabilen ya da tarihli olan bilgiler metinde ayrıca belirtildi.

**İşaretler:** ✅ doğru / güçlü · 🟡 kısmen doğru, abartılı ya da düzeltilmeli · ❌ yanlış, kanıtsız ya da bu haliyle uygulanamaz · ❓ doğrulanamadı

---

## İçindekiler

0. [Kısa hüküm](#0-kısa-hüküm)
1. [Hedef ve süre gerçekçi mi?](#1-hedef-ve-süre-gerçekçi-mi)
2. [Zaman bütçesi denetimi (Anki simülasyonu dahil)](#2-zaman-bütçesi-denetimi)
3. [Tutarsızlıklar](#3-tutarsızlıklar)
4. [Ana Plan — satır satır](#4-ana-plan--satır-satır)
5. [Son Faz — satır satır](#5-son-faz--satır-satır)
6. [Kaynak doğrulama tablosu](#6-kaynak-doğrulama-tablosu)
7. [Planda eksik olanlar](#7-planda-eksik-olanlar)
8. [Önerilen revizyon](#8-önerilen-revizyon-planı-bozmadan)
9. [Kaynakça](#9-kaynakça)
- [Ek A — Anki simülasyonunun varsayımları](#ek-a--anki-simülasyonunun-varsayımları)

---

## 0. Kısa hüküm

### Güçlü yanlar (korunmalı)

- **Çerçeve doğru seçilmiş.** Nation'ın Dört Bileşen modeli, aralıklı tekrar (Anki), geri çağırma pratiği (boş kâğıda dökme), yüksek değişkenlikli sesletim eğitimi (English Accent Coach, çok konuşmacılı dinleme), 4/3/2, kendi konuşmasını yazıya dökme ve okurken dinleme — hepsi araştırmayla desteklenen tekniklerdir.
- **Türkçeye özgü tuzaklar biliniyor:** ünsüz kümesine ünlü ekleme (*school → iskul*), tanımlıklar, söz dizimi.
- **Veriye dayalı karar kuralları** (120. gün denemesi, sınavı kaydırma kuralı, "iki denemede 6.5 görmeden sınava girme") planın en olgun kısmı.
- **Anki yük tahmini isabetli.** Planın "Gün ~141: 337 tekrar ≈ 55 dk" öngörüsü, FSRS simülasyonumun sonucuyla (≈357 cevap, ≈56 dk) aynı mertebede.

### Kritik sorunlar (önem sırasıyla)

1. **Zaman bütçesi yaklaşık iki kat dolu.** "Sabah 180 dk" bloğuna yazılan işler (Anki + kart üretimi + her gün bir Empower ünitesi + Murphy + Workbook + ELSA + ses-yazım) gerçekçi olarak 5–7 saat sürer. Gün taşınca ilk feda edilen, planın en değerli kısımları (okuma, dinleme, yazma, konuşma) olur.
2. **Denge, dayandığı modelle çelişiyor.** Plan "Nation'ın denge prensibine sadık yegâne mimari" olduğunu söylüyor; oysa dil odaklı öğrenme (LFL) 5 saatlik çekirdeğin %60'ı, Busuu/English Online eklenince 8 saatin yaklaşık %65–75'i. Nation'a göre LFL toplam sürenin %25'ini geçmemeli, akıcılık en az %25 olmalı.
3. **Girdi miktarı çok düşük.** Günde 20 dk okuma + 20 dk dinleme, 180 günde yaklaşık 0,4–0,5 milyon okunan kelime eder. IELTS Academic okuma metinlerinin %95'ini anlamak için ~4.000 kelime ailesi gerekiyor; orta sıklıktaki kelimeleri bağlam içinde yeterince görmek için çok daha fazla okuma şart.
4. **Hedef, etiketinden yüksek ve planın hız varsayımı üst sınırda.** IELTS'in kendi araştırması C1 eşiğini 6.5 ile 7.0 arasına koyuyor. Planın 120. günde 5.0–5.5 bekleyip 170–180. günde 6.5 istemesi ~8 haftada +1,0–1,5 bant demek. Karşılaştırma: yoğun kurslarda 10–12 haftada ortalama ~0,5 bant; IELTS'in aktardığı bir örnekte haftada ~60 saat çalışan öğrenci 3 ayda +1,0 bant. Sizin saat yoğunluğunuzla bile 6.5, ancak 120. gün denemesi 5.5 ve üzerindeyse gerçekçi.
5. **IELTS'e özgü çalışma çok geç başlıyor ve Writing/Speaking için insan geri bildirimi yok.** Türk adayların en zayıf becerisi istikrarlı biçimde Writing; yapay zekâ puanlamasının güvenilirliği ise araştırmalarda karışık.
6. **Bilimsel görünümlü ama yanlış ya da doğrulanamayan iddialar:** ELSA'da "spektrogram kontrolü", "dalga biçimlerini karşılaştırma", *fosilleşme* kavramının yanlış kullanımı, "iç sesi (subvocalization) kapatarak oku", "ana dili İngilizce olanlar dakikada 200 kelime okur", "gölgelemenin (shadowing) yaratıcısı Arguelles", "B2.2 akustik çıktısı yapısal olarak garanti".
7. **Belgeler arası ve belge içi çelişkiler:** 40 ve 37 kart; English Online hem "opsiyonel" hem "günde 3 saat zorunlu"; "General" örnek cevaplar; eksik gün numarası; tanımsız "konsolidasyon günü" ve fazlası (bkz. §3).

### Gerçekçi beklenti (kanıta dayalı tahminim)

Bu bir kehanet değil; §1'deki verilere dayanan bir tahmin:

| Senaryo | 120. gün tam deneme | 180. gün | Koşul |
|---|---|---|---|
| İyimser | 5.5 ve üzeri | **6.5** (ör. L 7.0 · R 6.5 · W 6.0 · S 6.0) | Plan revize edilir; günde 6–7 etkili saat; haftalık insan geri bildirimi |
| Gerçekçi | 5.0–5.5 | **6.0** (Writing 5.5–6.0) | Plan revize edilir ama zaman taşmaları olur |
| Riskli | 5.0'ın altı | **5.5 ve altı** | Plan bu haliyle uygulanır; tükenmişlik, atlanan girdi/çıktı |

Bu yüzden planın kendi karar kuralını (denemeler yeterli değilse sınavı kaydırma) ciddiye almanız, planın geri kalanı kadar önemlidir.

---

## 1. Hedef ve süre gerçekçi mi?

### 1.1 "B2.2" ile "IELTS 6.5" aynı şeyi söylemiyor

- 🟡 CEFR'de resmî bir "B2.2" alt düzeyi yoktur; Avrupa Konseyi'nin ölçeklerinde B2 ve bir ara basamak olarak **B2+** bulunur. "B2.1/B2.2" bölmesi bazı kurumların kendi iç ayrımıdır.
- ✅ IELTS'in resmî açıklamasına göre IELTS bantları CEFR geçiş noktalarıyla birebir örtüşmez; **IELTS'in kendi araştırması C1'in alt eşiğini 6.5 ile 7 arasına yerleştirir.** 6.5 alanların çoğu C1'dedir ama bir kısmı eşiğin biraz altındadır; C1'den emin olmak isteyen kurumlara 7 istemeleri önerilir ([IELTS and the CEFR](https://ielts.org/organisations/ielts-for-organisations/compare-ielts/ielts-and-the-cefr)).
- **Sonuç:** Hedefiniz pratikte "B2+ / C1 eşiği". Ancak genel bant dört bölümün ortalaması olduğu için 6.5'e farklı profillerle ulaşılabilir (bkz. §1.4). İlerlemeyi CEFR etiketiyle değil, tam süreli IELTS denemeleriyle ölçün.

### 1.2 Saat hesabı

| CEFR düzeyi | Cambridge'in tahmini kümülatif rehberli öğrenme saati |
|---|---|
| A2 | ~180–200 |
| B1 | ~350–400 |
| B2 | ~500–600 |
| C1 | ~700–800 |

Kaynak: [Cambridge English — Guided learning hours](https://support.cambridgeenglish.org/hc/en-gb/articles/202838506-Guided-learning-hours). Cambridge bu rakamların kaba bir rehber olduğunu, kişiye göre değiştiğini vurgular.

- Planın nominal hacmi: 8 saat × 180 gün = **1.440 saat**. Saf saat olarak bu, C1 için verilen rehberli saati bile aşar. Yani **asıl sorun saat sayısı değil; saatlerin niteliği, sürdürülebilirliği ve dağılımı.**
- Rehberli saat ≠ kendi kendine çalışma saati. Konuşma ve yazma gibi üretken beceriler geri bildirim olmadan aynı hızla gelişmez.
- **Sıkıştırma etkisi.** ABD Dışişleri Enstitüsü (FSI), İngilizce konuşanlar için Türkçeyi Kategori III'e koyar: profesyonel çalışma yeterliliğine (≈C1) **44 hafta / ~1.100 ders saati** + günlük bireysel çalışma ([FSI sıralaması — ikincil kaynak](https://en.wikibooks.org/wiki/Wikibooks:Language_Learning_Difficulty_for_English_Speakers)). Diller arası uzaklık simetrik olmasa da fikir verir: Plan benzer bir hacmi 26 haftaya sıkıştırıyor.
- **Türkiye'den karşılaştırma.** ODTÜ Temel İngilizce Bölümü haftada 20–25 ders saatiyle çalışıyor ([METU DBE](https://dbe.metu.edu.tr/gen_en.htm)); bir akademik yıllık hazırlık ~550–800 ders saati + ödev demek. ODTÜ'nün eşdeğerlik tablosunda muafiyetle ilişkilendirilen IELTS değeri 6.5 ([METU equivalence table](https://oidb.metu.edu.tr/en/equivalence-table-english-language-exams-recognized-metu-undergraduate-and-graduate-students); hangi programa ve yıla uygulandığı kaynaklarda net değil, güncel tabloyu kontrol edin). Yani üniversite hazırlık okulları, sizin 6 ayda hedeflediğiniz düzeye benzer bir çıkış için yoğun bir akademik yıl ayırıyor.

### 1.3 Sürdürülebilirlik

- Ericsson, Krampe ve Tesch-Römer'in (1993) "bilinçli pratik" makalesi, günde 1–8 saatlik pratik sürelerini karşılaştıran çalışmaların **4 saatin üzerinde neredeyse hiç ek fayda, 2 saatin üzerinde azalan fayda** gösterdiğini aktarır ([makaleden alıntı](https://acesounderglass.com/2019/06/21/epistemic-spot-check-the-role-of-deliberate-practice-in-the-acquisition-of-expert-performance/); özgün kaynak: *Psychological Review* 100(3), 363–406). Bu, dil öğrenimi için birebir ölçülmüş bir sınır değil; ama dinlenme günü olmadan 180 gün boyunca günde 8 saat yoğun çalışmanın verimi hakkında güçlü bir uyarı.
- **Öneri:** 8 saati "6–6,5 saat yoğun + 1,5–2 saat düşük yoğunluklu girdi (dizi, YouTube, kolay podcast)" diye bölün; haftada bir hafif gün (≤3 saat) bırakın.

### 1.4 Puan artışı araştırmaları ve planın kontrol noktaları

| Kaynak | Bulgu |
|---|---|
| [Elder & O'Loughlin (2003), IELTS Research Reports Vol. 4](https://ielts.org/researchers/our-research/research-reports/investigating-the-relationship-between-intensive-english-language-study-and-band-score-gain-on-ielts) | 112 öğrenci, 10–12 haftalık yoğun İngilizce: ortalama ~0,5 bant artış, büyük bireysel farklar |
| [Kang vd. (2021), IELTS araştırma raporu](https://ielts.org/researchers/our-research/research-reports/investigation-of-relationships-between-learner-background-linguistic-progression-and-score-gain-on-ielts) | 52 öğrenci, 3 ay IELTS hazırlık: ortalama ~0,3 bant; artışı en iyi **çalışma saati** ve başlangıç düzeyi yordadı |
| [IELTS (2023), "How long will it take…"](https://ielts.org/news-and-insights/how-long-will-it-take-to-get-the-ielts-band-score-i-need) | Haftada ~60 saat çalışan bir öğrenci 3 ayda +1,0 bant; başka bir öğrenci hiç ilerlemedi |

- **Planınız:** 120. gün 5.0–5.5 → 170–180. gün 6.5 ⇒ ~8 haftada +1,0–1,5 bant. Haftada ~56 saatlik yoğunluğunuzla bile bu, gözlenen hızların **üst sınırında**. 6.5, ancak 120. gün denemesi 5.5 civarı veya üstündeyse gerçekçi.
- **Genel bant hesabı işinize yarar.** Genel bant dört bölümün ortalamasıdır; ,25 ile biten ortalamalar bir üst yarım banda, ,75 ile bitenler bir üst tam banda yuvarlanır ([IDP — band score calculation](https://ielts.idp.com/canada/results/band-score-calculation)). Örnekler: 6.5 + 6.5 + 6.0 + 6.0 → 6,25 → **6.5**; 7.0 + 6.5 + 6.0 + 6.0 → 6,375 → **6.5**. Dinleme ve okuma en hızlı geliştirilebilen bölümlerdir; 6.5'e giden en olası yol L/R'yi 6.5–7.0'a taşıyıp W/S'yi 6.0'da tutmaktır. **Ancak** başvuracağınız kurum bölüm bazında asgari puan (ör. "hiçbir bölüm 6.0'ın altında değil") istiyorsa ona göre planlayın.
- **Türk adayların profili.** Farklı yıllara ait ve kısmen ikincil kaynaklardan aktarılan tablolarda Türkiye/Türkçe ana dilli Academic adaylarının en düşük ortalaması hep **Writing** (ör. tarihsiz bir tabloda L 6.6 · R 6.5 · **W 5.7** · S 6.2 — [GeeksforGeeks](https://www.geeksforgeeks.org/ielts/average-ielts-score/); 2024–25 için üçüncü taraf bir derlemede genel 6.43, **Writing 5.93**, Speaking 6.22 — [ieltsmentor](https://www.ieltsmentor.ai/guides/ielts-test-taker-statistics-2024-2025/)). Aynı derlemeye göre tüm Academic adayların genel ortalaması ~6.2. Güncel resmî tablo: [IELTS test statistics](https://ielts.org/researchers/our-research/test-statistics). Sonuç: Writing'e erken başlamak ve insan geri bildirimi almak şart.

---

## 2. Zaman bütçesi denetimi

### 2.1 "8 saat" kâğıt üzerinde tutuyor, gerçekte tutmuyor

Ana Plan'ın toplamı: 180 dk sabah LFL + 40 dk girdi + 50 dk çıktı + 30 dk akıcılık = 300 dk; + Busuu veya English Online 180 dk = **480 dk (8 saat)**. Toplam doğru; sorun, sabah bloğunun içine yazılanlarda:

| Sabah bloğundaki iş | Planda ayrılan | Gerçekçi tahmin | Dayanak |
|---|---|---|---|
| Ses-yazım bloğu | 25 dk | 25 dk | Plan |
| Anki: tekrar + 37 yeni kart | 40 dk | **45–60 dk** (cevap başına 8 sn) · **70–80 dk** (12 sn) | FSRS-6 simülasyonu (§2.2) |
| Kart üretimi: deftere yazma + bağlam + görsel + ses (37 kart) | — | **40–75 dk** | Varsayım: kart başına 1–2 dk |
| Empower: her gün 1 ünite + x-5 ve x-30 tekrarı + boş kâğıda dökme | — | **2–3 saat** | Önceki baskıda her seviye ~80 saatlik sınıf çalışması olarak tanımlanıyor (ikincil kaynak); ünite = A–D dört ders + tekrar/yazma bölümü ([Cambridge Empower](https://www.cambridge.org/empower)) |
| Murphy ünitesi (sol sayfa + alıştırmalar) | — | 30–45 dk | — |
| Empower Workbook (ertesi sabah) | — | 30–60 dk | — |
| ELSA protokolü | 30 dk | 30 dk | Plan |
| **Toplam** | **180 dk** | **≈ 5–7 saat** | |

Buna Busuu/English Online'ın 3 saati ve Nation zincirinin 2 saati eklenince gerçek gün **10–12 saate** çıkıyor. Bu mümkün olmadığından plan uygulamada kendi kendini kırpacak — ve büyük olasılıkla en değerli kısımlar (okuma, dinleme, yazma, konuşma) feda edilecek.

### 2.2 Anki iş yükü (FSRS-6 simülasyonu)

FSRS-6 varsayılan parametreleri, hedef hatırlama oranı %90, 3 rastgele tekrarın ortalaması (ayrıntı: Ek A).

| Günlük yeni kart | 30. gün | 90. gün | 141. gün | 180. gün | 180. günde toplam kart |
|---|---|---|---|---|---|
| 20 | 23 dk | 28 dk | 29 dk | 30 dk | 3.600 |
| 25 | 27 dk | 35 dk | 38 dk | 39 dk | 4.500 |
| 30 | 31 dk | 40 dk | 46 dk | 48 dk | 5.400 |
| **37 (plan)** | **40 dk** | **50 dk** | **56 dk** (≈357 cevap) | **58 dk** | 6.660 |
| 37, cevap başına 12 sn | 49 dk | 64 dk | 70 dk | 76 dk | 6.660 |
| 47 (plan + Empower kelimeleri) | 51 dk | 64 dk | 72 dk | 74 dk | 8.460 |
| 37 + "5 saniye kuralı"* | 69 dk | 115 dk | 137 dk | 158 dk | 6.660 |

\* Doğru ama yavaş hatırlanan kartların bir kısmına (genç kartlarda %15, olgun kartlarda %5) "Again" basıldığı varsayımı. Sonuç varsayıma duyarlı; ama yön değişmiyor: yük 2–2,5 katına çıkabiliyor.

**Okuma:**
1. Planın 55 dk tahmini doğru mertebede ✅; ama Anki'ye ayrılan 40 dk ancak **~25 yeni kart/gün** ile tutuyor ❌.
2. "5 saniye kuralı" planın en büyük gizli zaman maliyeti.
3. Kart üretim süresi hiçbir yerde bütçelenmemiş.

### 2.3 Diğer kalemler

- **English Online Platinum** haftada 3 canlı grup dersi (55 dk) ve ayda 25'e kadar 25 dakikalık webinar içeriyor ([British Council English Online](https://englishonline.britishcouncil.org/flexible-english-online-course/)). "Günde 3 saat English Online"un büyük kısmı canlı ders değil, kendi kendine çalışma olur — Empower/Murphy ile örtüşen bir LFL bloğu.
- **Busuu** kendini "günde 10 dakika" ile konumlandırıyor ([Busuu — How it works](https://busuu.com/en/it-works)); dersler kısa oturumlar için tasarlanmış. Günde 3 saat hem içerik tekrarına hem de Empower ve Murphy ile çakışmaya yol açar.

---

## 3. Tutarsızlıklar

1. Günlük yeni kart: "40-40 ilerlenecek" ↔ "30 headword + ~7 opak türev = ~37 kart".
2. Anki süresi: blokta 40′ ↔ planın kendi zirve tahmini 55 dk.
3. English Online: Ana Plan'da B1 → B2.2 arası **günde 3 saat** ↔ Son Faz'da "Ön Koşul (Opsiyonel)… yalnızca temel dil altyapısında majör eksiklik varsa".
4. Son Faz'ın LFL öncelik listesinde Busuu var (Ana Plan'a göre B1'de bırakılmış olmalı); English Online yok.
5. Ana Plan "General örnek cevaplar" diyor ↔ Son Faz "General örnekleri Academic'le değiştirin" diyor. Hedef Academic ise baştan Academic kullanılmalı.
6. Son Faz'daki ikinci kontrol noktasında gün numarası eksik ("gün: deneme sonucunuz 5.5–6.0'ın altındaysa…"); büyük olasılıkla Word'ün otomatik numaralandırmasında kaybolmuş.
7. Son Faz'da boş parantezler "()" var — formüller/semboller kopyalanırken kaybolmuş; son cümle yarım ("varyansı () sabitlem").
8. "Konsolidasyon günü" tanımlanmamış: hangi gün, kaç kelime, ne kadar süre?
9. "Aktif Test… Takıldığınız yerde… tekrar kapatın. Eğer sorun yoksa" cümlesi yarım kalmış.
10. Son Faz başlığı "TÜM BUNLAR BİTTİKTEN SONRA" diyor ↔ içerik "son 6–7 hafta" ve "120. gün" diyerek 180 günün içine yerleşiyor.
11. Ana Plan "dört bileşen de her gün çalışılır" diyor ↔ seviye tablosunda A1'de çıktı yalnızca çift yönlü çeviri; günlük 50 dk MFO A1'de neyle dolacak belirsiz.
12. ELSA protokolü "izole seslerde ≥%80 olmadan cümle düzeyi akıcılığa geçme" diyor ↔ seviye tablosu A2'de günlük monolog, B1'de 4/3/2 istiyor.
13. Okuma eşiği üç farklı biçimde verilmiş: "%95–98 (20 kelimede en fazla 1)", "Du ≤ %2" ve "sayfada 10'dan fazla bilinmeyen varsa uygun değil" — bunlar aynı eşik değil (bkz. §4.10).
14. "BNC/COCA word family listesi" (Paul Nation'ın listeleri) ile "COCA kelime listeleri" (farklı bir sıklık listesi) aynı şeymiş gibi kullanılmış.
15. Empower serisi A2'den başlatılmış; sıfırdan başlayan biri için A1 (Starter) atlanmış.
16. "Sana verdiğim kelimelerin kökünü önce basit iki üç kelimelik bir bağlamda kullan sonrasında ekler." satırı bir yapay zekâ komutunun kalıntısı gibi duruyor (kartları YZ ile üretecekseniz bkz. §4.2).

---

## 4. Ana Plan — satır satır

### 4.1 "Evde Tek Başına Sıfırdan B2.2'ye İngilizce — Günde 8 saat çalışılacak"

🟡 Hacim olarak (1.440 saat) yeterli; ama §1.3 ve §2'deki nedenlerle bu haliyle sürdürülemez.
**Öneri:** 6–6,5 saat yoğun + 1,5–2 saat düşük yoğunluklu girdi; haftada bir hafif gün.

### 4.2 Anki ve BNC/COCA listeleri

**"BNC/COCA word family listesinden 40-40 ilerlenecek"** — 🟡

- ✅ Sıklık temelli liste seçimi doğru. IELTS Academic okuma metinlerinin %95'ini kapsamak için ~4.000, %98'i için ~9.000 BNC/COCA kelime ailesi gerekiyor; dinleme metinleri için bu eşikler ~3.000 ve ~5.000 ([SAGE Open 2025 — IELTS reading](https://journals.sagepub.com/doi/xml/10.1177/21582440251362269); [SAGE Open 2022 — IELTS listening](https://journals.sagepub.com/doi/xml/10.1177/21582440221079934)). Günde 30 başlık kelimeyle ~135. günde 4.000 aileye ulaşırsınız — hedefle uyumlu.
- 🟡 Nation'ın dosyalarında her 1.000'lik bant içinde başlık kelimeler **alfabetik** sıralıdır ([ikincil kaynak](https://bunkyo.repo.nii.ac.jp/record/7521/files/BKK0003688.pdf); listelerin yapısı: [Information on the BNC/COCA lists](https://vuw-web.matrix.squiz.cloud/__data/assets/pdf_file/0004/1689349/Information-on-the-BNC_COCA-word-family-lists-20180705.pdf)). "Aile 1–30" diye sırayla gitmek, aynı harflerle başlayan benzer biçimli kelimeleri (*accept, access, accident, account…*) aynı güne yığar.
  **Öneri:** Her 1.000'lik bandı karıştırarak ilerleyin; 1k listedeki işlev sözcüklerini (*the, of, and, be…*) kart yapmayın — onlar gramer ve okumayla öğrenilir.
- 🟡 Alternatif/ek: [Oxford 3000/5000](https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000) her kelimeye CEFR düzeyi verir (Oxford 3000'de A1: 900, A2: 800, B1: 700, B2: 600 kelime; Oxford 5000 B2–C1 için ~2.000 kelime ekler). Seviye seviye ilerleyen bir planla daha uyumludur.

**"Headword'deki kelimeleri 2-3 kelimelik mikro bağlam içinde… önce defterime not alacağım sonra Anki'ye kart olarak yükleyeceğim"** — 🟡

- ✅ Mikro bağlam (ör. *make a decision*) iyi fikir; kelimeyle birlikte eşdizimini de öğretir.
- ❌ Zaman maliyeti bütçelenmemiş (§2.1).
  **Öneri:** Defter adımını yalnızca opak türevler ve zor kelimelerle sınırlayın; ses için Anki'nin metin-okuma (TTS) eklentisini, görseli yalnızca somut isimler için kullanın.
- Kartları yapay zekâyla üretiyorsanız, Türkçe karşılıkları ve örnek bağlamları bir öğrenci sözlüğüyle (Oxford/Cambridge/Longman) örnekleme yoluyla kontrol edin.

**Türetilmiş biçimler: şeffaf olanları ekleme, opak olanları ayrı kart yap** — ✅ (gerekçe 🟡)

- ✅ Mantıklı bir verim stratejisi. Örnekler doğru: *inflammable* "kolay tutuşan" demektir (*in-* burada olumsuzluk değil); *corner*'ın *corn* ile ilgisi yoktur; *department* "ayrılma" değil "bölüm" demektir.
- 🟡 "Kökü ve eki bilmek yeterlidir, metinlerde gördükçe anlayacaksınız" ancak sık ekleri bilinçli olarak öğrenirseniz doğru olur.
  **Öneri:** En sık 20–25 eki (*un-, re-, -er, -ness, -ment, -tion, -able, -ful, -less, -ly…*) tek seferlik küçük bir destede öğrenin ([Nation — word parts](https://jalt-publications.org/articles/28460-expositions-word-parts-and-language-learning)).
- 🟡 "Yeniden inşa pratiği… aktif (konuşma/yazma) becerilerde doğru kullanılmasını sağlar" — abartılı. Tanıma kartı (İngilizce → Türkçe) ağırlıklı olarak **alıcı** bilgiyi geliştirir; üretken bilgi için üretken çalışma gerekir ([Webb — receptive vs productive learning](https://ir.wgtn.ac.nz/handle/123456789/23701)).
  **Öneri:** En sık 2.000 kelimenin ve Akademik Kelime Listesi'nin bir kısmı için ters yön (Türkçe → İngilizce) kart ekleyin ya da kelimeyi o günkü yazıda kullanın (planın 6.2'deki "altın kuralı" bunu kısmen yapıyor ✅).

### 4.3 Ses-yazım bloğu (25′)

| Plandaki ifade | Değerlendirme |
|---|---|
| "Harf adı ≠ harf sesi · 26 harf, 44 ses" | ✅ Standart İngiliz telaffuzunda (RP) 24 ünsüz + 20 ünlü = 44 ses birimi ([Open Book Publishers](https://books.openbookpublishers.com/10.11647/obp.0053/ch2.xhtml)); Amerikan İngilizcesinde sayım farklıdır. |
| "Sesi 4-5 farklı konuşmacıdan dinle (Forvo/YouGlish), gözler kapalı ayırt et" | ✅ Yüksek değişkenlikli sesletim eğitiminin (HVPT) temel ilkesi; 32 çalışmalık bir sentez algıda güçlü etki gösteriyor ([Thomson 2018](https://www.benjamins.com/catalog/persons/957094395)). Üretime aktarım daha sınırlı/karışık. |
| "100-250 deneme — English Accent Coach" | ✅ Ron Thomson'ın araştırmaya dayalı ücretsiz web oyunları; amaç aksan değiştirmek değil, sesleri ayırt etmek ([Brock University](https://brocku.ca/brock-news/2012/02/app-and-website-help-non-english-speakers-learn-the-accent/)). |
| "10 kelime yaz — bu dikte değil, kodlama" | ✅ Ses → harf eşleştirmesi. IELTS Listening'de yazım hatası puan kaybettirdiği için ayrıca değerli. |
| "Türkçe tuzağı: school ≠ iskul" | ✅ Türkçe söz başında ünsüz kümesine izin vermez, araya ünlü ekler ([Ülkersoy vd. 2021](https://doaj.org/article/9c649dd6324c4d44a1cd6cf24c08b92c)). |

### 4.4 Anki kuralları

| Plandaki ifade | Değerlendirme |
|---|---|
| "Due kartların hepsini bitir" · "Önce birikmiş tekrarlar" · "Tekrarı asla erteleme; yeni kartı kısmak bozmaz" | ✅ Doğru öncelik. |
| "5 saniyede gelmiyorsa Again" | 🟡/❌ Anki kılavuzu: **Again** yanlış ya da hatırlanamayan cevap içindir; **Hard** doğru ama uzun sürmüş ya da şüpheli cevap içindir ([Anki Manual](https://docs.ankiweb.net/studying.html)). Kural otomatikleşmeyi hedefliyor ama simülasyonda yükü 2–2,5 katına çıkarabiliyor (§2.2). **Öneri:** yavaş ama doğru → Hard; hiç gelmedi → Again. |
| "Unuttuğunda asla Hard'a basma" | ✅ FSRS, Hard'ı başarılı hatırlama sayar; unutulan kartta Hard aralıkları gereksiz uzatır ([Anki forumu](https://forums.ankiweb.net/t/an-info-tip-regarding-recommended-button-usage/39834)). |
| "Serpiştirme: ana desteyi çalış… deste deste çalışmak tutturmayı düşürür" | ✅ sonuç, 🟡 gerekçe. Kelimelerde asıl kanıt, anlamca ilişkili kelimeleri birlikte öğrenmenin karışıklığa yol açması: Türk öğrencilerle yapılan bir çalışmada ilişkisiz setler daha iyi hatırlandı ([Erten & Tekin 2008](https://avesis.comu.edu.tr/yayin/4a84e8a3-294d-457c-9e11-65cbf94493a0/effects-on-vocabulary-acquisition-of-presenting-new-words-in-semantic-sets-versus-semantically-unrelated-sets)). Empower kelimelerini tematik alt destelerde tutacaksanız karışık çalışmak yerinde. |
| "Ön yüz = headword mikro-bağlam içinde + görsel; arka yüz = TR karşılık + ekler + ses" | 🟡 Ön yüzde anlamı gösteren bir görsel varsa kart kelimeyi değil **resmi** tanımayı test eder. **Öneri:** Görseli arka yüze alın; ses ön yüzde (ya da ayrı bir "dinle-anla" kartında) olsun ki dinlemede tanıma da gelişsin. |
| "Zirve yük Gün ~141: 337 tekrar ≈ 55 dk" | ✅ Simülasyonla tutarlı (≈357 cevap, ≈56 dk) — ama 40′'lık bloğa sığmıyor ❌. |
| "400'ü sürekli aşarsan opak türevi 7'den 4'e indir" | ✅ Doğru türden bir emniyet supabı. Ek kural önerisi: günlük Anki süresi üç gün üst üste 45 dk'yı aşarsa yeni kartı %20 azaltın. |

### 4.5 Cambridge Empower

| Plandaki ifade | Değerlendirme |
|---|---|
| "Empower (A2, B1, B1+, B2 SB + WB)" | 🟡 Seri 6 seviyeli (A1–C1), 2. baskı Ocak 2022 ([Cambridge](https://www.cambridge.org/empower)). Sıfırdan başlayan biri için **A1 Starter atlanmış**; Busuu A1 ve Essential Grammar in Use bu boşluğu kısmen kapatır ama Empower A2'nin varsaydığı temel eksik kalabilir. |
| "Her gün bir ünite" | ❌ Her ünite dört ders (A–D) + tekrar/yazma bölümünden oluşuyor; önceki baskıda her seviye ~80 saatlik sınıf çalışması olarak tanımlanmış (ikincil kaynak). Bir üniteyi 1 saatte "bitirmek" yüzeysel kalır. **Öneri:** 2–3 günde bir ünite → dört kitap (kitap başına 10–12 ünite varsayımıyla) ≈ 100–130 günde biter; bu da 180 günlük takvimle uyumlu. |
| "X. ünite çalışırken x-5 ve x-30 tekrar" | ✅ Aralıklı tekrar; aralıklı pratiğin dil öğrenimindeki olumlu etkisi meta-analizle destekli (Kim & Webb 2022, *Language Learning* 72(1), 269–319). Ünite hızı 2–3 güne çıkarsa "x-2 ve x-10" daha uygun olur. |
| "Hatırladıklarını boş kâğıda dök ve kontrol et" | ✅ Geri çağırma pratiği — en güçlü öğrenme tekniklerinden biri. |
| "Sesleri atlamadan" | ✅ |
| "Yeni kelimeleri işaretle, Anki'ye şimdi ekleme — konsolidasyon gününde toplu gireceksin" | 🟡 Konsolidasyon günü tanımsız; ayrıca bu kelimeler BNC/COCA akışının üstüne eklenince yük ~%25 artıyor (§2.2). **Öneri:** Empower kelimelerinden yalnızca BNC/COCA destesinde **olmayanları** ekleyin; haftada bir günü sabitleyin (ör. Cumartesi). |
| "Sentezleyerek not al (kopyalama yok)" | ✅ Üretici not alma. |
| "Kuralın matematiksel formülünü netleştirmek için… Essential (4th) / English Grammar in Use (5th) / Advanced Grammar in Use" | ✅ Baskılar doğru (English Grammar in Use 5. baskı 2019, B1–B2 için; 6. baskıya dair kanıt bulamadım). 🟡 *Advanced Grammar in Use* C1–C2 düzeyidir; B2+ hedefi için gerekmez. 🟡 Gramer "matematiksel formül" değildir; biçim + anlam + kullanım üçlüsüne bakın (ör. *present perfect*'in biçimi kolaydır, ne zaman kullanıldığı zordur). |
| "Ertesi sabah Workbook" | ✅ Kısa aralıklı tekrar. |

### 4.6 Busuu Premium Plus (A1 → B1, günde 3 saat)

- ✅ Ürün 2026'da da listeleniyor (üçüncü taraf fiyat sayfalarına göre); topluluk özelliği (anadili konuşurlarının düzeltmesi), planda az bulunan **insan geri bildirimini** sağlar.
- ❌ Günde 3 saat fazla: Busuu kısa oturumlar için tasarlanmış; Empower + Murphy + Anki ile büyük ölçüde örtüşüyor. Busuu'nun "22 saat = bir üniversite dönemi" iddiası, Busuu'nun kendi sitesinde yayımladığı, kontrol grubu tarif edilmeyen ve İspanyolca başlangıç öğrencileriyle yapılmış bir çalışmaya dayanıyor ([Busuu study](https://www.busuu.com/en/research/university-study)); İngilizce B1 sonucu hakkında bir şey söylemiyor.
- 🟡 "B1 seviyesine gelince bırak": Uygulamadaki B1 kursunu bitirmek, B1 yeterliliğine ulaşıldığı anlamına gelmez.
- **Öneri:** En fazla 30–45 dk/gün ve yalnızca Faz A–B'de; ya da tamamen çıkarıp o süreyi okumaya verin.

### 4.7 English Online (B1 → B2.2, günde 3 saat)

- ✅ British Council English Online gerçek; seviye belirleme sınavı var; Platinum en popüler plan ([English Online](https://englishonline.britishcouncil.org/flexible-english-online-course/)).
- 🟡 Platinum: haftada 3 canlı grup dersi (55 dk) + ayda 25'e kadar 25 dakikalık webinar. Günde 3 saatin çoğu canlı değil, kendi kendine çalışma olur.
- ❓ "B2.2" alt düzeyini kullandığına dair kaynak bulamadım.
- ❌ Son Faz'da "opsiyonel" — belgeler çelişiyor.
- **Öneri:** Canlı dersleri (planın tek düzenli insan etkileşimi) koruyun; ama "günde 3 saat" yerine haftada ~5–6 saatlik canlı ders + webinar olarak sayın. Faz C–D'de yanına IELTS deneyimli bir eğitmenle haftada 2 Speaking/Writing seansı ekleyin.

### 4.8 "2 haftada 1 … Cambridge sitesindeki resmî materyaller … General örnek cevaplar … yapay zekâ ile değerlendir"

- ✅ Resmî örnek testler ve puanlama ölçütleri doğru başlangıç noktası.
- ❌ **General** değil **Academic** örnekleri kullanın (Academic Writing Task 1 grafik/süreç/harita betimler; General Training Task 1 mektuptur).
- 🟡 Yapay zekâ puanlaması: GPT-4 ile yapılan bir IELTS Task 2 çalışmasında ortalamalar insan puanlarına yakın çıktı ama tekil metinlerde ciddi sapmalar görüldü ve yazar YZ'nin insanın yerini almaması gerektiği sonucuna vardı ([Koraishi 2024](https://avesis.uludag.edu.tr/yayin/9610a41d-001d-4f22-834e-579fe0ae99dd/the-intersection-of-ai-and-language-assessment-a-study-on-the-reliability-of-chatgpt-in-grading-ielts-writing-task-2)); GPT-4o ile yapılan daha yeni çalışmalar daha zayıf ve tutarsız uyum buldu ([GPT-4o çalışması](https://avesis.iuc.edu.tr/yayin/a433340f-6e81-4eb6-ba9f-f334fca4e436/chatgpt-4o-as-an-automated-scoring-tool-for-writing-assessment-strengths-and-weaknesses); [çok modelli IELTS karşılaştırması](https://abdn.elsevierpure.com/en/publications/from-prompts-to-scores-generative-ai-versus-human-grading-in-writ)).
  **Öneri:** YZ'yi hata bulma ve yeniden yazma için kullanın; bant tahmini için resmî örnek cevaplar + insan değerlendirici (eğitmen veya IELTS Progress Check) kullanın.

### 4.9 ELSA sesletim protokolü (Faz 1–3 ve "kritik kurallar")

**Genel çerçeve** — 🟡/❌

- Protokol "anadil konuşuru gibi ses" (nativeness) hedefliyor. Alan araştırması 1990'lardan beri **anlaşılırlığı** (intelligibility) ve kolay anlaşılmayı (comprehensibility) öncelikli görüyor; aksan belirgin olsa da konuşma yüksek derecede anlaşılır olabilir ([Munro & Derwing 1995 ve sonrası](https://www.benjamins.com/catalog/bct.121)).
- CEFR'in 2020 güncel sesbilgisel denetim ölçeğinde B2: tonlamayı ve vurguyu genelde doğru kullanır, sesleri net çıkarır; **aksanı diğer dillerden etkilenmiştir ama anlaşılırlığa etkisi az ya da hiç yoktur** ([CEFR CV — phonological control](https://rm.coe.int/the-new-scale-for-phonological-control-piccardo-/1680788b29)).
- IELTS'te sesletim dört ölçütten biri (%25); değerlendiriciler aksanı değil konuşulan İngilizceyi değerlendirir ([IDP](https://ielts.idp.com/uae/prepare/article-accents-ielts-speaking-scores/en-gb)). 8. bantta bile "aksanın anlaşılırlığa etkisi minimal" ifadesi geçer ([IELTS Speaking band descriptors](https://ielts.org/cdn/ielts-downloadable-assets/ielts-guidance-and-support/ielts-guides/ielts-speaking-band-descriptors.pdf)).

**Faz 1 (L0 → A2): izole ses birimleri, ELSA ≥%80**

- ✅ Ölçülebilir bir geçiş kriteri koymak iyi; asgari çiftler (minimal pairs) doğru araç. Ama ELSA puanı otomatik konuşma tanımaya dayalı bir tahmindir, anlaşılırlığın kendisi değildir.
- 🟡 Örnek olarak /θ/–/ð/ ile başlamak verimsiz. Bu karşıtlığın **işlevsel yükü** düşüktür (az sayıda kelimeyi ayırt eder); yüksek işlevsel yüklü hatalar anlaşılırlığı daha çok düşürür ([işlevsel yük derlemesi](https://frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.627378/full)).
- **Türkçe konuşanlar için öncelik listesi önerisi:**
  1. Kelime vurgusu, zayıf biçimler ve schwa
  2. /v/–/w/ (*vest/west*) ([Türk öğretmen adayları çalışması](https://avesis.akdeniz.edu.tr/yayin/aeacbeb5-6675-4f5a-be6a-81d85fe35b94/pre-service-english-language-teachers-problematic-sounds))
  3. Söz sonu ötümlü ünsüzlerin ötümsüzleşmesi (*bag → bak*)
  4. Türkçede olmayan ünlü karşıtlıkları: /iː/–/ɪ/ (*sheep/ship*), /æ/–/e/ (*bad/bed*), /ʌ/–/ɑː/ (*cut/cart*)
  5. Ünsüz kümelerine ünlü eklememe
  6. /θ/–/ð/ en sona
- 🟡 "Kelime anlamı veya bağlam analiz edilmez; salt akustik frekans hedeflenir": İlk haftalarda anlamdan bağımsız alıştırma makul; "akustik frekans" ifadesi teknik olarak anlamsız (hedef, doğru ses kategorisidir).

**Faz 2 (A2 → B1): kelime vurgusu, "hece zamanlı Türkçe / vurgu zamanlı İngilizce"**

- 🟡 Dillerin kesin biçimde "hece zamanlı" ve "vurgu zamanlı" diye ikiye ayrıldığı (eşzamanlılık / isochrony) varsayımı ölçümlerle desteklenmemiştir (Roach 1982; Dauer 1983; Arvaniti) ([Arvaniti — ritim](https://kar.kent.ac.uk/45775/)). Ama pratik hedef doğru: İngilizcede vurgusuz hecelerde ünlü zayıflaması ve vurgulu hecenin uzaması öğrenilmeli.
- ✅ *phoTOgraphy / PHOtograph* örneği doğru ve iyi seçilmiş.
- 🟡 "YouGlish'te minimum N = 10 kaynak": zaman açısından pahalı; 3–5 farklı konuşmacı çoğu durumda yeterli.
- 🟡 "F0 tepeleri": İngilizce vurgunun ipuçları yalnızca perde (F0) değil; süre, yoğunluk ve ünlü niteliği de belirleyicidir.
- ❓ "Spektrogram kontrol edilir": ELSA'nın kullanıcıya spektrogram gösterdiğine dair kanıt bulamadım; ELSA sesleri renk kodlu (yeşil/sarı/kırmızı) geri bildirimle gösteriyor. Görsel tonlama geri bildirimi istiyorsanız ücretsiz **Praat** programının perde (pitch) eğrisi işe yarar.

**Faz 3 (B1 → B2.2): bağlantılı konuşma, shadowing, ELSA Speech Analyzer**

- ✅ İçerik/işlev kelimesi işaretleme, bağlama (linking) noktaları, A/B döngüsü ve hata raporunun bir sonraki döngüye aktarılması mantıklı. Döngü B'deki 2–3 dakikalık serbest konuşma, IELTS Speaking Part 2'ye iyi hazırlık.
- ❌ "Dalga biçimlerini (waveform) mukayese et": Dalga biçimi görüntüsünden telaffuz doğruluğu okunamaz. Kulakla karşılaştırma veya Praat perde eğrisi kullanın.
- 🟡 ELSA Speech Analyzer gerçekten IELTS/TOEFL puan tahmini veriyor ([ISCA SLaTE 2023](https://www.isca-archive.org/slate_2023/anguera23_slate.html)); bağımsız incelemeler tahminin temkinle alınması gerektiğini söylüyor. "Advanced profiline oturmak" ölçütünün tam olarak ne olduğunu doğrulayamadım ❓. Bunu bir ara gösterge olarak kullanın; IELTS Speaking denemesinin yerine koymayın.

**"Kritik kurallar"**

- ❌ **"Fosilleşme kontrolü: ≥%80 olmadan cümle düzeyi akıcılığa geçmeyin… hata motor kortekse kazınır."** *Fosilleşme* (Selinker 1972), bazı ara dil özelliklerinin uzun süre boyunca kalıcılaşıp gelişimin durmasıdır ([Han 2004 incelemesi](https://linguistlist.org/issues/15/2198/)); birkaç haftalık akıcı konuşmanın hatayı "kazıdığına" dair kanıt yok. Tersine, cümle düzeyinde anlamlı konuşmayı geciktirmek konuşma becerisini geciktirir.
  **Öneri:** Cümle/konuşma pratiği ilk haftadan başlasın; ses çalışması paralel yürüsün.
- ✅ "Bilişsel yük: shadowing metinleri kavrama kapasitenizi aşmamalı" — doğru (Nation'ın akıcılık koşuluyla uyumlu).
- 🟡 "İterasyon disiplini: kırmızı fonem düzeltilmeden sonraki kelimeye geçilmez" — mükemmeliyetçilik bir zaman tuzağıdır, getirisi azalır.
  **Öneri:** Kelime başına en fazla 3–5 deneme; sonra işaretleyip ertesi gün tekrar.
- ❌ "Parametrelere tam uyumda B2.2 akustik çıktısına ulaşılması yapısal olarak güvence altındadır." Hiçbir protokol bunu garanti edemez; "B2.2 akustik çıktısı" tanımlı bir ölçüt değildir.

### 4.10 "Paul Nation Protokolüne Dayalı Günlük Plan" (5 saatlik çekirdek)

Not: Nation'ın resmî bir "protokolü" yoktur; Dört Bileşen bir müfredat dengesi ilkesidir.

**Tablo 1 (180 + 40 + 50 + 30) ve 3.2 "Sistem uygunluk ve yeterlilik raporu"** — ❌

- Nation: Dört bileşen kabaca eşit süre almalı; dil maddelerinin doğrudan çalışılması (LFL) toplam sürenin **%25'ini geçmemeli**; akıcılık en az **%25** olmalı ([Nation — Cambridge örnek bölümü](https://assets.cambridge.org/97810090/98359/excerpt/9781009098359_excerpt.pdf)).
- Plan: LFL %60, MFI %13, MFO %17, FD %10 (Busuu/English Online ile LFL ≈ %65–75). "Nation'ın denge prensibine sadık kalan geçerli yegâne mimari" ve "tamamen eksiksiz ve yeterlidir" ifadeleri kanıtsız ve Nation'ın kendi ölçütüyle çelişiyor.
- Not: Sıfırdan başlarken ilk 3–4 haftada LFL'nin daha yüksek olması makul; ama A2'den itibaren %25–30'a inmeli.

**Tablo 2 (seviye seviye)** — 🟡

- A1: "Yalnızca çift yönlü çeviri" çıktı için fazla dar; kısa sesli kayıtlar ve basit cümle yazma da eklenmeli.
- A2: 10 dk serbest yazma + 3 dk monolog ✅
- B1: ChatGPT Voice ile tartışma/rol yapma + 4/3/2 ✅
- B2: kompozisyon + Write & Improve + sesli sunum ✅ (Write & Improve ücretsizdir ve CEFR düzeyi verir; IELTS görevleri ücretli "Test Zone"dadır — [Write & Improve](https://writeandimprove.com/)).
- Kelime hedefleri: A2 500–1.000 ✅; **B1 1.000–2.000 🟡** (Nation: 2.000–3.000); **B2 2.000–4.000 🟡** (Nation: ~4.000; IELTS okumasında %95 kapsama için ~4.000 aile) ([Nation — vocabulary and the CEFR](https://wgtn.ac.nz/lals/resources/paul-nations-resources/vocabulary-lists/vocabulary-cefr-and-word-family-size/vocabulary-and-the-cefr-docx)). Sınava kadar hedefinizi **≥4.000–5.000 aile + Akademik Kelime Listesi (AWL)** olarak koyun.

**3.1 Bağlantılı beceriler zinciri** — ✅ fikir, 🟡 kurgu

- Aynı içeriği okuma → özet yazma → anlatma → hızlı tekrar zinciri iyi. Aynı konuyu tekrar anlatanların akıcılık kazanımlarını koruduğu, farklı konular anlatanların korumadığı gösterilmiş ([De Jong & Perfetti 2011](https://www.lrdc.pitt.edu/perfettilab/pubpdfs/de%20Jong%20Language%20Learning.pdf)).
- Ama sabah Anki'de çalışılan kelimeler frekans listesinden geldiği için o günün metninde çıkmaları tesadüfe kalıyor.
  **Öneri:** Her gün okunan metinden 3–5 hedef kelime/kalıp seçin ve o günün yazma-konuşmasında onları kullanın.

**4. Sabah rutini — "priming"** — 🟡 Güne LFL ile başlamak makul; "beyni günün geri kalanına hazırlar" iddiası kanıtsız bir süs.

**5.1 Bilinmeyen kelime sınırı** — 🟡

- ✅ Hu & Nation (2000) doğru kaynak: 66 öğrenci, %80/90/95/100 kapsama denenmiş; %98'in yardımsız yeterli anlama için gerektiği **çıkarım** olarak önerilmiş. 2023'teki bir tekrar çalışması bulguları tam olarak yineleyemedi ([replikasyon özeti](https://aila2021.dryfta.com/program/abstract-archive/abstract/public/416/unknown-vocabulary-density-reading-comprehension-and-the-98-coverage-figure-replicating-hu-nation-2000)). %98'i katı bir yasa değil, pratik bir kural olarak görün.
- ❌ Planda üç farklı eşik var: %95 = 20 kelimede 1 bilinmeyen; %98 = 50 kelimede 1; "sayfada 10 bilinmeyen" (≈250–300 kelimelik sayfada) ≈ %96–97.
  **Öneri:** Yaygın okuma için ≥%98 (sayfada ≤5–6 bilinmeyen), akıcılık çalışması için ~%100, yoğun/çalışma okuması için %95 kabul.
- 🟡 "Lexical density" terimi başka bir kavramdır (metindeki içerik kelimesi oranı); doğru terim "bilinmeyen kelime yoğunluğu / sözcüksel kapsama (lexical coverage)".

**5.2 Yaygın okuma (20 dk)** — ✅ yöntem, ❌ miktar

- 20 dk/gün, A1'de dakikada ~60–100 kelime okuma hızıyla günde 1.200–2.000 kelime eder; okuma hızı artsa bile 180 günde toplam ~0,4–0,5 milyon kelime (benim varsayımlarımla). Nation'a göre kelimelerle yeterli sayıda (≥12) karşılaşmak için 2. bin düzeyinde ~200 bin, 9. bin düzeyinde ~3 milyon kelimelik girdi gerekiyor ([Nation 2014](https://nflrc.hawaii.edu/rfl/item-detail/303)).
  **Öneri:** Okumayı Faz B'den itibaren günde 45–60 dk'ya çıkarın; B1+'dan sonra Nation'ın ücretsiz **Mid-frequency Readers** dizisini (4.000/6.000/8.000 düzeyleri) kullanın ([Wellington — free graded readers](https://www.wgtn.ac.nz/lals/resources/readers)). Bu, 180 günde ~1,2 milyon kelimelik okuma eder (§8.7).

**5.3 Yaygın dinleme** — ✅ / 🟡

- Görselsiz dinleme ve okurken dinleme ✅.
- 🟡 "Çoklu duyusal işleme kelimeleri kalıcı belleğe kazır": Okuma, okurken dinleme ve yalnız dinleme karşılaştırmasında kelimeler üç yolla da öğrenildi ama **çoğu kelime öğrenilmedi**; sık geçen kelimeler daha iyi öğrenildi ([Brown, Waring & Donkaewbua 2008](https://www2.hawaii.edu/~readfl/rfl/October2008/brown/brown.html)). Okurken dinleme faydalı ama sihirli değil.

**6.1 Çıktı kuralları** — ✅ (anlam odaklı çıktı için)

- "Önce mesaj", "çevreleme (circumlocution)", "düzeltme sonra" ✅. Çevreleme IELTS'te de doğrudan işe yarar (Lexical Resource ölçütü başka sözcüklerle ifade etme becerisini ödüllendirir).
- 🟡 IELTS Writing'de Grammatical Range & Accuracy ve Lexical Resource puanın yarısı. Bu yüzden "yaz → sonra sözlük/araçla düzelt → yeniden yaz" döngüsünü ayrı bir adım olarak planlayın.

**6.2 Yazılı üretim (25 dk, ≥200 kelime)** — 🟡

- A1–A2'de 25 dk'da 200 kelime gerçekçi değil (A2'de 60–100 kelime yeterli). B2'de IELTS Task 2'nin "40 dk'da 250 kelime" ölçüsüne doğru artırın.
- ✅ "Altın kural" (sabah kelimesini ve gramer yapısını kasıtlı kullanmak) itilmiş çıktıdır (pushed output); iyi fikir.

**6.3 Sözlü üretim (ChatGPT Voice / monolog)** — ✅ / 🟡

- ✅ "Fikrimi çürütmeye çalış" komutu IELTS Speaking Part 3 için çok iyi bir hazırlık.
- 🟡 Sesli yapay zekâ "hoşgörülü" bir muhataptır: telaffuz hatalarını çoğu zaman anlayıp geçer, siz istemedikçe düzeltmez. IELTS'te karşınızda insan değerlendirici olacak; insanla konuşma pratiği şart.

**6.4 Çift yönlü çeviri** — ✅ teknik, 🟡 iddia

- Özgün metinle karşılaştırmak "boşluğu fark etme" (noticing the gap) için iyi bir yöntem. "En güçlü yöntemlerden biri" ve "anadil konuşuru kesinliği" abartılı: sizin çeviriniz de doğru olabilir, özgün metin tek doğru değildir. Farkları "hata" ve "alternatif" diye ayırın.

**6.5 Süreli serbest yazma** — ✅ Nation'ın akıcılık etkinliklerinden; yazma hızı ve akıcılığı için iyi.

**6.6 Kayıtlı monolog + yazıya dökme** — ✅ yöntem, 🟡/❌ ayrıntılar

- ✅ Kendi konuşmasını yazıya dökmek dikkati biçime çeker (Lynch 2001, 2007, *ELT Journal*). Ancak öğrencilerin tek başına hatalarının yalnızca bir kısmını fark ettiği de gösterildi (bir çalışmada %25) ([Colombian Applied Linguistics Journal](https://revistas.udistrital.edu.co/index.php/calj/article/view/4989)); transkripti ara sıra bir eğitmene ya da YZ'ye kontrol ettirin.
- 🟡 "Kanıtlanmış en iyi yol" abartılı.
- ❌ "Tıkandığınızda Türkçe bir boşluk doldurucu söyleyin": Türkçe dolgu alışkanlığı sınavda zarar verir. İngilizce dolgular (*well, let me think, what I mean is…*) ve çevreleme kullanın.

**6.7 YZ ve dijital araçlar** — ✅ (§4.8'deki puanlama uyarısıyla).

**6.8 Ana dil aktarımı** — ✅ yön, 🟡 eksik

- Söz dizimi (SVO) ve tanımlıklar ✅. Türk öğrencilerle yapılan hata analizlerinde en sık hatalar **tanımlıklar, kelime seçimi, edatlar (prepositions), söz dizimi ve özne-yüklem uyumu** ([Educational Process 2017](https://doaj.org/article/d6c3cb9e5247484b810aef5d80f6c14e)).
- Kontrol listesine eklenmeli (dilbilgisel gerekçeleriyle):
  - *he/she/it* (Türkçede "o" cinsiyetsiz)
  - Sayılardan sonra çoğul (*two books*; Türkçede "iki kitap")
  - 3. tekil şahıs *-s*
  - Soru ve olumsuzlukta yardımcı fiil (*do/does/did*)
  - Özne zamirini düşürmeme (*It is raining*)
  - İlgi cümlelerinin yeri (Türkçede isimden önce, İngilizcede sonra)
  - *Present perfect / past simple* ayrımı
  - Edatlar
- ❌ "Fosilleşme" burada da yanlış anlamda kullanılmış (bkz. §4.9).

**7. Akıcılık gelişimi** — ✅ İlke ("yeni bilgi yok, hız baskısı var") Nation'la uyumlu; 🟡 süre (%10) düşük.

**7.1 4/3/2** — ✅

- Nation'ın (1989) tekniği; aynı konuyu üç kez ve azalan sürede anlatmak akıcılığı artırıyor ve kazanım korunuyor (De Jong & Perfetti 2011). Tandem/Meetup'ta farklı dinleyicilere anlatmak tekniğin özgün biçimine daha yakın ✅.
- 🟡 "Motor korteksi hızlandırır", "işlem belleğindeki tereddütleri zorla elimine eder" süs; araştırmadaki açıklama, bilginin prosedürel hâle gelmesidir (proceduralization).

**7.2 Gölgeleme (shadowing)** — ✅ teknik, ❌ tarihçe, ❓ yürüyüş

- ❌ "Yöntemin yaratıcısı Alexander Arguelles": Gölgeleme, simültane çevirmen eğitiminde kullanılan bir tekniktir ([Lambert 1992, *Meta*](https://assets.erudit.tech/en/revue/meta/1992/v37/n2/003378ar.pdf)); dil öğretimine 1992'de Japonya'da dinleme tekniği olarak girmiştir ([NJLTL derlemesi](https://journal.uia.no/index.php/NJLTL/article/view/1139)). Arguelles yöntemi 2000'lerde, Assimil kurslarıyla ve yürüyerek yaptığı videolarla **popülerleştirmiştir** ([Connexion](https://www.connexionfrance.com/news/american-who-speaks-50-languages-gives-his-tips-on-learning-french/655715)).
- ❓ "Yürürken yapmak beynin dil işlemesini destekler": bunu gösteren bir araştırma bulamadım; yürüyüş yalnızca bir tercih.
- ✅ "Metin kolay olmalı (%95–98 bilinen)" doğru.
- 🟡 VOA Learning English: 2025'te ABD'deki USAGM kesintileriyle yayınlar büyük ölçüde durdu; Mart 2026'da bir federal mahkeme yayınların yeniden başlatılmasına hükmetti; Ekim 2026'da sitede yeni dersler görünüyor ama süreklilik belirsiz ([Wikipedia — VOA](https://en.wikipedia.org/wiki/Voice_of_America); [JURIST](https://www.jurist.org/news/2026/03/us-federal-judge-orders-voice-of-america-broadcasting-restored/); [VOA Learning English](https://learningenglish.voanews.com/)). Yedek: BBC Learning English, LinguaWire, graded reader sesleri.

**7.3 Hızlı okuma/dinleme** — ✅ / ❌

- ✅ Tekrarlı okuma ve Nation'ın hız okuma metinleri (ör. *Asian and Pacific Speed Readings*: 1.000 kelime düzeyinde, 20 × 550 kelime) ücretsiz ve doğru kaynak ([Speed reading and listening fluency](https://www.wgtn.ac.nz/lals/resources/paul-nations-resources/speed-reading-and-listening-fluency)).
- ❌ "Sese dönüştürmeden (subvocalization olmadan) okuyun": İç sesi bastırma girişimlerinin, makul zorluktaki ve çıkarım gerektiren metinlerde **anlamayı bozduğu** gösterilmiştir; hızlı okuma vaatleri için "hızlı çözüm yok" ([Rayner vd. 2016 — APS](https://www.psychologicalscience.org/news/releases/speed-reading-promises-are-too-good-to-be-true-scientists-find.html)).
- ❌ "Anadili İngilizce olanların ortalama okuma hızı dakikada 200 kelime": 190 çalışmalık meta-analize göre yetişkinlerin sessiz okuma hızı kurgu dışı metinde **238**, kurguda **260** kelime/dk ([Brysbaert 2019](https://www.bps.org.uk/research-digest/most-comprehensive-review-date-finds-average-persons-reading-speed-slower)). İkinci dilde Nation'ın akıcı okuma hedefi, iyi anlamayla ~**250 kelime/dk** ([Reading for Speed and Fluency incelemesi](https://jalt-publications.org/tlt/departments/book-reviews/articles/514-reading-speed-and-fluency-1)).
- 🟡 "Kelimelerin optik formlarının bir bütün olarak algılanması": Akıcı okumada kelime tanıma otomatikleşir; "bütün şekil" açıklaması bir basitleştirme.

### 4.11 Bölüm 8 — Kaynaklar

Ayrıntı için §6'daki doğrulama tablosuna bakın. Öne çıkanlar: ❓ "Oqou" adlı bir kaynak bulamadım; ✅ Extensive Reading Central: düzey ölçeği ~50 kelimeden 12.000–18.000'e kadar uzanıyor ama bir incelemeye göre en zor metinler ~8.000 headword düzeyinde, yani planın "8.000 kelimeye kadar" ifadesi pratikte doğru ([ER-Central levels](https://www.er-central.com/?p=2628); [ERF](https://erfoundation.org/wordpress/useful-resources/useful-sites-2/)) — *ilk sürümde bunu yanlışlıkla hatalı saymıştım*; 🟡 VOA'nın durumu belirsiz.

---

## 5. Son Faz — satır satır

| # | Plandaki ifade | Değerlendirme |
|---|---|---|
| 1 | "TÜM BUNLAR BİTTİKTEN SONRA… SON FAZ" | 🟡 "Bittikten sonra" mı, yoksa 180 günün içindeki son 6–7 hafta mı? Belgenin geri kalanı ikincisini söylüyor; başlığı düzeltin. |
| 2 | "Son 6–7 haftayı Academic'e ayırın" | 🟡 Yön doğru, zamanlama geç. Academic Writing Task 1 (grafik/süreç/harita) ve okuma soru tipleri (True/False/Not Given, Matching Headings…) ayrı beceriler. ~90. günden (B1+) itibaren haftada 2–3 kısa IELTS göreviyle başlayın, son 6–7 haftada yoğunlaştırın. |
| 3 | "MFO saatlerinin yarısını Task 1 ve Task 2'ye verin" | ✅ Task 2, Writing puanında Task 1'in iki katı ağırlığa sahip ([IELTS Australia](https://ielts.com.au/australia/results/scores/writing)); zamanı kabaca 2:1 bölün. |
| 4 | "MFI saatlerinin bir kısmını Academic Reading pasajlarına verin" | ✅ Ham puandan banda dönüşüm yaklaşık: okumada 27–29 doğru ≈ 6.5, 30–32 ≈ 7.0; dinlemede 26–29 ≈ 6.5, 30–31 ≈ 7.0 (tablolar sınav sürümüne göre biraz değişir). |
| 5 | "FD saatlerinin bir kısmını süreli yazmaya verin" | ✅ Yazma akıcılığı için doğru. Ama Speaking akıcılığını (4/3/2) bırakmayın. |
| 6 | "'General' örnekleri Academic örneklerle değiştirin" | ✅ Baştan Academic olmalıydı (§4.8). |
| 7 | "LFL öncelik sıranız: Anki > Empower > Workbook > ELSA > Murphy > Busuu; gün sıkışınca sondan kesin" | 🟡 Kesme listesi fikri çok iyi. Ama (a) Busuu zaten B1'de bırakılmış olmalı, (b) English Online listede yok, (c) asıl korunması gerekenler LFL değil; **denemeler, Writing geri bildirimi ve okuma/dinleme hacmi**. Önerilen kesme sırası §8.5'te. |
| 8 | "Hipotezinizi verilerle test edin" | ✅ Planın en değerli cümlesi. |
| 9 | "120. gün: ilk tam süreli Academic deneme. Beklenti 5.0–5.5" | ✅ İyi bir kontrol noktası. 🟡 İlk tam deneme için 120. gün geç; ~90. günde bir tanı denemesi yapın. |
| 10 | "[gün numarası eksik]: deneme sonucunuz 5.5–6.0'ın altındaysa sınavı 2–3 ay kaydırın" | 🟡 Gün numarası eksik (büyük olasılıkla 150). Eşik gevşek: §1.4'teki hızlarla 150. günde 5.5 olan biri 180. günde büyük olasılıkla ~6.0'da olur. **Öneri:** 150. günde iki tam denemenin ortalaması ≥6.0 **ve** Writing ≥5.5 değilse kaydırın. |
| 11 | "170–180. gün: iki denemede 6.5 (gerekiyorsa her bölümde en az 6.0) görmeden sınava girmeyin" | ✅ Çok yerinde. 🟡 Ama Writing/Speaking denemeleri **insan** tarafından puanlanmalı; YZ tahmini bu kural için yeterli değil. Hedef kurumun bölüm bazlı asgari puanını da kontrol edin. |
| 12 | "Ön Koşul (Opsiyonel): English Online — Sınır Koşulu: yalnızca temel dil altyapısında majör eksiklik varsa ()" | ❌ Ana Plan'la çelişiyor; "()" içindeki ölçüt kaybolmuş. "Majör eksikliği" sayısal tanımlayın (ör. 120. gün denemesinde herhangi bir bölüm <5.0). |
| 13 | "Faz 1: Cambridge Test & Train (Ana Temel) — otantik veri üzerinde zaman kısıtı olmaksızın soru-cevap nedensellik ağının haritalanması, hata payının sıfıra yaklaştırılması" | ✅ Ürün var: *IELTS Test & Train Academic* — ücretli (~24,50 ABD doları, 18 ay erişim, 3 tam deneme + Speaking/Writing desteği + iki deneme değerinde Reading/Listening etkinliği, B1–C1); ücretsiz *Mini* sürümü Nisan 2025'te çıktı ([Cambridge shop](https://shop.cambridge.org/english/family/test-&-train)). 🟡 "Otantik veri" için asıl kaynak, gerçek sınav kâğıtlarından oluşan *Cambridge IELTS 1–20* serisidir (*IELTS 20 Academic* 2025, 4 deneme — [Cambridge shop](https://shop.cambridge.org/english/product/2700250101)). "Nedensellik ağı" = her doğru/yanlış cevabın metindeki kanıtını bulmak; bunu bir **hata günlüğüyle** yapın ✅. "Hata payını sıfıra yaklaştırmak" gerçekçi bir ölçüt değil. |
| 14 | "Faz 2: IELTS Ready Premium — resmî arayüzde 164 dakikalık stres testi" | ✅ British Council Türkiye üzerinden sınava kaydolanlara **ücretsiz** erişim veriliyor (40 deneme, dört beceri) ([British Council Türkiye](https://britishcouncil.org.tr/en/exam/ielts/why-choose/benefits)); erişim kayıttan sonra Test Taker Portal'dan açılıyor (bazı ülkelerde sınavdan 7 gün sonrasına kadar). **Pratik sonuç:** Sınava British Council üzerinden ve **erken** (ör. ~120–130. günde) kaydolun ki son fazda bu denemeleri kullanabilesiniz. ✅ "164 dk", toplam sınav süresine (~2 sa 45 dk) yakın; ama Speaking aynı gün ya da 7 gün önce/sonra yapılabilir ([British Council Türkiye — format](https://britishcouncil.org.tr/en/exam/ielts/format)). |
| 15 | "Faz 3: IELTS Progress Check — sınava 10 gün kala, Writing/Speaking sapmasını insan faktörüyle ölçerek varyansı sabitlemek" | ✅ Ürün var; Writing ve Speaking IELTS uzmanlarınca puanlanıyor, Speaking kayıtlı bir sınav görevlisi sesiyle yapılıyor, rapor ~5 (iş) günü içinde geliyor ([IDP Türkiye](https://ielts.idp.com/turkey/prepare/article-prepare-for-ielts-with-ielts-progress-check/en-gb)). ❌ "10 gün kala" çok geç: Sonuç ~5 gün sonra gelirse geri bildirime göre çalışacak ~5 gününüz kalır. **Öneri:** ~145–150. günde bir kez (karar kuralı için), gerekirse ~160–165. günde ikinci kez. |

---

## 6. Kaynak doğrulama tablosu

| Kaynak | Durum (Ekim 2026) | Not |
|---|---|---|
| Anki (FSRS) | ✅ | Ayarlar: §4.4 |
| Paul Nation BNC/COCA listeleri | ✅ | 25 sıklık listesi + özel adlar vb.; bant içi alfabetik → karıştırın |
| Oxford 3000/5000 | ✅ (öneri) | CEFR etiketli |
| Akademik Kelime Listesi (AWL) | ✅ (öneri) | 570 aile; akademik metinlerdeki kelimelerin ~%10'u ([Victoria University](https://www.wgtn.ac.nz/lals/resources/academicwordlist/information/thesublists)) |
| Cambridge Empower 2. baskı | ✅ | A1–C1, Ocak 2022; plan A1'i atlıyor |
| Essential / English Grammar in Use | ✅ | 4. / 5. baskı güncel |
| Advanced Grammar in Use | ✅ var, 🟡 hedef dışı | C1–C2 düzeyi |
| Busuu Premium Plus | ✅ | Üçüncü taraf fiyat sayfalarında 2026'da listeleniyor; günde 3 saat fazla |
| British Council English Online (Platinum) | ✅ | Haftada 3 canlı grup dersi + webinar; "B2.2" ❓ |
| ELSA Speak / Speech Analyzer | ✅ | IELTS tahmini temkinle; spektrogram ❓ |
| English Accent Coach | ✅ | Ücretsiz web oyunları |
| Forvo, YouGlish | ✅ | Bilinen kaynaklar; 2026 durumu bu çalışmada ayrıca doğrulanmadı |
| English e-Reader | ✅ | Bilinen kaynak; ayrıca doğrulanmadı |
| Extensive Reading Central | ✅ | 20 düzeylik ölçek; metinler ~8.000 headword'e kadar (planın ifadesi pratikte doğru) |
| FreeGradedReaders.com | ✅ | ER Foundation ve Victoria University listelerinde ([ERF](https://erfoundation.org/wordpress/?p=3361)) |
| Oqou | ❓ | Bulunamadı |
| ESL Bits | ✅ | Bilinen kaynak; ayrıca doğrulanmadı |
| Oxford Bookworms / Pearson / Cambridge Readers | ✅ | |
| Mid-frequency Readers (Meister & Nation) | ✅ (öneri) | 4k/6k/8k düzeyleri, ücretsiz |
| LinguaWire | ✅ | A1 ve A2 haber podcast'leri; YZ destekli üretim ([Podnews](https://podnews.net/podcast/i11a8x)) |
| Coffee Break English | ✅ | Bilinen kaynak; ayrıca doğrulanmadı |
| BBC — The English We Speak | ✅ | Eylül 2026'da haftalık yayında (podcast dizinleri) |
| Luke's English Podcast / All Ears English | ✅ | Bilinen kaynaklar; ayrıca doğrulanmadı |
| VOA Learning English | 🟡 | 2025 kesintisi; 2026'da kısmi içerik |
| ChatGPT Voice | ✅ | Hoşgörülü muhatap; puanlama için güvenilir değil |
| Write & Improve | ✅ | Ücretsiz, CEFR tahmini; IELTS görevleri ücretli |
| Tandem / Meetup | ✅ | |
| Nation — Speed reading & listening fluency | ✅ | Ücretsiz |
| Cambridge IELTS Test & Train (Academic) | ✅ | Ücretli; Mini sürüm ücretsiz |
| Cambridge IELTS 20 Academic | ✅ (öneri) | 2025, 4 otantik deneme |
| IELTS Ready Premium | ✅ | British Council Türkiye kaydıyla ücretsiz, 40 deneme |
| IELTS Progress Check | ✅ | W/S uzman puanlı; ~5 (iş) günü |
| Praat | ✅ (öneri) | Ücretsiz perde (tonlama) eğrisi |

---

## 7. Planda eksik olanlar

1. **Başlangıç ve ara ölçümler.** İlerlemeyi ölçecek basit bir panel yok. Öneri: Nation'ın sitesindeki kelime düzeyi testleri ([Paul Nation's resources](https://wgtn.ac.nz/lals/resources/paul-nations-resources)), Write & Improve'un CEFR tahmini, 90/120/150/165. günlerde tam IELTS denemeleri.
2. **İnsan geri bildirimi.** IELTS Writing ve Speaking'i insan değerlendirir; planda düzenli insan geri bildirimi yalnızca Busuu topluluğundan ve (çelişkili biçimde) English Online'dan geliyor. Faz C'den itibaren haftada 2 seans IELTS deneyimli eğitmen ve 1–2 Progress Check ekleyin.
3. **Akademik kelime.** AWL (570 aile) B1'den itibaren Anki'ye alınmalı.
4. **IELTS görev okuryazarlığı.** Task 1 betimleme dili (eğilim, karşılaştırma, süreç), Task 2 deneme türleri, okuma soru tipleri, dinlemede form doldurma ve yazım, farklı aksanlar (İngiliz, Avustralya, Kuzey Amerika…).
5. **Sınav türü kararı.** Bilgisayarda IELTS seçerseniz Türkiye'de *One Skill Retake* (60 gün içinde tek bölümü yeniden alma) mümkün; Ankara, İstanbul, İzmir ve Erzurum'da bilgisayarlı sınav var ([British Council Türkiye](https://www.britishcouncil.org.tr/en/exam/ielts/dates-fees-locations/ways-to-take-your-IELTS-test)). Kurumunuzun One Skill Retake'i kabul edip etmediğini kontrol edin. Seçime göre klavyede ya da elle yazma pratiği yapın.
6. **Dinlenme ve uyku.** Haftada bir hafif gün; düzenli uyku (öğrenilenlerin pekişmesi için önemli).
7. **Düşük yoğunluklu girdi.** 8 saati sürdürülebilir kılacak keyifli ama İngilizce içerik (İngilizce altyazılı dizi/YouTube, kolay podcast).
8. **Hata günlüğü (error log).** Yazma, konuşma, okuma ve dinleme hataları için tek tablo; her hafta en sık 3 hata türüne bir Murphy ünitesi atanır.
9. **Kurumsal gereklilik.** Başvuracağınız kurumların genel ve bölüm bazlı asgari puanları; sonuçların geçerlilik süresi (genellikle 2 yıl).

---

## 8. Önerilen revizyon (planı bozmadan)

**Güncel ve tek başına yeterli sürüm:** [Nihai Plan](nihai_dort_bilesen_plani.md) (telaffuz, girdi, çıktı, akıcılık; 6 temel kaynak; derin araştırmayla güncellendi). Önceki sürüm: [En Az Kaynakla Dört Bileşen Planı](en_az_kaynakla_dort_bilesen_plani.md). Okuma, dinleme, yazma ve konuşma bloklarının seviye seviye ayrıntılı hali ayrı belgelerde: [8 basamaklı uygulama planı](girdi_cikti_uygulama_plani.md) ve araştırma gerekçeleri için [Anlam Odaklı Girdi ve Çıktı Planı](anlam_odakli_girdi_cikti_plani.md).

### 8.1 İlkeler

1. **Zaman bütçesi gerçek olsun:** Her bloğa içindeki işlerin gerçek süresi yazılsın; 8 saat = 6–6,5 saat yoğun + 1,5–2 saat hafif.
2. **Denge:** LFL ilk ay ~%35–40, sonra %25–30; MFI %30–35; MFO %20–25; FD %10–15 (+ çok kolay okuma/dinleme).
3. **Anki:** 25 yeni kart/gün (≈35–40 dk); karıştırılmış BNC/COCA (işlev sözcükleri hariç) → 3.000'den sonra AWL + okumadan toplanan kelimeler; yavaş ama doğru = Hard.
4. **Empower:** 2–3 günde bir ünite; A1 Starter'ı (veya Essential Grammar in Use'un ilk ünitelerini) ilk 3 haftada hızla geçin.
5. **Okuma hacmi:** günde 45–60 dk; haftalık okunan kelime sayısını takip edin.
6. **IELTS:** 90. günden itibaren hafif, 136. günden itibaren yoğun.
7. **İnsan geri bildirimi:** Faz B'den itibaren canlı ders; Faz C–D'de haftada 2 eğitmen seansı + Progress Check.
8. **Telaffuz:** anlaşılırlık önceliği ve Türkçeye özgü öncelik listesi (§4.9).

### 8.2 Faz takvimi

| Faz | Günler | Çıkış hedefi | Odak |
|---|---|---|---|
| A — Temel | 1–30 | A2'ye giriş | Ses-yazım, temel gramer (Empower A1→A2 / Essential GIU), 25 kart/gün, kolay graded reader + okurken dinleme, kısa yazma/konuşma |
| B — Yapı | 31–90 | B1 | Empower A2→B1, okuma 45–60 dk, 4/3/2 başlar, canlı dersler (English Online), haftada 3–4 yazı |
| C — Genişleme | 91–135 | B1+/B2 | Empower B1+→B2, AWL, Mid-frequency Readers, IELTS formatlarına giriş (haftada 2 Task 2 + 1–2 Task 1, okuma soru tipleri), eğitmenle Speaking |
| D — IELTS Academic | 136–180 | 6.0–6.5 | Haftada 2 tam deneme + analiz, günlük Writing, Speaking denemeleri, hata günlüğü, Progress Check |

### 8.3 Günlük şablon (dakika)

| Bileşen | Faz A | Faz B | Faz C | Faz D |
|---|---|---|---|---|
| **LFL** — Anki (tekrar + yeni) | 35 | 40 | 40 | 30 |
| LFL — kart üretimi | 20 | 20 | 15 | 10 |
| LFL — ders kitabı + gramer | 70 | 60 | 45 | 20 (hata günlüğüne göre) |
| LFL — sesletim (HVPT/ELSA) | 25 | 20 | 15 | 10 |
| **MFI** — yaygın okuma | 45 | 60 | 60 | 45 (Academic Reading dahil) |
| MFI — dinleme / okurken dinleme | 45 | 45 | 45 | 30 (IELTS Listening dahil) |
| **MFO** — yazma | 20 | 30 | 45 | 60 (Task 1 + Task 2) |
| MFO — konuşma (YZ, monolog + transkript, canlı ders) | 25 | 40 | 45 | 45 (Speaking Part 1–3) |
| **FD** — 4/3/2, tekrarlı/hızlı okuma, süreli yazma | 20 | 30 | 30 | 25 |
| IELTS bölüm/tam deneme + analiz | — | — | 30 | 60–90 (ortalama) |
| **Yoğun toplam** | ≈ 305 dk (5,1 sa) | ≈ 345 dk (5,75 sa) | ≈ 370 dk (6,2 sa) | ≈ 335–365 dk (5,6–6,1 sa) |
| Düşük yoğunluklu girdi (dizi, YouTube, podcast) | 60–90 | 60–90 | 60–90 | 45–60 |
| **Genel toplam** | ≈ 6,1–6,6 sa | ≈ 6,75–7,25 sa | ≈ 7,2–7,7 sa | ≈ 6,3–7,1 sa |
| LFL payı (hafif girdi dahil) | ~%40 | ~%33 | ~%26 | ~%18 |

- 8 saate tamamlamak isterseniz fazlayı yalnızca **düşük yoğunluklu girdiye** (ve Faz B–C'de canlı derslere) ekleyin; yoğun bloğu büyütmeyin.
- English Online canlı dersleri, ders olan günlerde "konuşma" bloğunun yerine geçer. Busuu kullanacaksanız Faz A'da "ders kitabı + gramer" bloğunun 20–30 dakikası olarak (ya da yolda) kullanın.
- **Pazar:** hafif gün — haftalık Anki, 4/3/2, gölgeleme, haftalık değerlendirme (≤3 saat). Faz D'de Pazar tam deneme günü olacaksa haftanın başka bir günü hafif olsun.

### 8.4 Faz D için örnek hafta

| Gün | İçerik |
|---|---|
| Pazartesi | Tam deneme (Listening + Reading + Writing) + analiz |
| Salı | Writing: 1 Task 2 + 1 Task 1 (süreli) + geri bildirimle yeniden yazma; Speaking Part 2–3 |
| Çarşamba | Reading: 2 pasaj (süreli) + hata günlüğü; Listening: 2 bölüm; eğitmen seansı |
| Perşembe | Tam deneme (L + R + W) + Speaking denemesi |
| Cuma | Writing × 2 + eğitmen seansı; zayıf soru tipine odak |
| Cumartesi | Telafi + IELTS metinlerinden toplanan kelimeler + 4/3/2 |
| Pazar | Hafif gün |

### 8.5 Gün sıkışınca kesme sırası (önerilen)

- **Önce kesilecekler:** Busuu → ek Murphy alıştırmaları → ELSA'nın ileri modülleri → Anki **yeni** kart sayısı (tekrarlar asla) → ders kitabı hızı.
- **Asla kesilmeyecekler:** Anki tekrarları, yaygın okuma/dinleme hacmi, Faz C–D'de geri bildirimli Writing, Faz D'de tam denemeler.

### 8.6 Revize karar kuralları

| Gün | Ölçüm | Karar |
|---|---|---|
| 30 | A1–A2 graded reader'ı ≥%98 kapsamayla rahat okuyabiliyor musunuz? Anki gerçek hatırlama oranı ≥%85 mi? | Hayırsa: yeni kartı 20'ye indirin, okuma seviyesini düşürün |
| 60 | Nation'ın kelime düzeyi testi (1.000–2.000 düzeyi); Write & Improve tahmini (A2+/B1) | B1'e yaklaşılmıyorsa: ders kitabı temposunu yavaşlatın, okumayı artırın |
| 90 | İlk tam IELTS Academic denemesi (W/S bir eğitmence puanlanır) | Beklenti ~4.5–5.0; tanı amaçlı |
| 120 | Tam deneme (planınızdaki gibi) | <5.0 ise sınav hedefini şimdiden ~3 ay ileri alın |
| 120–130 | Sınava British Council üzerinden kaydolun (IELTS Ready Premium erişimi için) | Kayıttan önce erteleme/iptal kurallarını okuyun |
| 145–150 | İki tam deneme + 1 Progress Check | Ortalama <6.0 ya da Writing <5.5 ise 2–3 ay kaydırın |
| 165–175 | İki deneme ≥6.5 (W/S insan puanlı) + kurumun bölüm bazlı asgari puanları | Sağlanmıyorsa kaydırın |

### 8.7 Takip paneli

| Gösterge | Hedef |
|---|---|
| Anki gerçek hatırlama oranı (true retention) | %85–92 |
| Anki günlük süresi | ≤45 dk |
| Haftalık okunan kelime | Faz A 15–25 bin → Faz C 50 bin+ (180 günde toplam ~1,2 milyon) |
| Okuma hızı (kolay metin, iyi anlama) | 90. gün ~150, 150. gün ~200+ kelime/dk |
| Haftalık dinleme | ≥10 saat (hafif girdi dahil) |
| Geri bildirimli yazı | Faz C: 3/hafta · Faz D: 5–6/hafta |
| Kayıtlı konuşma | ≥30 dk/hafta + transkript |
| Deneme puanları | Bölüm bazında grafik; okuma ham puanı 27+ (≈6.5), 30+ (≈7.0); dinleme 26+ (≈6.5), 30+ (≈7.0) |

---

## 9. Kaynakça

**Seviye, süre, IELTS**
- Cambridge English — [Guided learning hours](https://support.cambridgeenglish.org/hc/en-gb/articles/202838506-Guided-learning-hours)
- IELTS — [IELTS and the CEFR](https://ielts.org/organisations/ielts-for-organisations/compare-ielts/ielts-and-the-cefr)
- IELTS — [Test statistics](https://ielts.org/researchers/our-research/test-statistics)
- IDP — [Band score calculation](https://ielts.idp.com/canada/results/band-score-calculation)
- IELTS Australia — [Writing scores (Task 2 ağırlığı)](https://ielts.com.au/australia/results/scores/writing)
- IELTS — [Speaking band descriptors](https://ielts.org/cdn/ielts-downloadable-assets/ielts-guidance-and-support/ielts-guides/ielts-speaking-band-descriptors.pdf)
- IDP — [Accents and IELTS Speaking scores](https://ielts.idp.com/uae/prepare/article-accents-ielts-speaking-scores/en-gb)
- British Council Türkiye — [IELTS format](https://britishcouncil.org.tr/en/exam/ielts/format) · [Ways to take IELTS / One Skill Retake](https://www.britishcouncil.org.tr/en/exam/ielts/dates-fees-locations/ways-to-take-your-IELTS-test) · [Benefits / IELTS Ready Premium](https://britishcouncil.org.tr/en/exam/ielts/why-choose/benefits)
- IDP Türkiye — [IELTS Progress Check](https://ielts.idp.com/turkey/prepare/article-prepare-for-ielts-with-ielts-progress-check/en-gb)
- Cambridge — [Test & Train](https://shop.cambridge.org/english/family/test-&-train) · [Cambridge IELTS 20 Academic](https://shop.cambridge.org/english/product/2700250101)
- Elder & O'Loughlin (2003) — [Intensive English study and band score gain](https://ielts.org/researchers/our-research/research-reports/investigating-the-relationship-between-intensive-english-language-study-and-band-score-gain-on-ielts)
- Kang vd. (2021) — [Learner background, linguistic progression and score gain](https://ielts.org/researchers/our-research/research-reports/investigation-of-relationships-between-learner-background-linguistic-progression-and-score-gain-on-ielts)
- IELTS (2023) — [How long will it take to get the IELTS band score I need?](https://ielts.org/news-and-insights/how-long-will-it-take-to-get-the-ielts-band-score-i-need)
- FSI dil zorluğu sıralaması (ikincil) — [Wikibooks](https://en.wikibooks.org/wiki/Wikibooks:Language_Learning_Difficulty_for_English_Speakers)
- ODTÜ — [Department of Basic English](https://dbe.metu.edu.tr/gen_en.htm) · [Equivalence table](https://oidb.metu.edu.tr/en/equivalence-table-english-language-exams-recognized-metu-undergraduate-and-graduate-students)
- Türk adayların puan profili (ikincil) — [GeeksforGeeks](https://www.geeksforgeeks.org/ielts/average-ielts-score/) · [ieltsmentor](https://www.ieltsmentor.ai/guides/ielts-test-taker-statistics-2024-2025/)

**Öğrenme bilimi ve Nation**
- Nation — [Four Strands, Cambridge örnek bölümü](https://assets.cambridge.org/97810090/98359/excerpt/9781009098359_excerpt.pdf)
- Nation (2014) — [How much input do you need to learn the most frequent 9,000 words?](https://nflrc.hawaii.edu/rfl/item-detail/303)
- Nation — [Vocabulary, the CEFR levels and word family size](https://wgtn.ac.nz/lals/resources/paul-nations-resources/vocabulary-lists/vocabulary-cefr-and-word-family-size/vocabulary-and-the-cefr-docx)
- Nation — [Word parts and language learning](https://jalt-publications.org/articles/28460-expositions-word-parts-and-language-learning)
- Nation & Millett — [Speed reading and listening fluency](https://www.wgtn.ac.nz/lals/resources/paul-nations-resources/speed-reading-and-listening-fluency) · [Free graded / mid-frequency readers](https://www.wgtn.ac.nz/lals/resources/readers)
- [Information on the BNC/COCA word family lists](https://vuw-web.matrix.squiz.cloud/__data/assets/pdf_file/0004/1689349/Information-on-the-BNC_COCA-word-family-lists-20180705.pdf) · [bant içi alfabetik sıra (ikincil)](https://bunkyo.repo.nii.ac.jp/record/7521/files/BKK0003688.pdf)
- [Oxford 3000/5000](https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000) · [Academic Word List](https://www.wgtn.ac.nz/lals/resources/academicwordlist/information/thesublists)
- IELTS okuma kapsaması — [SAGE Open 2025](https://journals.sagepub.com/doi/xml/10.1177/21582440251362269) · IELTS dinleme kapsaması — [SAGE Open 2022](https://journals.sagepub.com/doi/xml/10.1177/21582440221079934)
- Hu & Nation (2000) ve replikasyonu — [AILA özeti](https://aila2021.dryfta.com/program/abstract-archive/abstract/public/416/unknown-vocabulary-density-reading-comprehension-and-the-98-coverage-figure-replicating-hu-nation-2000)
- Webb — [Receptive and productive vocabulary learning (tez)](https://ir.wgtn.ac.nz/handle/123456789/23701)
- Kim & Webb (2022) — The effects of spaced practice on second language learning: A meta-analysis. *Language Learning*, 72(1), 269–319.
- Erten & Tekin (2008) — [Semantic sets vs unrelated sets](https://avesis.comu.edu.tr/yayin/4a84e8a3-294d-457c-9e11-65cbf94493a0/effects-on-vocabulary-acquisition-of-presenting-new-words-in-semantic-sets-versus-semantically-unrelated-sets)
- Brown, Waring & Donkaewbua (2008) — [Incidental vocabulary acquisition from reading, reading-while-listening and listening](https://www2.hawaii.edu/~readfl/rfl/October2008/brown/brown.html)
- Ericsson, Krampe & Tesch-Römer (1993), *Psychological Review* 100(3), 363–406 — [alıntı](https://acesounderglass.com/2019/06/21/epistemic-spot-check-the-role-of-deliberate-practice-in-the-acquisition-of-expert-performance/)
- Anki — [Manual: Studying](https://docs.ankiweb.net/studying.html) · [Forum: button usage](https://forums.ankiweb.net/t/an-info-tip-regarding-recommended-button-usage/39834)
- Brysbaert (2019) okuma hızı — [BPS Research Digest](https://www.bps.org.uk/research-digest/most-comprehensive-review-date-finds-average-persons-reading-speed-slower)
- Rayner vd. (2016) — [Speed reading promises are too good to be true (APS)](https://www.psychologicalscience.org/news/releases/speed-reading-promises-are-too-good-to-be-true-scientists-find.html)
- Nation — [Reading for Speed and Fluency incelemesi](https://jalt-publications.org/tlt/departments/book-reviews/articles/514-reading-speed-and-fluency-1)
- De Jong & Perfetti (2011) — [Fluency training in the ESL classroom](https://www.lrdc.pitt.edu/perfettilab/pubpdfs/de%20Jong%20Language%20Learning.pdf)
- Lynch (2001, 2007), *ELT Journal* · kendi konuşmasını yazıya dökme üzerine — [Colombian Applied Linguistics Journal](https://revistas.udistrital.edu.co/index.php/calj/article/view/4989)
- Shadowing — [Lambert 1992, *Meta*](https://assets.erudit.tech/en/revue/meta/1992/v37/n2/003378ar.pdf) · [NJLTL derlemesi](https://journal.uia.no/index.php/NJLTL/article/view/1139) · [Arguelles hakkında](https://www.connexionfrance.com/news/american-who-speaks-50-languages-gives-his-tips-on-learning-french/655715)
- Fosilleşme — [Han (2004) incelemesi](https://linguistlist.org/issues/15/2198/)

**Sesletim**
- Munro & Derwing ve Levis — [The Evolution of Pronunciation Teaching and Research](https://www.benjamins.com/catalog/bct.121)
- CEFR Companion Volume — [Phonological control scale](https://rm.coe.int/the-new-scale-for-phonological-control-piccardo-/1680788b29)
- İşlevsel yük — [Frontiers mini review](https://frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.627378/full)
- Ritim sınıfları — [Arvaniti](https://kar.kent.ac.uk/45775/)
- HVPT — [Thomson 2018](https://www.benjamins.com/catalog/persons/957094395) · English Accent Coach — [Brock University](https://brocku.ca/brock-news/2012/02/app-and-website-help-non-english-speakers-learn-the-accent/)
- RP ses birimleri — [Open Book Publishers](https://books.openbookpublishers.com/10.11647/obp.0053/ch2.xhtml)
- Türkçe konuşanlar — [Ülkersoy vd. 2021 (ünlü ekleme)](https://doaj.org/article/9c649dd6324c4d44a1cd6cf24c08b92c) · [Öğretmen adaylarının sorunlu sesleri](https://avesis.akdeniz.edu.tr/yayin/aeacbeb5-6675-4f5a-be6a-81d85fe35b94/pre-service-english-language-teachers-problematic-sounds) · [Hata analizi (Educational Process 2017)](https://doaj.org/article/d6c3cb9e5247484b810aef5d80f6c14e)
- ELSA Speech Analyzer — [ISCA SLaTE 2023](https://www.isca-archive.org/slate_2023/anguera23_slate.html)

**Yapay zekâ ile puanlama**
- [Koraishi 2024 (GPT-4, IELTS Task 2)](https://avesis.uludag.edu.tr/yayin/9610a41d-001d-4f22-834e-579fe0ae99dd/the-intersection-of-ai-and-language-assessment-a-study-on-the-reliability-of-chatgpt-in-grading-ielts-writing-task-2) · [GPT-4o çalışması](https://avesis.iuc.edu.tr/yayin/a433340f-6e81-4eb6-ba9f-f334fca4e436/chatgpt-4o-as-an-automated-scoring-tool-for-writing-assessment-strengths-and-weaknesses) · [Çok modelli IELTS karşılaştırması](https://abdn.elsevierpure.com/en/publications/from-prompts-to-scores-generative-ai-versus-human-grading-in-writ)

**Araçlar ve kaynaklar**
- [Cambridge Empower](https://www.cambridge.org/empower) · [British Council English Online](https://englishonline.britishcouncil.org/flexible-english-online-course/) · [Busuu — How it works](https://busuu.com/en/it-works) · [Busuu study](https://www.busuu.com/en/research/university-study) · [Write & Improve](https://writeandimprove.com/)
- [ER-Central levels](https://www.er-central.com/?p=2628) · [ER Foundation — free reading material](https://erfoundation.org/wordpress/?p=3361) · [LinguaWire (Podnews)](https://podnews.net/podcast/i11a8x)
- VOA — [Wikipedia](https://en.wikipedia.org/wiki/Voice_of_America) · [JURIST, Mart 2026](https://www.jurist.org/news/2026/03/us-federal-judge-orders-voice-of-america-broadcasting-restored/) · [VOA Learning English](https://learningenglish.voanews.com/)

---

## Ek A — Anki simülasyonunun varsayımları

- **Araç:** `fsrs` Python paketi 6.3.2 (FSRS-6 varsayılan parametreleri); hedef hatırlama 0,90; öğrenme adımları 1 dk ve 10 dk; yeniden öğrenme adımı 10 dk; aralık bulanıklaştırma açık.
- **Bellek modeli:** Her tekrarın başarı olasılığı, FSRS'nin o andaki hatırlanabilirlik tahmini (ortalama bir öğrenici varsayımı).
- **Yeni kart:** İlk gösterimde hatırlanma olasılığı %65 (kelime önce deftere yazıldığı için).
- **Süreler:** Yeni kartın ilk gösterimi 20 sn, öğrenme adımı 9 sn, tekrar 8 sn (duyarlılık analizi: 12 sn).
- **"5 saniye kuralı":** Doğru cevapların genç kartlarda (kararlılık <10 gün) %15'i, olgun kartlarda %5'i "Again" olarak işaretlenir.
- **Tekrar sayısı:** 3 farklı rastgele tohumun ortalaması; 180 gün.
- **Sınırlar:** Gerçek parametreler kişiden kişiye değişir (FSRS kendi verinize göre optimize olur); sonuçlar mertebe tahminidir; kart üretim süresi dahil değildir.
- **Çalıştırma:** `pip install fsrs` → `python anki_fsrs_simulasyonu.py all`
