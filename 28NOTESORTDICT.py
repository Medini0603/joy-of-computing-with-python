import operator
con_factor={}
print(con_factor)

con_factor['dollar']=60
print(con_factor)
con_factor['euro']=800
print(con_factor)
con_factor['byen']=100
print(con_factor)

# to sort according to values 
sorted_con=sorted(con_factor.items(),key=operator.itemgetter(1))
print(sorted_con)

#to sort according to key
sorted_con=sorted(con_factor.items(),key=operator.itemgetter(0))
print(sorted_con)