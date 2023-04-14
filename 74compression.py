import numpy as np
from PIL import Image
def mapping(pixelmap,i,j,k):
#     print(pixelmap[i,j][k])
    if(pixelmap[i,j][k]>=0 and pixelmap[i,j][k]<=31):
        return 0
    if(pixelmap[i,j][k]>=32 and pixelmap[i,j][k]<=63):
        return 1
    if(pixelmap[i,j][k]>=64 and pixelmap[i,j][k]<=95):
        return 2
    if(pixelmap[i,j][k]>=96 and pixelmap[i,j][k]<=127):
        return 3
    if(pixelmap[i,j][k]>=128 and pixelmap[i,j][k]<=159):
        return 4
    if(pixelmap[i,j][k]>=160 and pixelmap[i,j][k]<=191):
        return 5
    if(pixelmap[i,j][k]>=192 and pixelmap[i,j][k]<=223):
        return 6
    if(pixelmap[i,j][k]>=224 and pixelmap[i,j][k]<=255):
        return 7

img=Image.open("lena grey scale.png")
pixelmap=img.load()
# print(pixelmap[10,10][0])

# img.show()

# I=np.asanyarray(Image.open("lena grey scale.png"))
# print(I)

# create new image of same size and type 
im=Image.new(img.mode, img.size)
pixelnew=im.load()
print(type(pixelmap))
#NOTE 2^8 ---> 2^3
# so divide we get 2^5 
# 0 to 31  =  0
# 32 to 63 = 1
# 64 to 95 = 2
# 96 to 127 =3
# 128 to 159 =4
# 160 to 191 = 5
# 192 to 223 =6
# 224 to 255 =7
# print(mapping(pixelmap,0,0,0))
for i in range(im.size[0]):
    for j in range(im.size[1]):
        # if(pixelmap[i,j][0]>=0 and pixelmap[i,j][0]<=31):
        #     pixelnew[i,j]=0
        # elif(pixelmap[i,j][0]>=32 and pixelmap[i,j][0]<=63):
        #     pixelnew[i,j]=1
        # if(pixelmap[i,j][0]>=64 and pixelmap[i,j][0]<=95):
        #     pixelnew[i,j]=2
        # if(pixelmap[i,j][0]>=96 and pixelmap[i,j][0]<=127):
        #     pixelnew[i,j]=3
        # if(pixelmap[i,j][0]>=128 and pixelmap[i,j][0]<=159):
        #     pixelnew[i,j]=4
        # if(pixelmap[i,j][0]>=160 and pixelmap[i,j][0]<=191):
        #     pixelnew[i,j]=5
        # if(pixelmap[i,j][0]>=192 and pixelmap[i,j][0]<=223):
        #     pixelnew[i,j]=6
        # if(pixelmap[i,j][0]>=224 and pixelmap[i,j][0]<=225):
        #     pixelnew[i,j]=7
        l=[]
        for k in range(4):
                l.append(mapping(pixelmap,i,j,k))
                # print(l)

        pixelnew[i,j]=tuple(l)

im.save('lena compressed.png')

# J=np.asanyarray(Image.open('lena compressed.png'))