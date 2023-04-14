# Romeo and Juliet love each other. Romeo wants to send a message to Juliet and also don't want anyone to read it without his permission. So he shifted every small letter in the sentence by -2 position and every capital letter by -3 position. (If the letter is c, after shifting to by -2 position it changes to a, and for D new letter will be A).
# But the letter is too long and Romeo does not have enough time to encrypt his whole letter. Write a program to help Romeo which prints the encrypted message. You can assume there are no special characters except spaces and numeric value.


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