import cv2
import numpy as np
import matplotlib.pyplot as plt

# 图像直方图均衡化
img = cv2.imread('scenery.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
result = cv2.equalizeHist(gray)

# 现实图像
plt.subplot(221),plt.imshow(gray, cmap = plt.cm.gray),plt.axis('off'),plt.title('(a)')
plt.subplot(222),plt.imshow(result, cmap = plt.cm.gray),plt.axis('off'),plt.title('(b)')
plt.subplot(223),plt.hist(img.ravel(), 256),plt.title('c')
plt.subplot(224),plt.hist(result.ravel(), 256),plt.title('d')
plt.show()