import cv2
import numpy as np

im1 = cv2.imread(r'C:\Users\Asus\OneDrive\Pictures\Camera Roll\WIN_20230714_03_54_11_Pro.jpg')
 
# resize image 
im2 = cv2.resize(im1, (800, 800)) # (width height)
im3 = cv2.resize(im1, None, fx=0.5, fy=0.5) # (scalex, scaley)

# rotate image  

im4 = cv2.rotate(im1, cv2.ROTATE_90_CLOCKWISE)
im5 = cv2.rotate(im1, cv2.ROTATE_90_COUNTERCLOCKWISE)
im6 = cv2.rotate(im1, cv2.ROTATE_180)

#filters
im7 = cv2.GaussianBlur(im1, (5, 5),0)
gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(im1, cv2.COLOR_BGR2HSV)
gray3 = np.dstack((gray, gray ,gray))
print(gray3.shape)
color_filter_stack = np.hstack((gray3, rgb, hsv))


#cv2.imshow('original', im1)
#cv2.imshow('resize', im2)
#cv2.imshow('resize2',im3)
#cv2.imshow('roatate 90 clockwise', im4)
#cv2.imshow('rotate 90 counter clockwise',im5)
#cv2.imshow('rotate 180', im6)
#cv2.imshow('filter', im7)
cv2.imshow('stack',color_filter_stack)
cv2.waitKey(0)