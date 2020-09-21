import cv2
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
import os
from imutils.perspective import four_point_transform
from imutils import contours
import imutils

from PIL import Image
from pytesseract import image_to_string

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

def main():
    # Use the attached camera to capture images
    # 0 stands for the first one
    cap = cv2.VideoCapture(4)
    while cap.isOpened():
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        #frame = imutils.resize(frame, height=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(blurred, 50, 200, 255)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        #gray = cv2.medianBlur(gray, 3)
        #cv2.imwrite('temp.png',gray)
        cv2.imwrite('temp.png',edged)
        text = pytesseract.image_to_string(Image.open('temp.png'))
        os.remove('temp.png')
        print("Extracted Text: ", text)
        #cv2.imshow('frame', gray)
        cv2.imshow('edged', edged)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            return None

    cap.release()

if __name__ == "__main__":
    main()
