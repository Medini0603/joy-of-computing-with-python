# Image enhancement 
# One methods === Histogram equalization 
# contrast limited adaptive histogram equalization ==== CLAHE

import cv2
img=cv2.imread('60image2.png')
#Preparation for clahe
clahe=cv2.createCLAHE()
#Convert to grey scale image 
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Enhancement techniques 
enhanced=clahe.apply(gray_img)
#save to file
cv2.imwrite('60im2enhanced.png',enhanced)
print("Done enhancing")