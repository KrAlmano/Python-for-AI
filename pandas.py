#Pandas

# 1) pandas dataframeler için hizli ve etkili

#Dataframe örneği (Excel gibi)

#isim yas medenihal
#ali  33   evli

# 2) csv ve text dosyalarını acip inceleyip sonucları da bu dosya tiplerine kaydedebiliriz
# 3) pandas bizim isimizi kolaystirir kayıp datalar için
# 4) reshape yapıp datayı daha etkili bir şekilde kullanabiliriz
# 5) slicing indexing kolay
# 6) time series data analizinde yardımcı
# 7) herseyden önemlisi hizlidir


import pandas as pd

dictionary ={"Name":["ali", "veli","kenan","hilal", "ayse", "evren"],
             "Age":[15,16,17,33,45,66],
             "Maas":[100,150,240,350,110,220]}

dataframe1 = pd.DataFrame(dictionary)

head = dataframe1.head()
tail = dataframe1.tail()


#%%
#pandas basic method

print(dataframe1.columns)

print(dataframe1.info())

print(dataframe1.dtypes)
print(dataframe1.describe())  #numeric feature = colums (age,maas)

#%%

#indexing and slicing

print(dataframe1["Age"])

print(dataframe1.Age)

dataframe1["yeni feature"] = [-1,-2,-3,-4,-5,-6]

print(dataframe1.loc[:3,"Age"])

print(dataframe1.loc[:3, "Name":"Maas"])

print(dataframe1.loc[:3, ["Name","Maas"]])

print(dataframe1.loc[::-1,:])

print(dataframe1.loc[:,:"Age"])

print(dataframe1.loc[:,"Name"])

print(dataframe1.iloc[:,2])  #Maas 2. indexte olduğu için iloc fonk kullandık 

#%%
#Filtering 

#True yada False

filtre1=dataframe1.Maas <200

filtrelenmis_data=dataframe1[filtre1]

filtre2=dataframe1.Age >30

dataframe1[filtre1 & filtre2]

dataframe1[dataframe1.Age>60]


#%%
#List Comprehension
import numpy as np
ortalama_maas = dataframe1.Maas.mean()
ortalama_maas

#ortalama_maas_np= np.mean(dataframe1.Maas)
#ortalama_maas_np

dataframe1["maas_seviyesi"] = ["Dusuk maas"if ortalama_maas >each else "Yuksek maas"for each in dataframe1.Maas]

dataframe1.columns = [each.upper() for each in dataframe1.columns]

dataframe1.columns = [each.split()[0]+"_"+ each.split()[1] if (len(each.split())>1) else each for each in dataframe1.columns ]
#%%
#Drop and concatenating
dataframe1.drop([1],axis=0,inplace=True)

data1=dataframe1.head()
data2=dataframe1.tail()

#vertical
data_concat = pd.concat([data1,data2],axis=0)

#Horizontal

maas = dataframe1.MAAS
name = dataframe1.NAME

data_h_concat = pd.concat ([maas,name],axis=1)
#%%
#transforming data

dataframe1["list_comp"] = [each*2 for each in dataframe1.MAAS]

#apply()

def multiply(MAAS):
    return MAAS*2

dataframe1["apply_metodu"]=dataframe1.MAAS.apply(multiply)
