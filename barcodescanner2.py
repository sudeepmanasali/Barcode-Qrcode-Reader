# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 14:26:09 2020

@author: dell
"""


import cv2
from pyzbar.pyzbar import decode
import numpy as np         

cap= cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

while cap.isOpened():
    success, img = cap.read()
  
    for barcode in decode(img):
   
        mydata = barcode.data.decode("utf-8")
        print(mydata)
        pts=np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2)) 
        cv2.polylines(img,[pts],True,(255,0,0),5)
         
    cv2.imshow('Result', img)
 
    
    if cv2.waitKey(0)==27:
        
      cv2.destroyAllWindows()
    
      cap.release()  
           