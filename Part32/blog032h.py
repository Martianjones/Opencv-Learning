import cv2
import numpy as np



# 图像特效
# 滤镜特效
def getBGR(img,table,i,j):
    # 获取图像颜色
    b,g,r = img[i][j]
    # 计算标准颜色表中颜色的位置坐标
    x = int(g/4 + int(b/32)*64)
    y = int(r/4 + int((b%32)/4)*64)
    # 返回滤镜颜色表中对应的颜色
    return lj_map[x][y]

# 读取原始图像
img = cv2.imread('cangyuantu.jpg')
lj_map = cv2.imread('table.png')

# 获取图像行和列
rows,cols = img.shape[:2]

# 新建目标图像
dst1 = np.zeros((rows,cols,3),np.uint8)
dst2 = np.zeros((rows,cols,3),np.uint8)

# 循环设置滤镜颜色
for i in range(rows):
    for j in range(cols):
        dst1[i][j] = getBGR(img,lj_map,i,j)

# 提取三个颜色通道
(b,g,r) = cv2.split(img)
# 彩色图像均衡化
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
# 合并通道
dst2 = cv2.merge((bH,gH,rH))



# 显示图像
cv2.imshow('Source',img)
cv2.imshow('Destination one',dst1)
cv2.imshow('Destination two',dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()