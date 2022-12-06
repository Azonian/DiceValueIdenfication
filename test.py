import cv2
import numpy as np;
import easygui
import pytesseract
#import pandas as pd;


fileName = easygui.fileopenbox(filetypes=["*.jpg","*.jpeg","*.png"])
im = cv2.imread(fileName,cv2.IMREAD_COLOR)
fileName2 = easygui.fileopenbox(filetypes=["*.jpg","*.jpeg","*.png"])
im2 = cv2.imread(fileName2,cv2.IMREAD_COLOR)

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
invert = 255 - thresh

data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
print(data)


gray2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
thresh2 = cv2.threshold(gray2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
invert2 = 255 - thresh2

data2 = pytesseract.image_to_string(invert2, lang='eng', config='--psm 6')
print(data2)

data = str(data)
data2 = str(data2)

dice1 = 0
dice2 = 0 
# if equals to 1 its a number if quals to 2 its a dot
try:

    data = int(data)
    print("it's a number dice")
    dice1 = 1
except ValueError:

    print('Dot Dice')
    dice1 = 2

try:

    data2 = int(data2)
    print("it's a number dice")
    dice2 = 1
except ValueError:

    print('Dot Dice')
    dice2 = 2

if dice1 == 1:
    if dice2 == 1:
        # # this is where you check confidence
        # # # OCR detection
        # d1 = pytesseract.image_to_data(invert, config="--psm 6", output_type=pytesseract.Output.DICT)
        # d2 = pytesseract.image_to_data(invert2, config="--psm 6", output_type=pytesseract.Output.DICT)
        # print(d1['conf'])
        # print(d2['conf'])
        print("both are numbers")

    else:
        print("image one is the number")
else:
    if dice2 == 1:
        print("image two is the number")
    else:
        print("both images are dots")