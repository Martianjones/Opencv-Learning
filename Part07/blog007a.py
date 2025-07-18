import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('street.jpg')
src = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

img1 = cv2.flip(src,0) # 参数=0 以X轴为对称轴翻转
img2 = cv2.flip(src,1) # 参数=1 以Y轴为对称轴翻转
img3 = cv2.flip(src,-1) # 参数<0 以X轴和Y轴翻转

# 显示图形
titles = ['Source','Horizontal','Vertical','Both']
images = [src,img1,img2,img3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()