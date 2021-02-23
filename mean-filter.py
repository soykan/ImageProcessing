import cv2
import numpy as np
import scipy.ndimage

a = cv2.imread('lena.jpeg')

a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

k = np.ones((5,5)) / 25

b = scipy.ndimage.filters.convolve(a, k)

cv2.imshow('Lena Original', a)
cv2.imshow('Lena mean filtered', b)

cv2.waitKey(0)