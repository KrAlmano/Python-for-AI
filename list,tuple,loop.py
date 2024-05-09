#%%

#List

liste=[1,2,3,4,5,6]
liste_str=["pzt","sali","cars"]

liste[1]

last_value=liste[-1] #sondaki elemanı bulmak için

liste[0:3] #0. indis dahil 3. sü dahil değil demek ilk 3 değeri gösterir

liste.append(7)
liste

liste.remove(7)
liste
liste.reverse()
liste

liste2=[1,5,4,3,2,7,9]
liste2.sort()
liste2

string_int_liste=[1,2,3,"a","b","c"]


#%%

#Tuple

t=(1,2,3,4,5,6,1)

t.count(1)

t.index(2)
t.index(1)

#%%

#Dictionary

dictionary={"ali":32,"veli":45,"ayse":13}
dictionary["ali"]
type(dictionary["ali"])

#ali veli ayse = keys
#32,45,13 = values
dictionary.keys()
dictionary.values()

def deneme():
    dictionary={"ali":32,"veli":45,"ayse":13}
    return dictionary

dic=deneme()
dic["veli"]

#%%

#if else statements

var1 =10
var2 =10

if(var1>var2):
    print("var1 buyuktur var2")
elif (var1==var2) :
    print("Var1 ve var 2 esittir")
else: 
 print("var 1 kucuktur var2")    
 #%%
 def year2Century(year):
     """
     year to century
     """
     str_year = str(year)
     
     if(len(str_year)<3):
         return 1
     elif(len(str_year) == 3):
         if(str_year[1:3] == "00"):  # 100 ,200 300, 400 ... 900
             return int(str_year[0])
         else:                       # 190, 250, 450
             return int(str_year[0])+1
     else:                           # 1750, 1700, 1805
         if(str_year[2:4]=="00"):    # 1700, 1900, 1100
             return int(str_year[:2])
         else:                       # 1705, 1645, 1258
             return int(str_year[:2])+1