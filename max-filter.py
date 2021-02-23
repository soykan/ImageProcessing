import scipy.misc
import scipy.ndimage
import cv2
 
a = cv2.imread('lena.jpeg', cv2.IMREAD_GRAYSCALE)
b = scipy.ndimage.filters.maximum_filter(a, size=5)

cv2.imshow('Lena', a)
cv2.imshow('Lena after max filter', b)

cv2.waitKey(0)
