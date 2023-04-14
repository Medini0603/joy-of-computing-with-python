import string
s="Medini"

# convert 
print(s.upper())
print(s.lower())

# list 
ls=list(s)
print(ls)

# replace 
print(s.replace('i','#'))
print(s.replace('ni','#'))
print(s.replace('Me','#'))
# Case sensitive 
print(s.replace('me','#'))
print(s.replace('Me','#**'))

# splicing 
# 'NOTE :last index in not printed 
print(ls[1:4])
# default values 
print(ls[:4])
print(ls[2:])
print(ls[:])

#index 
print(ls.index('i'))

#NOTE: index[-1] corresponds to last element

print(ls[-1])
print(ls[-2])
print(ls[-3])
print(ls[-4])

s="joy of computing"
print(s[:])

y='i am amazed'
y.replace('a','z')
z=y.replace('a','z')
print(z)
print(y)


s="JOY"
print('#'.join(s))