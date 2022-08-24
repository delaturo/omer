import cv2
import os
import BetterConsoleLog.Log as Log
from datetime import datetime
import numpy as np


def getTempFile():
    my_path = os.path.abspath(os.path.dirname(__file__))
    tempFile = os.path.join(my_path,"..\\tmp_"+datetime.now().strftime("%d-%m-%Y_%H%M%S")+".png")
    return tempFile

def removeAlpha(src,dest):
    tmpImage = cv2.imread(src, cv2.IMREAD_UNCHANGED)
    B, G, R, A = cv2.split(tmpImage)
    alpha = A / 255

    R = (255 * (1 - alpha) + R * alpha).astype(np.uint8)
    G = (255 * (1 - alpha) + G * alpha).astype(np.uint8)
    B = (255 * (1 - alpha) + B * alpha).astype(np.uint8)

    new_img = cv2.merge((B, G, R))
    cv2.imwrite(dest, new_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

def cropImage(path):
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.abs(gray - 255)
    thresh = cv2.threshold(gray, 190, 200, 0)[1]

    # Find contour and sort by contour area
    cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    maxX = minX = -1
    maxY = minY = -1
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        # image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        
        if x < minX or minX ==-1:
            minX = x
        
        if (x+w) > maxX or maxX==-1:
            maxX = (x+w)

        if y < minY or minY ==-1:
            minY = y
        
        if (y+h) > maxY or maxY==-1:
            maxY = (y+h)
            
    ROI = image[minY:maxY,minX:maxX]
    newPath = os.path.splitext(path)[0]+"_cropped.jpg"
    cv2.imwrite(newPath,ROI)
    # newImgPath = os.path.splitext(path)[0]+"_proc.jpg"
    # cv2.imwrite(newImgPath,image)

totalCroppedImages = 0
def cropImagesIteration(path):
    global totalCroppedImages
    childs = os.listdir(path)
    for ch in childs:
        f = os.path.join(path,ch)
        if os.path.isdir(f):
            cropImagesIteration(f)
        if os.path.splitext(ch)[-1].lower() == ".jpg":
            cropImage(f)
            Log.logAsProgress("Processed: "+ ch, animated=True)