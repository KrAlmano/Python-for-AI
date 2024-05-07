#variable
#function
#object

#%%
#Variables

var1=10
var2=15

gun="pazartesi" #string
var3=10.2 #double


#%%

#String

s="Bugun gunlerden pazartesi"

variable_type = type(s)

print(s)


var1="ankara"
var2="ist"

var3=var1+var2

var4="100"
var5="200"
var6=var4+var5

uzunluk=len(var6)
uzunluk
var6[0]
#%%

#Numbers

#int double

integer_deneme = -50

#double = float = ondalikli sayi

float_deneme=-30.7

#%%

#Built in function
str1="deneme"
len(str1)

print(str1)

float1=10.6
print(float1)

round(float1) #10.6 yı 11 e yuvarladı

str2="1005"

type(int(str2))
#%%

#User defined functions

var1=10
var2=100

output=(((var1+var2)*50)/100)
output


#Fonksiyon parametresi = input
def ilk_func(a,b):
    """
    Bu ilk denemem
    
    parametre:
        
    return:
                    
    """
    output=(((a+b)*50)/100)
    
    return output

sonuc = ilk_func(1,2)
sonuc    

def deneme1():
    print("bu benim ikinci denemem")
    
    deneme1()
    
    
#%%

#Default function 
 
#cemberin cevre uzunluğu = 2*pi*r

def cember_cevre(r,pi=3.14):
    """
    cember cevresi hesapla
    input(parametre)=r,pi
    output = cemberin cevresi
    
    """
    output=2*pi*r
    return output
    
cember_cevre(3)


#Flexible function

def hesapla(boy,kilo,*args):
    output=(boy+kilo)
    return output

hesapla(10,30)

def hesapla(boy,kilo,yas):
    output=(boy+kilo)*yas
    return output

hesapla(10,30,10)

#%%

#Quiz denemesi

yas=10
name="Ahmet"
soyisim="Cayirtepe"

def function_quiz(yas,name,*args,ayak_num=35):
    print("Cocugun adı ", name ,"yasi:",yas,"ayak numarası",ayak_num)
    print("ismin karakter uzunluğu: ",(len(name)))
    print(type(yas))
    
    output = args[0]*yas
        return output

sonuc = function_quiz(yas, name, soyisim)
print("args[0]*yas:",sonuc)

#%%
#Lambda Function

def hesapla(x):
    output = x*x
    return output

hesapla(3)

sonuc2=lambda x:x*x
sonuc2(3)
