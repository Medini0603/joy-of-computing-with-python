import string
s=input()
s=list(s)
d={}
for i in range(len(string.ascii_lowercase)):
  d[string.ascii_lowercase[i]]=string.ascii_lowercase[i-2]
for i in range(len(string.ascii_uppercase)):
  d[string.ascii_uppercase[i]]=string.ascii_uppercase[i-3]
  
for i in range(len(s)):
  if(s[i] in d):
    s[i]=(d[s[i]])
  else:
    continue
    
s=''.join(str(x) for x in s)
  
print(s)