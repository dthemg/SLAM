#!/usr/bin/env python

import cv2 

from display import Display

W, H = 1920//2, 1080//2

def process_frame(img):
    img = cv2.resize(img, (W, H))
    display.paint(img)
    
if __name__ == "__main__":
    display = Display(W, H)
    cap = cv2.VideoCapture("videos/fastcar.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break   
