import cv2
import numpy as np
import matplotlib.pyplot as plt

# 图像对数变换直方图对比

img = cv2.imread('mhw.jpg')
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
height,width = grayImage.shape[:2]
result = np.zeros((height,width),np.uint8)

for i in range(height):
    for j in range(width):
        gray = 42 * np.log(1.0 + grayImage[i,j])
        result[i,j] = np.uint8(gray)

hist = cv2.calcHist([img],[0],None,[256],[0,255])
hist_res = cv2.calcHist([result],[0],None,[256],[0,255])

plt.figure(figsize = (8,6))
plt.subplot(221),plt.imshow(img,'gray'),plt.title('(a)'),plt.axis('off')
plt.subplot(222),plt.plot(hist),plt.title('(b)'),plt.xlabel('x'),plt.ylabel('y')
plt.subplot(223),plt.imshow(result,'gray'),plt.title('(c)'),plt.axis('off')
plt.subplot(224),plt.plot(hist_res),plt.title('(d)'),plt.xlabel('x'),plt.ylabel('y')

plt.show()
