import math
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 图像特效
img = cv2.imread('shanghai.jpg')
img_RGB = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
img_Gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rows,cols = img_RGB.shape[:2]

# 新建目标图像
dst1 = np.zeros((rows,cols,3),np.uint8)
dst2 = np.zeros((rows,cols,3),np.uint8)
dst3 = np.zeros((rows,cols,3),np.uint8)
dst4 = np.zeros((rows,cols,3),np.uint8)

# 图像怀旧特效
for i in range(rows):
    for j in range(cols):
        B = 0.272 * img_RGB[i, j][2] + 0.534 * img_RGB[i, j][1] + 0.131 * img_RGB[i, j][0]
        G = 0.349 * img_RGB[i, j][2] + 0.686 * img_RGB[i, j][1] + 0.168 * img_RGB[i, j][0]
        R = 0.393 * img_RGB[i, j][2] + 0.769 * img_RGB[i, j][1] + 0.189 * img_RGB[i, j][0]
        if B >255 :
            B = 255
        if G >255 :
            G = 255
        if R >255 :
            R = 255
        dst1[i,j] = np.uint8((B,G,R))

# 图像六年特效
for i in range(rows):
    for j in range(cols):
        # B 通道的数值开平方乘以参数十二
        B = math.sqrt(img_RGB[i,j][0])*12
        G = img[i,j][1]
        R = img[i,j][2]
        if B>255:
            B = 255
        dst2[i,j] = np.uint8((B,G,R))

# 图像光照特效
centerX = rows / 2
centerY = cols / 2
radius = min(centerX,centerY)

## 光照强度
strength = 200

for i in range(rows):
    for j in range(cols):
        distance = math.pow((centerY-j),2)+math.pow((centerX - i ),2)
        # 获取原始图像
        B = img_RGB[i, j][0]
        G = img_RGB[i, j][1]
        R = img_RGB[i, j][2]
        if (distance < radius*radius):
            # 按照距离大小计算增强的光照值
            result = (int)(strength * (1.0 - math.sqrt(distance)/radius))
            B = img_RGB[i, j][0] + result
            G = img_RGB[i, j][1] + result
            R = img_RGB[i, j][2] + result
            # 判断边剪 防止越界
            B = min(255, max(0, B))
            G = min(255, max(0, G))
            R = min(255, max(0, R))
            dst3[i, j] = np.uint8((B,G,R))
        else:
            dst3[i, j] = np.uint8((B,G,R))

# 图像水波特效
wavelength = 20
amplitude = 30
phase = math.pi / 4
centreX = 0.5
centreY = 0.5
radius = min(rows,cols)/8

# 设置水波覆盖面积
icentreX = cols*centreX
icentreY = rows*centreY

# 水波特效
for i in range(rows):
    for j in range(cols):
        dx = j - icentreX
        dy = i - icentreY
        distance = dx * dx + dy * dy

        if distance > radius*radius:
            x = j
            y = i
        else:
            # 计算水波区域
            distance = math.sqrt(distance)
            amount = amplitude * math.sin(distance / wavelength * 2 * math.pi - phase)
            amount = amount * (radius - distance) / radius
            amount = amount * wavelength / (distance + 0.0001)
            x = j + dx * amount
            y = i + dy * amount

        # 边界判断
        if x < 0:
            x = 0
        if x>= cols -1 :
            x = cols - 2
        if y<0:
            y = 0
        if y >= rows -1:
            y = rows - 2

        p = x - int(x)
        q = y - int(y)

        # 图像水波赋值

        dst4[i,j,:] = (1-p)*(1-q)*img[int(y),int(x),:] + p*(1-q)*img[int(y),int(x),:]+(1-p)*q*img[int(y),int(x),:]+p*q*img[int(y),int(x),:]


# 显示中文
plt.rcParams['font.sans-serif']=['SimHei']

# 显示图像
titles = ['原始图像','灰度图像','怀旧特效','流年特效','光照特效','水波特效']
images = [img_RGB,img_Gray,dst1,dst2,dst3,dst4]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray'),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()