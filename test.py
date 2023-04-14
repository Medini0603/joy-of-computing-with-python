'''Ramesh is the principal of a school. Every year, he appoints some teachers to calculate the grades of students from the marks scored by them. Since technology is evolving Ramesh wants to digitize this process. So, he decided to hire a programmer for this task. 



You are given a dictionary where the keys are the name, and the values are another dictionary that contains subjects as keys and marks as values. Write a function convertMarks that takes a dictionary as an argument and returns a dictionary with marks replaced with grades. 
	

The principal has also provided the grades associated with the range of marks.

(Note: Both endpoints are included)


1
Grade - Marks
2
​
3
 A    -  91-100 
4
 B    -  81 - 90
5
 C    -  71 - 80
6
 D    -  61 - 70
7
 E+   -  51 - 60
8
 E    -  41 - 50
9
 F    -  0 - 40
10
​'''
def grades(mark):
    if(mark>=91 and mark<=100):
        return 'A'
    if(mark>=81 and mark<=90):
        return 'B'
    if(mark>=71 and mark<=80):
        return 'C'
    if(mark>=61 and mark<=70):
        return 'D'
    if(mark>=51 and mark<=60):
        return 'E+'
    if(mark>=41 and mark<=50):
        return 'E'
    if(mark>=0 and mark<=40):
        return 'F'

def converMarks(d):
    for stu in d.keys():
        dict={}
        dict=d[stu]
        for i in dict:
            
            dict[i]=grades(int(dict[i]))
        d[stu]=dict
    return d

name = input().split()

d = {}
for i in name:
    d[i] = {}
    subjects = input().split()
    marks = input().split()
    for j in range(len(subjects)):
        d[i][subjects[j]] = int(marks[j])

print(converMarks(d))

# Shyam has N Jars of Ladoos and he wants to distribute the Ladoos amongst M Villagers. The i-th jar contains Li pieces of Ladoos. He wants to make sure that every villager gets the same amount of ladoos and that the number of ladoos they receive is the greatest possible. He can open each jar and mix all the ladoos before distributing them to the villagers. How many pieces of ladoos will remain after he shares them amongst villagers, based on the rules described above?

# Input:
# The first line of input contains two integers: integer N, the number of ladoos, and M, number of villagers.
# The next line contains N non-negative integers.
mn=list(map(int,input().split()))
lado=list(map(int,input().split()))

lados=0
for i in range(len(lado)):
  lados+=lado[i]
  
rem=lados%mn[1]
print(rem)