import cv2
import numpy as np
#import pandas as pd


image = cv2.imread(r'C:\Users\Admin\Desktop\I2IT_Workshop\lena.png')
row,col,plane = image.shape
print(row,col,plane)

dsize = (256,256)

# resize image
output = cv2.resize(image, dsize)

#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
row1,col1,plane= output.shape
print(row1,col1)
  
cv2.imshow('Original image',image)
cv2.imshow('Resized image', output)
cv2.waitKey(0)

isWritten = cv2.imwrite(r'C:\Users\Admin\Desktop\I2IT_Workshop\lena_gray.png', output)

if isWritten:
	print('The rezized image is successfully saved.')

cv2.destroyAllWindows()