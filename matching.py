
import cv2
import imutils

original = cv2.imread("master.png")
new = cv2.imread("m2.png")

#resize images
original = imutils.resize(original, height = 300)
new = imutils.resize(new, height = 300)

#find difference between the images
diff = original.copy()
cv2.absdiff(original, new, diff)
gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
 
#increasing the size of differences so we can capture them all
for i in range(0, 3):
    dilated = cv2.dilate(gray.copy(), None, iterations= i+ 1)
largest = dilated.max(axis=(0, 1))

#threshold the gray image to binarise it. Anything pixel that has
#value more than 3 we are converting to white
#(remember 0 is black and 255 is absolute white)
#the image is called binarised as any value less than 3 will be 0 and
# all values equal to and more than 3 will be 255
(T, thresh) = cv2.threshold(dilated, 3 , 255, cv2.THRESH_BINARY)
 
# find contours
cnts = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
    # draw a box around the differences
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(new, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imwrite("changes.png", new)