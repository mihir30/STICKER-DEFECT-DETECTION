import cv2
import numpy as np

import matplotlib.pyplot as plt

# Reading the image
im = cv2.imread('master.png')

# Converting image to grayscale
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# Thresholding and getting contours from the image
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
im_copy = im.copy()
cv2.drawContours(im_copy, contours, 0, (255, 0, 0), 3)
plt.imshow(im_copy)
plt.axis("off");