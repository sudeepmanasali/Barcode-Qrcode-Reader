# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:39:12 2020

@author: dell
"""
import cv2
from pyzbar.pyzbar import decode
 

image = cv2.imread('download.png',0)
decodes=decode(image) 

 
for obj in decodes:
    print("DATA: ", obj.data);
    
cv2.imshow("Image", image)
  
cv2.waitKey(0)
cv2.destroyAllWindows()