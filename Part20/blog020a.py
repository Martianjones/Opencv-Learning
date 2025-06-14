import cv2
import numpy
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from numpy.ma.core import shape

img = cv2.imread('scenery.png')
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

mask = np.zeros(img.shape[:2],np.uint8)
mask[100:300,100:300] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)

# 图像直方图计算
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,255])

plt.figure(figsize=(8,6))
matplotlib.rcParams['font.sans-serif']=['SimHei']

# 原始图像
plt.subplot(221),plt.imshow(img_rgb,'gray'),plt.axis('off'),plt.title('(a)原始图像')
plt.subplot(222),plt.imshow(mask,'gray'),plt.axis('off'),plt.title('(b)掩膜')
plt.subplot(223),plt.imshow(masked_img,'gray'),plt.axis('off'),plt.title('(c)图像掩膜处理')
plt.subplot(224),plt.plot(hist_full),plt.plot(hist_mask),plt.title('(d)直方图曲线'),plt.xlabel('x'),plt.ylabel('y')

plt.show()