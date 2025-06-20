import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

img = cv2.imread('keyboard.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150)

# 显示原始图像
plt.subplot(121),plt.imshow(edges,'gray'),plt.title(u'(a)原始图像'),plt.axis('off')

# # 霍夫变换检测直线
# lines = cv2.HoughLines(edges,1,np.pi/180,160)
#
# # 转换为二维
# line = lines[:,0,:]
#
# # 将检测的线在极坐标中绘制
# for rho,theta in line[:]:
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0+1000*(-b))
#     y1 = int(y0+1000*(a))
#     x2 = int(x0-1000*(-b))
#     y2 = int(y0-1000*(a))
#     cv2.line(img,(x1,y1),(x2,y2),(255,0,0),1)


# 霍夫累计变换直线检测
minLineLength = 60
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,30,minLineLength,maxLineGap)

# 绘制直线
lines1 = lines[:,0,:]
for x1,y1,x2,y2 in lines1[:]:
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)
res = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


# 设置字体
matplotlib.rcParams['font.sans-serif']=['SimHei']

# 显示处理图像
plt.subplot(122),plt.imshow(res,'gray'),plt.title('(b)结果图像'),plt.axis('off')

plt.show()