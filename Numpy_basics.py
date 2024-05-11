
#%%
#importing


import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])  #1*15 vector

print(array.shape)


a=array.reshape(3,5)
print(a.shape)

print("dimesion (kaç boyutlu):", a.ndim)

print("data type: ",a.dtype.name)

print("size:", a.size)

print("type: ",type(a))


array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])

array1


zeros = np.zeros((3,4))

zeros[0,0] = 5 
print(zeros)

np.ones((3,4))

np.empty((2,3))

a=np.arange(1,932,5)
a

a=np.linspace(10,50,20)
a

#%%

#numpy basic operations

a=np.array([1,2,3])
b=np.array([4,5,6])

a+b
a-b
a**2
a*b

print(np.sin(a))

a<2

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,3],[4,5,6]])

#element wise prodcut

print(a*b)

#matrix prodcut

a.dot(b.T)

print(np.exp(a))

a=np.random.random((5,5))
a
a.sum()
a.max()
a.min()

a.sum(axis=0) #sütunları topla
a.sum(axis=1) #satırları topla


np.sqrt(a) #karekök
np.square(a) #karesi a**2

np.add(a,a)

#%%

#İndexing and slicing

array=np.array([1,2,3,4,5,6,7])

print(array[0])

print(array[0:4])

reverse_array=array[::-1]
print(reverse_array)

array1= np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(array1[1,1])

print(array1[:,1])
print(array1[1,1:4])

array1 

print(array1[-1,:])
print(array1[:,-1])

#%%

#shape manipulation

array= np.array([[1,2,3],[4,5,6],[7,8,9]])
array

#flatten  tek 1 satır haline getirme
a=array.ravel()
a

array2=a.reshape(3,3)
array2

#Transpoz
array2=array2.T

array2

print(array2.shape)

array5=np.array([[1,2],[3,4],[4,5]])
array5

array5.reshape(2,3)
array5


array5.resize(3,2)
array5

array5.resize(2,3)
array5

#%%

#Stacking arrays

array1=np.array([[1,2],[3,4]])
array2=np.array([[-1,-2],[-3,-4]])

#vertical

array3=np.vstack((array1,array2))
array3

#horizontal

array4=np.hstack((array1,array2))
array4

#%%

#Convert and Copy

liste = [1,2,3,4]
array=np.array([liste])
array

liste2= list(array)
liste2

a=np.array([1,2,3])
b=a
c=a

a
b
c

b[0]=5
a

d=np.array([1,2,3])
e=d.copy()

e
e[0]=12

e
d
