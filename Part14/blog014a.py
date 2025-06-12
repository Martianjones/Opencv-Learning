import cv2
import numpy as np
import matplotlib.pyplot as plt

# 固定阈值化处理方法
# 二值阈值化：像素点的灰度值大于阈值设其灰度值为最大值，小于阈值的像素点灰度值设定为0
# 反向二值阈值化：大于阈值的像素点设定为0，而小于该阈值的设定为255
# 截断阈值化：像素点灰度值小于阈值不改变，反之将像素点的灰度值设定为该阈值
# 超过阈值置0：像素点灰度值小于阈值不变，反之将像素点灰度值置为0
# 低于阈值置0：像素点灰度值小于阈值置为0，反之不改变

img = cv2.imread('dog.jpg')
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 阈值化处理
ret,thresh1 = cv2.threshold(grayImage,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(grayImage,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(grayImage,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(grayImage,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(grayImage,127,255,cv2.THRESH_TOZERO_INV)

# 显示结果
titles = ['GrayImage','Binary','Binary_inv','Trunc','Tozero','Tozero_inv']
images = [grayImage,thresh1,thresh2,thresh3,thresh4,thresh5]
for i in range(6):
    plt.subplot(2,3, i+1 ),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()