# Where input() function accepts a string, integer, and character input from a user and split() function to split an input string by space.
l=input("Enter numbers in a line").split()
# l.split()
print(l)

# map the single line input separated by white space into a list of integers.
lst = list(map(int, input("Type number with space: ").split()))
print(((lst[0])-(lst[2])))