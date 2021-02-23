import cv2
import scipy.ndimage
 
a = cv2.imread('lena.jpeg', cv2.IMREAD_GRAYSCALE)
 
b = scipy.ndimage.filters.minimum_filter(a, size=5)

cv2.imshow('lena', a)
cv2.imshow('lena after min filtering', b)

cv2.waitKey(0)