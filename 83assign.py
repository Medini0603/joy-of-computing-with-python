# Write a program to take an integer as the input and reverse that integer.

n=int(input())
s = [int(x) for x in str(n)]
s.reverse()
s="".join(str(x) for x in s)
s=int(s)
print(s)

# Take a list of strings as an input and write a program to write sort the list of strings on the basis of last character of each string.
# If last character is same, consider the second last character and so on.

def strrev(l):
  for i in range(len(l)):
    l[i]=l[i][::-1]

i=input()
user_list =i.split()
strrev(user_list)
user_list.sort()
strrev(user_list)
print(user_list)

# Take a student's email id as an input in the format rollNumber@institute.edu.in and write a program to find the roll number and institute name of the student.

str=input()
i=str.index('@')
j=str.index('.')
roll=str[:i]
ins=str[(i+1):j]
print(roll,ins) 