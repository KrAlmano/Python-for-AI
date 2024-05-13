#matplotlib kutuphanesi
#gorsellestirme kutuphanesi

import pandas as pd

df = pd.read_csv("iris.csv")

print(df.columns)
print(df.Species.unique())


print(df.info())

print(df.describe())

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]

print(setosa.describe())
print(versicolor.describe())

#%%
import matplotlib.pyplot as plt

df1 = df.drop(["Id"], axis = 1)

#df1.plot()
#plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot ( setosa.Id , setosa.PetalLengthCm,color ="red",label="setosa")
plt.plot ( versicolor.Id , versicolor.PetalLengthCm,color ="green",label="versicolor ")
plt.plot ( virginica.Id , virginica.PetalLengthCm,color ="blue",label="setosa" )
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()

plt.show()

df1.plot (grid=True,linestyle=":")
plt.show()

df1.plot (grid=True,alpha=0.1)
plt.show()

#%%
#Scatter Plot 
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm, color="red",label="setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm, color="green",label="versicolor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm, color="blue",label="virginica")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm",fontsize=10)
plt.title("scatter plot")
plt.show()

print(setosa.columns)

#%%

#Histogram
plt.hist(setosa.PetalLengthCm,bins=25)
plt.xlabel("PetalLengthCm")
plt.ylabel("frekans")
plt.title("hist")
plt.show()

#%%
#Bar plot
import numpy as np
# =============================================================================
# x=np.array([1,2,3,4,5,6,7])
# y=x*2+5
# plt.bar(x,y)
# plt.title("bar plot")
# plt.xlabel("x")
# plt.ylabel("y")
# y.show()
# =============================================================================
x=np.array([1,2,3,4,5,6,7])
a=["turkey","usa","b","a","c","d","e"]
y=x*2+5
plt.bar(x,y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
#%%
#Subplots
import pandas as pd 
import matplotlib.pyplot as plt

# =============================================================================
# df1.plot(grid=True,alpha= 0.9,subplots = True)
# plt.show()
# 
# =============================================================================
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.subplot(2,1,1)
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label= "setosa")

plt.subplot(2,1,2)
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label= "versicolor")

plt.show()

