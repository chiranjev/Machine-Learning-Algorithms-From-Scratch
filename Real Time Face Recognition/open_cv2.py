# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:43:38 2018

@author: shl12
"""

import cv2

img = cv2.imread('images/dog2.jpg')
gray = cv2.imread('images/dog2.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('Dog image',img)
cv2.imshow('Gray Dog Image',gray)

cv2.waitKey(0)  # to keep screen open for infinite time
cv2.destroyAllWindows()