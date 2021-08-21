import cv2
import numpy as np

image = cv2.imread('master.png')
cv2.waitKey(0)

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 30, 200)
cv2.waitKey(0)

# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image
contours, hierarchy = cv2.findContours(edged,
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)

print("Number of Contours found = " + str(len(contours)))

idx = 0 
for c in contours: 
    x,y,w,h = cv2.boundingRect(c) 
    if w>50 and h>50: 
        idx+=1 
        new_img=image[y:y+h,x:x+w] 
        cv2.imwrite(str(idx) + '.png', new_img)