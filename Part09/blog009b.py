import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取原始图片
img = cv2.imread('dragonboat.png',1)

# 设置鼠标左键开启
en = False

# 鼠标事件
def draw(event,x,y,flags,param):
    global en
    # 鼠标左键按下开启en值
    if event == cv2.EVENT_LBUTTONDOWN:
        en = True
    # 鼠标左键按下并且移动
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_LBUTTONDOWN:
        # 调用马赛克函数
        if en:
            drawMask(y,x)
            # 鼠标左键弹起结束操作
        elif event == cv2.EVENT_LBUTTONUP:
            en = False

# 图像局部采样操作
def drawMask(x,y,size=10):
    # size*size 采样处理
    m = int(x/size*size)
    n = int(y/size*size)
    print(m,n)
    # 10*10 区域设置为同一像素值
    for i in range(size):
        for j in range(size):
            img[m+i][n+j] = img [m][n]

# 打开对话框
cv2.namedWindow('image')

# 调用draw函数设置鼠标操作
cv2.setMouseCallback('image',draw)

#循环处理
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(10)&0xFF==27:
        break
    # 按s键保存图片
    elif cv2.waitKey(10)&0xFF==115:
        cv2.imwrite('motified.png',img)

# 退出窗口
cv2.destroyAllWindows()