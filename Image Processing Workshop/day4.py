import cv2
import numpy as np
#import pandas as pd


image1 = cv2.imread(r'C:\Users\Admin\Desktop\I2IT_Workshop\lena.png')
row,col,plane = image1.shape
print(row,col,plane)

image2 = cv2.imread(r'C:\Users\Admin\Desktop\I2IT_Workshop\img1.png')
row,col,plane = image2.shape
print(row,col,plane)

dsize = (256,256)

# resize image
re1 = cv2.resize(image1, dsize)
re2 = cv2.resize(image2, dsize)


# add or blend the images
output = cv2.addWeighted(re1, 1, re2, 1, 0.0)

# save the output image
#cv2.imwrite('image.png', dst)

  
cv2.imshow('Lena image',image1)
cv2.imshow('Title image',image2)
cv2.imshow('Blended image', output)
cv2.waitKey(0)

isWritten = cv2.imwrite(r'C:\Users\Admin\Desktop\I2IT_Workshop\blended_img.png', output)

if isWritten:
	print('The Blended image is successfully saved.')

cv2.destroyAllWindows()