# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:50:52 2020

@author: dell
"""


import qrcode
# example data
data = "https://www.thepythoncode.com"
# output file name
filename = "site.png"
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)