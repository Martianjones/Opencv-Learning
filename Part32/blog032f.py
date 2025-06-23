import cv2
import numpy as np

# 图像特效之素描特效
def dodgeNaive(image,mask):
    # 定义变量存储输入图片的宽高
    width,height = image.shape[:2]

    # 声明一个大小相同的输出numpy矩阵
    blend = np.zeros((width,height),np.uint8)

    for col in range(width):
        for row in range(height):
            # 检测每个像素
            if mask[col,row] == 255:
                # 避免除数为零
                blend[col,row] = 255
            else:
                # 将图片的像素转为8bit
                # 除以255与mask的差值
                tmp = (image[col,row]<<8)/(255-mask)
                if tmp.any() > 255:
                    tmp = 255
                    blend[col,row] = tmp
    return blend
def dodgeV2(image,mask):
    return cv2.divide(image,255-mask,scale = 256)
def burnV2(image,mask):
    return 255-cv2.divide(255-image,255-mask,scale=256)
def rgb_to_sketch(src_image_name,dst_image_name):
    img_rgb = cv2.imread(src_image_name)
    img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
    # 读取图片时直接转换操作
    img_gray_inv = 255 - img_gray
    img_blur = cv2.GaussianBlur(img_gray_inv,ksize=(21,21),sigmaX=0,sigmaY=0)
    img_blend = dodgeV2(img_gray,img_blur)
    cv2.imshow('Original',img_rgb)
    cv2.imshow('Gray',img_gray)
    cv2.imshow('Gray_inv',img_gray_inv)
    cv2.imshow('Gray_blur',img_blur)
    cv2.imshow('Pencil sketch',img_blend)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    src_image_name = 'scenery.png'
    dst_image_name = 'sketch_example.jpg'
    rgb_to_sketch(src_image_name, dst_image_name)
