# import random
# bet=int(input("Your bet between 1 to 10 : "))
# lucky_draw=random.randint(1,10)
# print("Lucky draw showed : "+str(lucky_draw))
# account=0


#subtract 100 from both cases as we are paying 100 to play game
#if one wins then tjey get 900


# if(bet==lucky_draw):
#     account=account+900-100
# else:
#     account=account-100
# print(account)

#simulation for 1 week
# import random
# account=0

# for i in range(7):
#     bet=random.randint(1,10)
#     lucky_draw=random.randint(1,10)
#     print("Bet is : "+str(bet))
#     print("Lucky draw showed : "+str(lucky_draw))
#     if(bet==lucky_draw):
#         account=account+900-100
#     else:
#         account=account-100
#     print("Amount in your game account : "+str(account))

# #simulation for 1 month
# import random
# account=0

# for i in range(30):
#     bet=random.randint(1,10)
#     lucky_draw=random.randint(1,10)
#     print("Bet is : "+str(bet))
#     print("Lucky draw showed : "+str(lucky_draw))
#     if(bet==lucky_draw):
#         account=account+900-100
#     else:
#         account=account-100
#     print("Amount in your game account : "+str(account))

#simulation for 1 year
import random
import matplotlib.pyplot as plt
account=0
x=[]#day
y=[]#Amount in account

for i in range(365):
    x.append(i+1)
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    # print("Bet is : "+str(bet))
    # print("Lucky draw showed : "+str(lucky_draw))
    if(bet==lucky_draw):
        account=account+900-100
    else:
        account=account-100
    y.append(account)
    print("Amount in your game account : "+str(account))

plt.plot(x,y)
plt.show()