# 教育机构 ：马士兵教育
# 时间 2023年4月开始正式学习
# 学员 陈玉曼

import cv2
import numpy as np
def funtion(img):
    height,width,channels =img.shape
    emptyImage=np.zeros((800,800,channels),np.uint8)
    sh=800/height
    sw=800/width
    for i in range(800):
        for j in range(800):
            x=int(i/sh + 0.5)
            y=int(j/sw + 0.5)
            emptyImage[i,j]=img[x,y]
    return emptyImage

img=cv2.imread("lenna.png")
zoom=funtion(img)
print(zoom)
print(zoom.shape)
cv2.imshow("nearest interp",zoom)  #这行代码使用了OpenCV库的imshow函数，用于显示缩放后的图像。该函数接受两个参数，
# 第一个参数是窗口的名称，第二个参数是要显示的图像。在这里，窗口的名称为"nearest interp"，表示使用最近邻插值算法进行缩放操作。而
# 要显示的图像则是变量"zoom"，即缩放后的图像。因此，这行代码的作用是在一个名为"nearest interp"的窗口中显示缩放后的图像。
cv2.imshow("image",img)
cv2.waitKey(0)