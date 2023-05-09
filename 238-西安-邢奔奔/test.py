# -*- coding: utf-8 -*-
import tifffile
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

# 灰度化
img = cv2.imread("D:\8ai\image\lenna.png")    #此处路径不能带有中文，并且读入图片数据为bgr
h, w = img.shape[:2]
img_gray = np.zeros([h, w], img.dtype)
for i in range(h):
    for j in range(w):
        m = img[i, j]
        img_gray[i, j] = int(m[0] * 0.11 + m[1] * 0.59 + m[2] * 0.3)
print(img_gray)
print("image show gray:%s" % img_gray)
cv2.imshow("image show gray", img_gray)

plt.subplot(221)
img = plt.imread("D:\8ai\image\lenna.png")
plt.imshow(img)
print("=====image gray=====")
print(img)




img_gray = rgb2gray(img)
plt.subplot(222)
plt.imshow(img_gray,cmap='gray')
print("----image gray----")
print(img_gray)


#rows,cols = img_gray.shape
#for i in range(rows):
#   for j in range(cols):
#       if(img_gray[i,j] <= 0.5):
#           img_gray[i,j] = 0
#        else:
#            img_gray[i,j] = 1;

img_binary = np.where(img_gray >= 0.5,1,0)
print("====image gray=====")
print(img_binary)
print(img_binary.shape)

plt.subplot(223)
plt.imshow(img_binary,cmap='gray')


img = plt.imread("D:\8ai\image\image1.jpg")
plt.subplot(224)
plt.imshow(img)
plt.show()
