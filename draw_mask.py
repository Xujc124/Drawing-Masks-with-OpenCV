# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:38:59 2022

@author: Jacob Xu
"""

import os
import cv2
import numpy as np
import math

drawingFlag = False # True when mouse down

# Press Number Key 1 and hold: draw lines
# Press Number Key 2 and hold: draw rectangles
# Press Number Key 3 and hold: draw circles
# Press Esc to end the program

mode = [1,2,3]
mode_flag = 0
ix, iy = -1, -1  # create Callback function
 
 
def draw(event, x, y, flags, param):
    global ix, iy, drawingFlag, mode
    if event == cv2.EVENT_LBUTTONDOWN:# mouse down for the first time
        drawingFlag = True
        ix, iy = x, y # record initial positon with (x,y)

    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:# keep mouse down and move the mouse
        if drawingFlag == True:
            if mode_flag == 2:# draw rectangles
                cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 0), -1)
            elif mode_flag == 3:# draw circles
                cv2.circle(img,(ix,iy),int(math.sqrt(pow(ix-x,2)+pow(iy-y,2))),(0, 0, 0),-1)
                # print("ix, iy:", ix, iy, "x, y", x, y)

    # mouse up and end drawing process
    elif event == cv2.EVENT_LBUTTONUP and mode_flag == 1:# draw lines
        drawingFlag == False
        cv2.line(img, (ix, iy), (x, y), (0, 0, 0),
                 thickness=3, lineType=cv2.LINE_AA)# thick=30 slim=10 for test
 
 
    
if __name__ == '__main__':
    # draw_mode 1: single output
    # draw_mode 2: bunch output
    draw_mode = 1  # 
    if draw_mode == 1:
        # create project folder
        if os.path.exists('./mask')!=True:
            os.mkdir('./mask')
        # create output folder
        if os.path.exists('./mask/draw')!=True:
            os.mkdir('./mask/draw')
        # create background img
        img_test = np.zeros((224, 224, 3), np.uint8)
        for i in range(224):
            for j in range(224):
                for k in range(3):
                    img_test[i,j,k]=170
        cv2.imwrite('./mask/draw/draw.jpg',img_test,[int(cv2.IMWRITE_JPEG_QUALITY),70])# 
        
        # create new img
        img = np.zeros((224, 224, 3), np.uint8)
        for i in range(224):
            for j in range(224):
                for k in range(3):
                    img[i,j,k]=200
        # read background img
        exist = cv2.imread('./mask/draw/draw.jpg')
        # add new img to background img
        alpha = 0.1 # control opacity
        cv2.addWeighted(img, alpha, exist, 1 - alpha, 0, exist)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', draw)
        while(1):
            cv2.imshow('image', img)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('1'):
                mode_flag = mode[0]
            elif k == ord('2'):
                mode_flag = mode[1]
            elif k == ord('3'):
                mode_flag = mode[2]
            elif k == 27:
                cv2.destroyAllWindows()
                break
        
        # # binaryzation-white background with black masks
        # for i in range(224):
        #     for j in range(224):
        #         for k in range(3):
        #             if img[i,j,k] == 0:
        #                 img[i,j,k]=0
        #             else:
        #                 img[i,j,k]=255
                        
        # binaryzation-black background with white masks
        for i in range(224):
            for j in range(224):
                for k in range(3):
                    if img[i,j,k] == 0:
                        img[i,j,k]=255
                    else:
                        img[i,j,k]=0
        # save single img
        cv2.imwrite('./mask/draw/new_draw33.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),70])
        
        
    else:
        # save bunch img
        for ii in range(40,45):# output one img for one round
            # create project folder
            if os.path.exists('./mask')!=True:
                os.mkdir('./mask')
            # create output folder
            if os.path.exists('./mask/draw')!=True:
                os.mkdir('./mask/draw')
            # create background img
            img_test = np.zeros((224, 224, 3), np.uint8)
            for i in range(224):
                for j in range(224):
                    for k in range(3):
                        img_test[i,j,k]=170
            cv2.imwrite('./mask/draw/draw.jpg',img_test,[int(cv2.IMWRITE_JPEG_QUALITY),70])
            # create new img
            img = np.zeros((224, 224, 3), np.uint8)
            for i in range(224):
                for j in range(224):
                    for k in range(3):
                        img[i,j,k]=200
            # read background img
            exist = cv2.imread('./mask/draw/draw.jpg')
            # add new img to background img
            alpha = 0.1
            cv2.addWeighted(img, alpha, exist, 1 - alpha, 0, exist)
            cv2.namedWindow('image')
            cv2.setMouseCallback('image', draw)
            while(1):
                cv2.imshow('image', img)
                k = cv2.waitKey(1) & 0xFF
                if k == ord('1'):
                    mode_flag = mode[0]
                elif k == ord('2'):
                    mode_flag = mode[1]
                elif k == ord('3'):
                    mode_flag = mode[2]
                elif k == 27:
                    cv2.destroyAllWindows()
                    break
            
            # # binaryzation-white background with black masks
            # for i in range(224):
            #     for j in range(224):
            #         for k in range(3):
            #             if img[i,j,k] == 0:
            #                 img[i,j,k]=0
            #             else:
            #                 img[i,j,k]=255
                            
            # binaryzation-black background with white masks
            for i in range(224):
                for j in range(224):
                    for k in range(3):
                        if img[i,j,k] == 0:
                            img[i,j,k]=255
                        else:
                            img[i,j,k]=0
            # save single img
            cv2.imwrite('./mask/draw/new_draw' + str(ii) + '.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),70])
