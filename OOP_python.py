#%%

#Class

class Calisan:
    
    
    zam_orani=1.8
    counter=0
    def __init__(self,isim,soyisim,maas):
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.mail=isim+soyisim+"@gmail.com"
        
        Calisan.counter=Calisan.counter+1
        
    def giveNameSurname(self):
        return self.isim+" " +self.soyisim
        
            
    def zam_yap(self):
        self.maas=self.maas+self.maas*self.zam_orani
        
        
# isci1= Calisan("ali","cayirtepe",100)

# print(isci1.giveNameSurname())



#Class varianble
calisan1=Calisan("ali","cayirtepe",100)
print("ilk maas :",calisan1.maas)
calisan1.zam_yap()
print("yeni maas :",calisan1.maas)

calisan2=Calisan("ahmet","cayirtepe",200)