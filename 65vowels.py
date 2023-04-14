# Given a string S, write a function replaceV that accepts a string and replace the occurrences of 3 consecutive vowels with _ in that string. Make sure to return the answer string.
def isvowel(c):
  if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U'):
    return True
  return False

def consvow(s,i):
  if((i+2)<len(s) and isvowel(s[i+1]) and isvowel(s[i+2])):
    return True
  return False

def replaceV(s):
  i=0
  res=[]
  while(i<len(s)):
    if(isvowel(s[i])):
      if(consvow(s,i)):
        res.append("_")
        i=i+3
      else:
        res.append(s[i])
        i=i+1
    else:
      res.append(s[i])
      i=i+1
  res="".join(str(x) for x in res)
  return (res)


s=input("Enter your string : ")
print(replaceV(s))