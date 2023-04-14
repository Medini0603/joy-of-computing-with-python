# '''s=input()
# if(s == s[::-1]):
#   print("palindrome")
# else:
#   print("not palindrome")'''

# def isPalindrome(s):
 
#     # Using predefined function to
#     # reverse to string print(s)
#     rev = ''.join(reversed(s))
 
#     # Checking if both string are
#     # equal or not
#     if (s == rev):
#         return True
#     return False
 
# # main function
# s =input()
# ans = isPalindrome(s)
 
# if (ans):
#     print("palindrome")
# else:
#     print("not palindrome")

# # j = -1
# # flag = 0
# # for i in s:
# #     print(s[j])
# #     if i != s[j]:
# #         flag = 1
# #         break
# #     j = j - 1
# # if flag == 1:
# #     print("palindrome")
# # else:
# #     print("not palindrome")

# Recursive function to check if a
# string is palindrome
def isPalindrome(s):

	# to change it the string is similar case
	s = s.lower()
	# length of s
	l = len(s)

	# if length is less than 2
	if l < 2:
		return True

	# If s[0] and s[l-1] are equal
	elif s[0] == s[l - 1]:

		# Call is palindrome form substring(1,l-1)
		return isPalindrome(s[1: l - 1])

	else:
		return False

# Driver Code
s = input()
ans = isPalindrome(s)

if ans:
	print("palindrome")

else:
	print("not palindrome")


 


s=input()
r=s
r=list(r)
s=list(s)
r.reverse()
flag=1
for i in range(len(s)):
  if(s[i]!=r[i]):
    flag=0
    print("not palindrome")
    break
if(flag):
  print("palindrome")

 