import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('rot_fix.png')
original = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
canny = cv2.Canny(blurred, 120, 255, 1)
kernel = np.ones((5,5),np.uint8)
dilate = cv2.dilate(canny, kernel, iterations=1)

# Find contours
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

if len(cnts)!=0:
    c=max(cnts, key= cv2.contourArea)
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image, (x,y),(x+w,y+h),(0,255,0),2)
    ROI = original[y:y+h, x:x+w]
    cv2.imwrite("border_rot_fix.png", ROI)











# Iterate thorugh contours and filter for ROI
# image_number = 0
# for c in cnts:
#     x,y,w,h = cv2.boundingRect(c)
#     cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
#     ROI = original[y:y+h, x:x+w]
#     cv2.imwrite("./query/ROI{}.png".format(image_number), ROI)
#     image_number += 1


# cv2.imshow('canny', canny)
# cv2.imshow('image', image)
# plt.show()
# cv2.waitKey(0)
