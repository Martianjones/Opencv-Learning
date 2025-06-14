import cv2
import numpy as np
import matplotlib.pyplot as plt



def func_judge(img):
    # 获取高度和宽度
    height,width = img.shape[:2]
    piexs_sum = height * width
    dark_sum = 0   # 偏暗像素个数
    dark_prop = 0  # 偏暗像素所占比例

    for i in range(height):
        for j in range(width):
            if img[i,j] < 50: # 阈值为50
                dark_sum +=1

    # 计算比例
    dark_prop = dark_sum * 1.0 /piexs_sum
    if dark_prop >= 0.8:
        print('This picture is dark!',dark_prop)
    else:
        print('This picture is bright!',dark_prop)

img = cv2.imread('nightscenery.jpg')
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([grayImage],[0],None,[256],[0,255])

func_judge(grayImage)

# 显示原始图像和绘制的直方图
plt.subplot(121),plt.imshow(img_rgb,'gray'),plt.axis('off'),plt.title('(a)')
plt.subplot(122),plt.plot(hist,color='r'),plt.xlabel('x'),plt.ylabel('y'),plt.title('(b)')
plt.show()