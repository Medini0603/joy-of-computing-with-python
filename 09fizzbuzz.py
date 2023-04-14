#us a syntax
#  def fun_name():
#  to define a function 

# def inputno(n1,n2):
#     n1=input("Enter starting number of game")
#     n2=input("Enter last number of the game")

def fizzbuzz(n1,n2):
    i=int(n1)
    for i in range(int(n2)+1):
        if(i%3==0 and i%5==0):
            print(str(i)+"FizzBuzz")
        elif(i%3==0):
            print(str(i)+"Fizz")
        elif(i%5==0):
            print(str(i)+"Buzz")
        else:
            print(i)


n1=input("Enter starting number of game")
n2=input("Enter last number of the game")
fizzbuzz(n1,n2)