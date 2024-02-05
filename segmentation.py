
###############################################################
# RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)
###############################################################

###############################################################
# İş Problemi (Business Problem)
###############################################################
# FLO müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor.
# Buna yönelik olarak müşterilerin davranışları tanımlanacak ve bu davranış öbeklenmelerine göre gruplar oluşturulacak..

###############################################################
# Veri Seti Hikayesi
###############################################################

# Veri seti son alışverişlerini 2020 - 2021 yıllarında OmniChannel(hem online hem offline alışveriş yapan) olarak yapan müşterilerin geçmiş alışveriş davranışlarından
# elde edilen bilgilerden oluşmaktadır.

# master_id: Eşsiz müşteri numarası
# order_channel : Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile, Offline)
# last_order_channel : En son alışverişin yapıldığı kanal
# first_order_date : Müşterinin yaptığı ilk alışveriş tarihi
# last_order_date : Müşterinin yaptığı son alışveriş tarihi
# last_order_date_online : Muşterinin online platformda yaptığı son alışveriş tarihi
# last_order_date_offline : Muşterinin offline platformda yaptığı son alışveriş tarihi
# order_num_total_ever_online : Müşterinin online platformda yaptığı toplam alışveriş sayısı
# order_num_total_ever_offline : Müşterinin offline'da yaptığı toplam alışveriş sayısı
# customer_value_total_ever_offline : Müşterinin offline alışverişlerinde ödediği toplam ücret
# customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
# interested_in_categories_12 : Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi

###############################################################
# GÖREVLER
###############################################################

# GÖREV 1: Veriyi Anlama (Data Understanding) ve Hazırlama
           # 1. flo_data_20K.csv verisini okuyunuz.
           # 2. Veri setinde
                     # a. İlk 10 gözlem,
                     # b. Değişken isimleri,
                     # c. Betimsel istatistik,
                     # d. Boş değer,
                     # e. Değişken tipleri, incelemesi yapınız.
           # 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir.
           # Her bir müşterinin toplam
           # alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.
           # 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
           # 5. Alışveriş kanallarındaki müşteri sayısının, ortalama alınan ürün sayısının ve ortalama harcamaların dağılımına bakınız.
           # 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.
           # 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.
           # 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.

# GÖREV 2: RFM Metriklerinin Hesaplanması

# GÖREV 3: RF ve RFM Skorlarının Hesaplanması

# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması

# GÖREV 5: Aksiyon zamanı!
           # 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.
           # 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulun ve müşteri id'lerini csv ye kaydediniz.
                   # a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
                   # tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Sadık müşterilerinden(champions,loyal_customers),
                   # ortalama 250 TL üzeri ve kadın kategorisinden alışveriş yapan kişiler özel olarak iletişim kuralacak müşteriler. Bu müşterilerin id numaralarını csv dosyasına
                   # yeni_marka_hedef_müşteri_id.cvs olarak kaydediniz.
                   # b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşteri olan ama uzun süredir
                   # alışveriş yapmayan kaybedilmemesi gereken müşteriler, uykuda olanlar ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
                   # olarak kaydediniz.


# GÖREV 6: Tüm süreci fonksiyonlaştırınız.

###############################################################
# GÖREV 1: Veriyi  Hazırlama ve Anlama (Data Understanding)
###############################################################

import datetime as dt
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

df_ = pd.read_csv("flo_data_20k.csv")
df = df_.copy()

# 2. Veri setinde
        # a. İlk 10 gözlem,
df.head(10)
        # b. Değişken isimleri,
df.columns
        # c. Boyut,
df.shape
        # d. Betimsel istatistik,
df.describe().T

        # e. Boş değer,
df.isnull().sum()

        # f. Değişken tipleri, incelemesi yapınız.
for col in df.columns:
    print("Data type of " + str(col) + " => "+ str(df[col].dtype))


# 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir.
# Herbir müşterinin toplam alışveriş sayısı ve harcaması için yeni değişkenler oluşturunuz.

df["order_num_total_ever_offonline"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
df["value_total_ever_offonline"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]

df.columns

# 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.

new_date_columns = ["first_order_date", "last_order_date","last_order_date_online", "last_order_date_offline"]

for column in new_date_columns:
    df[column] = pd.to_datetime(df[column], format="%Y-%m-%d")

df["first_order_date"].dtype
df.dtypes

# df["last_order_date"] = df["last_order_date"].apply(pd.to_datetime)


# 5. Alışveriş kanallarındaki müşteri sayısının, toplam alınan ürün sayısı ve toplam harcamaların dağılımına bakınız.

result = df.groupby("order_channel").agg({"master_id" : "count",
                                 "order_num_total_ever_offonline" : "mean",
                                 "value_total_ever_offonline" : "mean"}).describe().T

print(result)

# 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.

df.sort_values(by="value_total_ever_offonline", ascending=False).head(10)

# 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.

df.sort_values(by="order_num_total_ever_offonline", ascending=False ).head(10)

# 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.

def create_preparation(dataframe):

    # ön hazırlık
    print(dataframe.head(2))
    print("######")
    print(df.columns)
    print("######")
    print(df.shape)
    print("######")
    print(df.describe().T)
    print("######")
    print(df.isnull().sum())

    ###############

    for col in dataframe.columns:
        print("Data type of " + str(col) + " => " + str(dataframe[col].dtype))

    for col in dataframe.columns:
        print("Data type of " + str(col) + " => " + str(dataframe[col].dtype))

    # toplam alışveriş sayısı / toplam harcama değişkeni oluşturma

    df["order_num_total_ever_offonline"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
    df["value_total_ever_offonline"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]

    print( "Order Num Total Ever Offline and Online" , df["order_num_total_ever_offonline"])
    print( "Value Total Ever Offline and Online" , df["value_total_ever_offonline"])

    # Tarih ifade eden değişkenlerin tipini date'e çevirme

    new_date_columns = ["first_order_date", "last_order_date", "last_order_date_online", "last_order_date_offline"]

    for column in new_date_columns:
        dataframe[column] = pd.to_datetime(dataframe[column], format="%Y-%m-%d")
        print("Data structure which converted to date" , dataframe[column])

    # Kanallardaki müşteri sayısının, toplam alınan ürün sayısı ve toplam harcamaların dağılımına bakma

    result = dataframe.groupby("order_channel").agg({"master_id": "count",
                                              "order_num_total_ever_offonline": "mean",
                                              "value_total_ever_offonline": "mean"}).describe().T

    print("Müşteri sayısı, toplam ürün sayısı, toplam harcama dağılımı" , result)

    # En fazla kazancı getiren ve siparişi veren ilk 10 müşteriyi sıralayınız.
    print(df.sort_values(by="value_total_ever_offonline", ascending=False).head(10))
    print(df.sort_values(by="order_num_total_ever_offonline", ascending=False).head(10))

    return dataframe

df_new = create_preparation(df)

###############################################################
# GÖREV 2: RFM Metriklerinin Hesaplanması
###############################################################

# Veri setindeki en son alışverişin yapıldığı tarihten 2 gün sonrasını analiz tarihi

today_date = dt.datetime(2021, 6, 1)

# customer_id, recency, frequnecy ve monetary değerlerinin yer aldığı yeni bir rfm dataframe

pd.set_option('display.width', 500)

rfm = df.groupby("master_id").agg({
    'last_order_date': lambda x: (today_date - x.max()).days,  # Recency
    'order_num_total_ever_offonline': 'mean',  # Frequency
    'value_total_ever_offonline': 'sum'  # Monetary
    }).reset_index()

rfm.columns = ['master_id', 'recency', 'frequency', 'monetary']

rfm.describe().T
df.head()
###############################################################
# GÖREV 3: RF ve RFM Skorlarının Hesaplanması (Calculating RF and RFM Scores)
###############################################################

#  Recency, Frequency ve Monetary metriklerini qcut yardımı ile 1-5 arasında skorlara çevrilmesi ve
# Bu skorları recency_score, frequency_score ve monetary_score olarak kaydedilmesi

rfm["recency_score"] = pd.qcut(rfm["recency"], q=5, labels=[5,4,3,2,1])
rfm["monetary_score"] = pd.qcut(rfm["monetary"], q=5, labels=[5,4,3,2,1])
rfm["frequency_score"] = pd.qcut(rfm['frequency'].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]) #oluşturulan aralıklarda unique değerler yer almadığı için error veriyor ( rank() )

# recency_score ve frequency_score’u tek bir değişken olarak ifade edilmesi ve RF_SCORE olarak kaydedilmesi
rfm["RF_SCORE"] = rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(str)

###############################################################
# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması
###############################################################

# Oluşturulan RFM skorların daha açıklanabilir olması için segment tanımlama ve  tanımlanan seg_map yardımı ile RF_SCORE'u segmentlere çevirme
seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}

rfm["segment"] = rfm["RF_SCORE"].replace(seg_map, regex=True)

###############################################################
# GÖREV 5: Aksiyon zamanı!
###############################################################

# 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.

rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean", "count"])

# 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulunuz ve müşteri id'lerini csv ye kaydediniz.

# "cant_loose" segmentindeki müşterilerin ID'leri
cant_loose_df = rfm.loc[rfm["segment"] == "cant_loose", ["master_id"]]
cant_loose_df["segment"] = "cant_loose"

# "champions" segmentindeki müşterilerin ID'leri
champions_df = rfm.loc[rfm["segment"] == "champions", ["master_id"]]
champions_df["segment"] = "champions"

new_df = pd.concat([cant_loose_df, champions_df])

new_df.to_csv("champions_cantloose.csv", index=False)

#"champions" ve "cant loose" segmentine ait "master_id" değerlerini içeren bir Series


# a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
# tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Bu müşterilerin sadık  ve
# kadın kategorisinden alışveriş yapan kişiler olması planlandı. Müşterilerin id numaralarını csv dosyasına yeni_marka_hedef_müşteri_id.cvs
# olarak kaydediniz.

df.head()
loyal_and_female_shop = rfm.loc[(rfm["segment"] == 'loyal_customers') & df["interested_in_categories_12"].str.contains("KADIN"), "master_id"]

loyal_and_female_shop.to_csv("yeni_marka_hedef_musteri_id")

# b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşterilerden olan ama uzun süredir
# alışveriş yapmayan ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
# olarak kaydediniz.

indirim_hedef_musteri_ids = rfm.loc[
    ((rfm["segment"] == 'about_to_sleep') | (rfm["segment"] == 'new_customers')) &
    df["interested_in_categories_12"].str.contains("ERKEK|COCUK", case=False),
    "master_id"
]

indirim_hedef_musteri_ids.to_csv("indirim_hedef_musteri_ids.csv", index=False)

