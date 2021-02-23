import cv2
import scipy.ndimage

a = cv2.imread('salt-and-pepper-lena.png')

a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

b = scipy.ndimage.filters.median_filter(a, size=5)

cv2.imshow('Salt and Pepper Noised Lena', a)
cv2.imshow('After Median Filter Lena', b)

cv2.waitKey(0)