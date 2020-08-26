import cv2
import numpy as np
#import pandas as pd


image = cv2.imread(r'C:\Users\Admin\Desktop\I2IT_Workshop\lena.png')
row,col,plane = image.shape
print(row,col,plane)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
row1,col1 = gray.shape
print(row1,col1)
  
cv2.imshow('Original image',image)
cv2.imshow('Gray image', gray)

red_image = np.zeros((row,col,plane),np.uint8)
red_image[:,:,2]=image[:,:,2]
cv2.imshow('Red image', red_image)

green_image = np.zeros((row,col,plane),np.uint8)
green_image[:,:,1]=image[:,:,1]
cv2.imshow('Green image', green_image)

blue_image = np.zeros((row,col,plane),np.uint8)
blue_image[:,:,0]=image[:,:,0]
cv2.imshow('Blue image', blue_image)

cv2.waitKey(0)
cv2.destroyAllWindows()