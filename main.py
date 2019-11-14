import numpy as np 
import cv2 
import time
import detect

videoFeed = cv2.VideoCapture(0) 
time.sleep(1.000)

def roam():
    return

def led(color):
    return

def run():
    while (True): 
        ret, frame = videoFeed.read()
        if ret == False:
            print("Failed to retrieve frame")
            break 
        processed_img = detect.find_face(frame, 40)  # try to find face and return processed image
        if(processed_img[0]):     
            led('green')
            print('achou')
        else:
            led('red')
            roam()
        print(processed_img)
        cv2.imshow('Feed', frame) 
        if cv2.waitKey(10) & 0xFF == ord("q"): 
            break 
    videoFeed.release() 
    cv2.destroyAllWindows() 

run()