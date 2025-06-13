import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('mhw.jpg')
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
r,result = cv2.threshold(grayImage,127,255,cv2.THRESH_BINARY)

hist = cv2.calcHist([img],[0],None,[256],[0,255])
hist_rest = cv2.calcHist([result],[0],None,[256],[0,255])

plt.figure(figsize=(8,6))
plt.subplot(221),plt.imshow(img,'gray'),plt.title('(a)'),plt.axis('off')
plt.subplot(222),plt.plot(hist),plt.title('(b)'),plt.xlabel('x'),plt.ylabel('y')
plt.subplot(223),plt.imshow(result,'gray'),plt.title('(c)'),plt.axis('off')
plt.subplot(224),plt.plot(hist_rest),plt.title('(d)'),plt.xlabel('x'),plt.ylabel('y')
plt.show()

