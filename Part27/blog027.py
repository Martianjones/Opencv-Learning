import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('hamster.jpg')
hamster_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Scharr 算子
x = cv2.Scharr(grayImage,cv2.CV_32F,1,0)    #X 方向
y = cv2.Scharr(grayImage,cv2.CV_32F,0,1)    #Y 方向
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Scharr = cv2.addWeighted(absX,0.5,absY,0.5,0)

# Canny 算子
gaussian = cv2.GaussianBlur(grayImage,(3,3),0)
Canny = cv2.Canny(gaussian,50,150)

# LOG 算子
dst = cv2.Laplacian(gaussian,cv2.CV_16S,ksize=3)
LOG = cv2.convertScaleAbs(dst)

# 正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']

# 显示图形
titles = ['Source','Scharr','Canny','LOG']
images = [hamster_img,Scharr,Canny,LOG]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i]),plt.xticks([]),plt.yticks([])
plt.show()