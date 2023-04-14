import numpy as np
a=np.array([1,2,3,4])
print(a)
print(type(a))

print(a.shape)
print(a[0],a[1],a[2])

a[1]=6
print(a)

b=np.array([[1,2,3,4],[5,6,7,8]])
print(b)
print(b.shape)

c=np.zeros((2,2))
print(c)

d=np.ones((4,4))
print(d)

e=np.full((3,3),6)
print(e)

f=np.random.random((2,2))
print(f)

g=np.array([1,2,3])
print(g.dtype)
g=np.array([1,2,3],dtype=np.int64)
print(g.dtype)
g=np.array([1.0,2.0,3.0])
print(g.dtype)


x=np.array([[1,2],[3,4]],dtype=np.float64)
y=np.array([[5,6],[7,8]],dtype=np.float64)
print(x+y)
print(np.add(x,y))
print(np.subtract(x,y))
print(x*y)
print(np.multiply(x,y))
print(np.sqrt(x))
# Transpose
print(x.T)
print(np.sum(x))
print(np.sum(x,axis=0))
print(np.sum(x,axis=1))

y=np.array([[1,2]]),[3,4]
print(y)
print(np.sum(y))
print(np.square(3))


g=np.array([[1,2],[3,4]])
# print(g.T)
# print(g.T())
print(g.transpose())
# print(g.transpose)

a=np.array([[8,9,20],[10,31,22]])
b=np.array([[1,2,3],[4,5,6]])
print(a+b)

m=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(m.reshape(3,4))