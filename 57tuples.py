ice_cream_flavours=("vanilla","strawberry","butterscoch","chocolate")
print(ice_cream_flavours)
for i in ice_cream_flavours:
    print(i)

print(ice_cream_flavours[2])
# cant replace
# ice_cream_flavours[2]="blackcurrent"
# cant add to tuple
# ice_cream_flavours[4]="blackcurrent"
#cant delete
# del ice_cream_flavours[2]

# i.e. tuples are IMMUTABLE 
# fixed data structure 

#to delete entire tuple
del ice_cream_flavours
# print(ice_cream_flavours)

toy=(1,2,3,4,2,2,5)
print(len(toy))
print(toy.count(2))

# returns first index 
print(toy.index(2))
print(toy.index(5))

# example where tuple is used 
rainbow=('Violet','Indigo','Blue','Green','Yellow','Orange','Red')
# i.e it cat be changes added or deleted once defined 

#Another example is image Processing..........
# Basic unit of picture is PIXEL 
#RGB color --->primary colors
# i.e proportion of rgb in that pixel 
pixel1=(0.1,0.5,0.9)
pixel2=(0.5,0.1,0.6)

#typecasting of list to tuple....
def cubeT(l):
  res=[]
  for i in l:
    num=i*i*i
    res.append(num)
  return tuple(res)

l=[1,2,3,4,5]
print(cubeT(l))
print(list(cubeT(l)))
