#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:15:03 2019

@author: roger
"""
from __future__ import print_function
import sys

if '/opt/ros/kinetic/lib/python2.7/dist-packages' in sys.path:
    sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')


#import

import imutils
import cv2
import matplotlib.pyplot as plt



#load image to grayscale and threshold
print("OpenCV Version: {}".format(cv2.__version__))
image = cv2.imread("tetris_blocks.png")
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

#CHECK TO SEE IF WE ARE USING OPENCV 2.X OR OPENCV 4
#if imutils.is_cv2() or imutils.is_cv4():
(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#CHECK TO SEE IF WE ARE USING OPENCV 3
#if imutils.is_cv3():
    #(_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#draw the contours on the image
cv2.drawContours(image, cnts, -1, (240, 0, 159), 3)
cv2.imshow("image",image)
cv2.waitKey(0)
#plt.imshow(image)



