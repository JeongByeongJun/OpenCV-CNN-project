#!/usr/bin/env python
# coding: utf-8
# In[31]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("C:\input/test.png",cv2.IMREAD_COLOR)
plt.figure(figsize=(15,12))
plt.imshow(img)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(15,12))
plt.imshow(img_gray);
img_blur=cv2.GaussianBlur(img_gray,(5,5),0)
plt.figure(figsize=(15,12))
plt.imshow(img_blur);
ret,img_th=cv2.threshold(img_blur,75,170,cv2.THRESH_BINARY_INV)
contours,hierachy=cv2.findContours(img_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rects=[cv2.boundingRect(each)for each in contours]
rects
tmp=[w*h for (x,y,w,h)in rects]
tmp.sort()
print(tmp)
rects=[(x,y,w,h)for (x,y,w,h)in rects]
rects
img_result=[]
img_for_class=img.copy()
margin_pixel=20
for rect in rects:
    img_result.append(img_for_class[rect[1]-margin_pixel:rect[1]+rect[3]+margin_pixel,rect[0]-margin_pixel:rect[0]+rect[2]+margin_pixel])
    cv2.rectangle(img,(rect[0],rect[1]),(rect[0]+rect[2],rect[1]+rect[3]),(0,255,0),5)
plt.figure(figsize=(15,12))
plt.imshow(img);

count=0
nrows=3
ncols=4
plt.figure(figsize=(12,8))
for n in img_result:
    count+=1
    plt.subplot(nrows,ncols,count)
    plt.imshow(cv2.resize(n,(28,28)),cmap='Greys',interpolation='nearest')
    cv2.imwrite("images.png",n)
plt.tight_layout()
plt.show()

img_w = 640 
img_h = 480
bpp = 3

img = np.zeros((img_h,img_w, bpp), np.uint8)


red = (0, 0, 255)
green = (0,255,0)
blue =(255,0,0)
white = (255,255,255)
yellow = (0,255,255)
cyan = (255,255,0)

center_x = int(img_w / 2.0)
center_y = int(img_h / 2.0)

thickness = 2

location = (center_x - 200, center_y-100)
font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
fontScale = 3.5
cv.putText(img,'OpenCV',location, font, fontScale, yellow, thickness)

location = (center_x - 150, center_y + 20)
font = cv.FONT_ITALIC
fontScale = 2
cv.putText(img,'Tutorial',location, font, fontScale, red, thickness)


cv.imshow("drawing", img)
cv.waitKey(0)






