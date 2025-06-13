import cv2
import numpy as np

# 创建黑色图像
img1 = np.zeros((256,256,3),np.uint8)
img2 = np.zeros((512,512,3),np.uint8)
img3 = np.zeros((256,256,3),np.uint8)

# 绘制多边形
pts1 = np.array([[10,80],[120,80],[120,200],[30,250]])   #四边形
cv2.polylines(img1,[pts1],True,(255,255,255),5)

pts2 = np.array([[50,190],[380,420],[255,50],[120,420],[450,190]])
cv2.polylines(img2,[pts2],True,(0,255,255),10)

# 绘制文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img3,'I love Python!',(10,100),font,0.5,(255,255,0),2)

# 显示图像
cv2.imshow('poly',img1)
cv2.imshow('poly2',img2)
cv2.imshow('Text',img3)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()