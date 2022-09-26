import numpy as np

my_list = [0,1,2,3,4]
arr = np.array(my_list)
print(arr)

a = np.arange(0,10)
print(a)

a= np.arange(0,10,2)
print(a)

a = np.zeros((5,5))
print(a)

a = np.ones((2,4))
print(a)

a = np.random.randint(0,10)
print(a)

a = np.random.randint(0,10,(3,3))
print(a)

a = np.linspace(0,10,6)
print(a)

a = np.linspace(0,10,101)
print(a)

np.random.seed(101)
arr = np.random.randint(0,100,10)
print(arr)
arr2 = np.random.randint(0,100,10)
print(arr2)

print(arr.max())
print(arr.min())
print(arr.mean())
print(arr.argmin())
print(arr.argmax())
print(arr.reshape(2,5))

mat = np.arange(0,100).reshape(10,10)
print(mat)

row = 0
col = 1

print(mat[row,col])
print(mat[:,col])
print(mat[row,:])

print(mat > 50)
print(mat[mat>50])
