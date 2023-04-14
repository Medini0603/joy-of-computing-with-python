import numpy as np
from PIL import Image

# first fix dimension of image 
width=5
height =4

# create an array for image  
# each pixel has 3 parameters 
# 1.amount of red
# 2.amount of green 
# 3.amount of blue
array=np.zeros([height,width,3],dtype=np.uint8)
#NOTE:  ^Here array is a 2 D array i.e height x width and in each we have 3 color combination..
# this function creates an array of given dimension and 3 bytes one each for rgb and then dtype refers to uint i.e.unsigned int 
img=Image.fromarray(array)
img.save('text.png')
# as all dots in array are initialized to zeros all zeroes corresponds to colour black so we get a small black box as output in test.png 
array1=np.zeros([100,200,3],dtype=np.uint8)
array1[:,:100]=[255,128,0] #orange colour on left side
array1[:,100:]=[0,0,255] #blue colour on right side
img=Image.fromarray(array1)
img.save('text2.png')