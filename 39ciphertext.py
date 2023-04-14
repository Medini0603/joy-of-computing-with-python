from asyncore import read
from pickle import TRUE
import string
# print(string.ascii_letters)
dict={}
# here key is ascii letters and value is substituted cipher 
# now a is mapped to Z ,b to a , c to b so on..
for i in range (len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print (dict)

    # or 
# j=0
# for i in string.ascii_letters:
#     dict[i]=string.ascii_letters[j-1]
#     j=j+1
file=open("Outputcipher.txt","w")
with open("cipherinput.txt") as f:
    while(TRUE):
        c=f.read(1)
        # print(c)
        if not c:
        # if c is None:
            print("End of file")
            break
        if c in dict:
            data=dict[c]
            # its for ascii characters 
        else:
            data=c  
            # its for numbers and other special symbols 
        file.write(data)
        print(data)
file.close()