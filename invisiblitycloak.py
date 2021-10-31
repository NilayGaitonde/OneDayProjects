# HSV=Hue Saturation Value
# HUE-Color
# SATURATION-Mixed with white
# VALUE- Mixed with black

import cv2
import numpy as np
import captureImage
import os
# get webcam open
video=cv2.VideoCapture(0)
if (os.path.isfile('./image.jpg')):
   pass
else:
   captureImage.capture()
   
background=cv2.imread('./image.jpg')
while video.isOpened():
   ret,frame=video.read()
   if ret:
      hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)    
      # lower=hue -10,100,100 higher:h+10,255,255
      #               B G  R
      blue=np.uint8([[[255,0,0]]])
      hsv_blue=cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
      lowerBlue=np.array([0,100,100])
      upperBlue=np.array([130,255,255])

      mask=cv2.inRange(hsv,lowerBlue,upperBlue)
      # part1 all things blue
      part1=cv2.bitwise_and(background,background,mask=mask)

      unmask=cv2.bitwise_not(mask)
      
      # all things not blue
      part2=cv2.bitwise_and(frame,frame,mask=unmask)
      cv2.imshow("mask",part1+part2)
      if cv2.waitKey(5) == ord('q'):
         break
video.release()
cv2.destroyAllWindows()
