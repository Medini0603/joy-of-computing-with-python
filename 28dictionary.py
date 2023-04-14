# dictionary has keys()  and  values() 
# they both together are called as items 

#key value
#key is always unique 
#value may or may not unique
#eg
#id  value is name,marks so on..

#to create dictionary with initializations
player1={0:'Rock',1:'Paper',2:'Scissor'}
print(player1)
con_factor={} #creates empty dictionary
#to addd items to dictionary
print(con_factor)

con_factor['dollar']=60
print(con_factor)
con_factor['euro']=80
print(con_factor)
con_factor['yen']=100
print(con_factor)

#to retrieve value of key
print(con_factor['euro'])

#to print all keys
print(con_factor.keys())

#to convert keys of dictionary to list
keyslist=list(con_factor.keys())
print(keyslist)


#to print all values
print(con_factor.values())

#to convert keys of dictionary to list
valueslist=list(con_factor.values())
print(valueslist)

print(con_factor.items())

#to change value of key
con_factor['dollar']=65
print(con_factor)


# to remove key and get its value 
val=con_factor.pop('yen')
print(val)
print(con_factor)

#to just delete
del con_factor['dollar']
print(con_factor)

#lets do some conversion using dictionary

con_factor['dollar']=60
print(con_factor)
con_factor['euro']=80
print(con_factor)
con_factor['yen']=100
print(con_factor)


e=30
r=e*con_factor['euro']
print(str(e)+" euros in rupees is "+str(r))


# NOTE::::
# One can make a dictionary inside a dictionary in python.
# Keys in the dictionary are not mutable.
