# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:45:21 2019

@author: lab_pc
"""

import cv2
import os

def convert_to_video(time):
        
    img_array = []
    
    filenames=[]
    for i in range(time*10):
        if os.path.isfile("Images\\H_{}.png".format(i)):
#            print(i)
            filenames.append(os.getcwd()+"\\Images\\H_{}.png".format(i))
        else:
            print("break")
            break
    
    
    for filename in filenames:
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
     
     
    out = cv2.VideoWriter('sim_video_{}.mp4'.format(time),cv2.VideoWriter_fourcc(*'DIVX'),7, size)
     
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    print("video has been saved cheers!!")



