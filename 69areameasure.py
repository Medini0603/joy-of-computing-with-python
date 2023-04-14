# now to find area of punjab in india given area of INDIA 
# we should randomly place dots inside India map
# now count number of dots in punjab area and outside punjab area 
# now ( punjab dots/out of punjab dots )/area of india gives avg area of punjab
# to increase accuracy we need to increae number of iterations

import random
import imageio
img=imageio.v2.imread("IndiaPunjab.png")
countp=0
counti=0
count=0
while(count<=100000):
    #ulta x and y in python 
    #get dimensions from the details of properties of image
    x=random.randint(0,934)
    y=random.randint(0,833)
    z=0

    if(img[x][y][z]==61):
        counti+=1
        count+=1
    elif(img[x][y][z]==80):
        countp+=1
        count+=1

areap=(countp/counti)*3287263
print(areap)