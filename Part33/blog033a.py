import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('newspaper.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 中值滤波去除噪声
median = cv2.medianBlur(gray,3)
# 图像直方图均衡化
equalize = cv2.equalizeHist(median)
# Sobel算子锐化处理
sobel = cv2.Sobel(median,cv2.CV_8U,1,0,ksize=3)
# 图像二值化处理
ret,binary = cv2.threshold(sobel,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY)
# 膨胀和腐蚀处理设置膨胀和腐蚀操作的和函数
element1 = cv2.getStructuringElement(cv2.MORPH_RECT,(30,9))
element2 = cv2.getStructuringElement(cv2.MORPH_RECT,(24,6))

# 膨胀突出轮廓
dilation = cv2.dilate(binary,element2,iterations = 1)
# 腐蚀去掉细节
erosion = cv2.erode(dilation,element1,iterations = 1)
# 查找文字轮廓
region = []
contours,hierarchy = cv2.findContours(erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# 筛选面积
for i in range(len(contours)):
    # 遍历所有轮廓
    cnt = contours[i]
    # 计算轮廓面积
    area = cv2.contourArea(cnt)
    # 寻找最小轮廓
    rect = cv2.minAreaRect(cnt)
    # 轮廓的四个点坐标
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    # 计算高和宽
    height = abs(box[0][1]-box[2][1])
    width = abs(box[0][0]-box[2][0])

    # 过滤太细矩形
    if (height > width * 1.5):
        continue
    region.append(box)

# 定位的文字用绿线绘制轮廓
for box in region:
    print(box)
    cv2.drawContours(img,[box],0,(0,255,0),2)

# 显示图像
cv2.imshow('Gray Image',gray)
cv2.imshow('Result Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()