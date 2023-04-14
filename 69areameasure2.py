from PIL import Image
import random

im=Image.open("IndiaPunjab.png")
imrgb=im.convert("RGB")
counti=0
countp=0
count=0
while(count<=100000):
    x=random.randint(0,833)
    y=random.randint(0,934)
    z=0

    r,g,b=imrgb.getpixel((x,y))
    if(r==61):
        count+=1
        counti+=1
    elif(r==80):
        count+=1
        countp+=1

areap=(countp/counti)*3287263
print(areap)