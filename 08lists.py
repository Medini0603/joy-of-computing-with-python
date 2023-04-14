from turtle import st


shopping=["bread","sugar","coffee"]
print(shopping)

for item in shopping:
    print(item)

shopping.append("Curd")
print(shopping)

print(shopping[1])

for i in range(4):
    print(shopping[i])

shopping.insert(0,"oil")
print(shopping)

# Which of the following methods is correct to count the number of instances on an element in a list?
ages=[12,34,4,4,23,33,34,55,12,8,12,90,8,77]
print(ages.index(12,7,13))


print("People of age 12 = "+ str(ages.count(12)))
print("People of age 100 = "+ str(ages.count(100)))
print("People of age 33 = "+ str(ages.count(33)))
print("People of age 8 = "+ str(ages.count(8)))

l1=len(ages)
print(l1)
l2=len(shopping)
print(l2)

for i in range(l1):
    print(ages[i])

for item in ages:
    print(item)

ages.reverse()
print(ages)

ages.sort()
print(ages)

ages.reverse()
print(ages)

students=["sannidhi","medini","tanmay","manvith","samanvitha","bhargav"]
print(students)

students.sort()
print(students)

#as index starts from 0 use some dummy name at 0th location to start roll numbers from 1
students.insert(0,"ClassA")
print(students)

#slicing
#list_name[startindex:endindex+1]

print(students[1:5])#it prints 1 to 4 items
print(students)
print(students[:])
print(students[3:])
print(students[:5])
#default start value=0
#defsult end value=length of list

print(students[2:5])
students=students[2:5]
print(students)

L=['Python','C++','Java','Kotlin']

for lang in range(len(L)):
    print(lang)
    print(L[lang])