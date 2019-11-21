import numpy as np 
import cv2 
import time
import detect
import servo
import RPi.GPIO as GPIO

InvertTilt = False
min_tilt = 22          #minimum tilt angle in degree (up/down angle)
max_tilt = 80          #maximum tilt angle in degree
current_tilt = 0       #current tilt (info received from arduino and displayed in LCD numbers)
target_tilt = 90      #the tilt angle you need to reach

min_pan = 80            #minimum pan angle in degree(left/ right angle)
max_pan = 100         #maximum pan angle in degree
current_pan = 80        #current pan (info received from arduino and displayed in LCD numbers)
target_pan = 90       #the pan angle you need to reach

roam_target_pan = 90
roam_target_tilt = 90
roam_pause = 40      #amount of frame the camera is going to pause for when roam tilt or pan target reached

PanSensivity = 1
InvertPan = False
TiltSensivity = 1


videoFeed = cv2.VideoCapture(0) 
time.sleep(1.000)

def roam():
    return

def led(color):
    return


def calculate_movement(distance_X, distance_Y):

    global target_pan, PanSensivity, max_pan, target_tilt, TiltSensivity, min_tilt, max_tilt

    if(InvertPan): #handle inverted pan
        target_pan -= distance_X * PanSensivity
        if(target_pan>min_pan):
            target_pan = min_pan
        elif (target_pan < max_pan):
            target_pan = max_pan

    else:
        target_pan += distance_X * PanSensivity
        if(target_pan>max_pan):
            target_pan = max_pan
        elif (target_pan < min_pan):
            target_pan = min_pan


    #self.target_tilt += distance_Y * self.TiltSensivity

    if(InvertTilt): #handle inverted tilt
        target_tilt -= distance_Y * TiltSensivity
        if(target_tilt>min_tilt):
            target_tilt = min_tilt
        elif (target_tilt < max_tilt):
            target_tilt = max_tilt
    else:
        target_tilt += distance_Y * TiltSensivity
        if(target_tilt>max_tilt):
            target_tilt = max_tilt
        elif (target_tilt < min_tilt):
            target_tilt = min_tilt

    return target_pan, target_tilt

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
            target_pan, target_tilt = calculate_movement(processed_img[2], processed_img[3])
            servo.move(target_pan, target_tilt)
            print('target pan = ' + str(target_pan))
            print('target tilt = ' + str(target_tilt))
        else:
            led('red')
            roam()
        print(processed_img[0])
        cv2.imshow('Feed', frame) 
        if cv2.waitKey(10) & 0xFF == ord("q"): 
            print("cleaning up")
            GPIO.cleanup()
            break 
    videoFeed.release() 
    cv2.destroyAllWindows() 


def move(x, y):
    return
run()
