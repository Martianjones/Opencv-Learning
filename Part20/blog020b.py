import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('scenery.png')
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist = cv2.calcHist(hsv,[0,1],None,[180,256],[0,180,0,256])

plt.figure(figsize=(8,6))
plt.subplot(121),plt.imshow(img_rgb,'gray'),plt.title('(a)'),plt.axis('off')

# 绘制H-S直方图
plt.subplot(122),plt.imshow(hist,interpolation='nearest'),plt.title('(b)'),plt.xlabel('x')
plt.ylabel('y'),plt.show()
