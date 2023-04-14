#Flipping image
from PIL import Image
# opening image 
img=Image.open("60image1.png")
# transposing i.e flipping the mirror image
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)

transposed_img.save("60im1corrected.png")
print("Done flipping")