<img width="1415" alt="flo" src="https://github.com/melisacevik/FLO-Customer-Segmentation/assets/113050206/186995fe-454b-4e22-94db-14c32b03f8f8">
<img width="1382" alt="Screenshot 2024-02-05 at 22 08 43" src="https://github.com/melisacevik/FLO-Customer-Segmentation/assets/113050206/b9c895da-41cf-492f-b590-69e2bd2d50bf">


# FLO - RFM Analizi ile Müşteri Segmentasyonu

## İş Problemi

FLO, online ayakkabı mağazası olarak müşteri segmentasyonu yaparak, müşteri davranışlarını anlamayı ve pazarlama stratejilerini belirlemeyi hedeflemektedir. Bu çerçevede, RFM analizi kullanılarak müşteriler segmentlere ayrılacak ve her bir segmente özel pazarlama stratejileri geliştirilecektir.

## İlgili Dosyalar

- İndirim ve kampanya müşterileri ilgili departmanın talebine göre özel olarak oluşturulmuştur. İndirim ve tanımlanacak kampanyalar için belirlenen müşteri ID'leri ayrı csv dosyası olarak oluşturulmuştur.

## RFM Analizi Nedir?

RFM analizi, "Recency" (yenilik), "Frequency" (sıklık) ve "Monetary" (parasal değer) kriterlerini kullanarak müşterileri segmentlere ayırmak için kullanılan bir yöntemdir. Bu analiz, müşterilerin geçmiş alışveriş davranışlarına dayanarak, onları belirli özelliklere göre gruplamayı amaçlar.

## Nasıl Kullanılır?

1. **Veri Toplama:**
   - Müşteri verileri ve alışveriş geçmişi toplanmalıdır.

2. **RFM Analizi:**
   - Recency, Frequency ve Monetary kriterleri kullanılarak müşteriler segmentlere ayrılmalıdır.

3. **Segmentlere Göre Stratejiler Belirleme:**
   - Her bir segmente özel pazarlama stratejileri oluşturulmalıdır.

4. **Optimizasyon ve İzleme:**
   - Uygulanan stratejilerin etkisi düzenli olarak izlenmeli ve gerektiğinde optimize edilmelidir.



######## 2. Proje 

# FLO - BG/NBD ve Gamma-Gamma ile CLTV Prediction

## İş Problemi

FLO, online ayakkabı mağazası olarak müşteri segmentasyonu ve müşteri değeri tahmini yapmayı hedeflemektedir. Bu çerçevede, BG/NBD ve Gamma-Gamma modelleri kullanılarak müşteri ömrü değeri (CLTV) tahmin edilecek ve müşteri segmentlerine ayrılacaktır.

## İlgili Dosyalar

- `flo_data_20K.csv`: Müşteri verileri ve alışveriş geçmişi.

## BG/NBD ve Gamma-Gamma ile CLTV Prediction Kodları

Kodlar, BG/NBD ve Gamma-Gamma modelleri kullanılarak müşteri segmentasyonu ve CLTV tahmini işlemlerini içermektedir. İlgili görevler şunlardır:

### GÖREV 1: Veriyi Hazırlama

1. `flo_data_20K.csv` verisini okuma ve kopyalama işlemleri.
2. Aykırı değerlerin baskılanması için gerekli fonksiyonların tanımlanması.
3. Belirli değişkenlerin aykırı değerlerinin baskılanması.
4. Omnichannel müşteriler için yeni değişkenlerin oluşturulması.
5. Tarih ifade eden değişkenlerin tipinin "date" olarak değiştirilmesi.

### GÖREV 2: CLTV Veri Yapısının Oluşturulması

1. Veri setindeki en son alışverişin yapıldığı tarihten 2 gün sonrasının analiz tarihi olarak alınması.
2. `customer_id`, `recency_cltv_weekly`, `T_weekly`, `frequency` ve `monetary_cltv_avg` değerlerinin yer aldığı yeni bir CLTV dataframe'inin oluşturulması.

### GÖREV 3: BG/NBD, Gamma-Gamma Modellerinin Kurulması, CLTV'nin Hesaplanması

1. BG/NBD modelinin kurulması ve 3 ve 6 aylık müşteri satın alma tahminlerinin yapılması.
2. Gamma-Gamma modelinin fit edilmesi ve ortalama bırakacakları değerlerin tahminlenmesi.
3. 6 aylık CLTV'nin hesaplanması.

### GÖREV 4: CLTV'ye Göre Segmentlerin Oluşturulması

1. 6 aylık CLTV'ye göre müşterilerin dört gruba ayrılması ve grup isimlerinin dataframe'e eklenmesi.
2. Segmentlerin recency, frequency ve monetary ortalamalarının incelenmesi.

---

Tüm bu görevler, FLO'nun müşteri segmentasyonu ve CLTV tahmini için kullanılan BG/NBD ve Gamma-Gamma modellerini içermektedir. Detaylı açıklamalar ve görselleştirmeler kodların içerisinde mevcuttur.




