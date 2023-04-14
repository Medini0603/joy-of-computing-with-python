from PIL import Image
im=Image.open("text2.png")

# convert image to rgb 
im_rgb=im.convert('RGB')

#getpixel gives rgb values from matrix of given image
# r,g,b are 3 variables to store pixel values of colour red ,green and blue 
r,g,b=im_rgb.getpixel((1,1))
r1,g1,b1=im_rgb.getpixel((101,1))

print(r,g,b)
print(r1,g1,b1)