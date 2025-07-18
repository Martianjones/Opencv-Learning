import cv2
import numpy as np
import matplotlib.pyplot as plt

# Sobel算子
'''
1、通过Sobel函数处理图像
2、使用convertScaleAbs函数计算绝对值
3、调用addWeighted函数计算最终结果
'''

img = cv2.imread('cat.jpg')
cat_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# 灰度化处理图像
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Sobel算子
x = cv2.Sobel(grayImage,cv2.CV_16S,1,0) #对x求一阶导
y = cv2.Sobel(grayImage,cv2.CV_16S,0,1) #对y求一阶导
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Sobel = cv2.addWeighted(absX,0.5,absY,0.5,0)

# 用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']

# 显示图形
titles = ['原始图像','Sobel算子']
images = [cat_img,Sobel]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i]),plt.xticks([]),plt.yticks([])
plt.show()