from os import times
import pydirectinput
import cv2 as cv
import numpy as np
from time import sleep
from windowcapture import WindowCapture
import pydirectinput
import autoit

pydirectinput.PAUSE = 0.001


class Mouse:
    
    toggle = True
    mouseXaxies = 0
    mouseYaxies = 0
    middleHeight = 0
    middleWidth = 0
    color = 0

    def __init__(self, window_offset, window_size):

        # for translating window positions into screen positions, it's easier to just
        # get the offsets and window size from WindowCapture rather than passing in 
        # the whole object
        self.window_offset_x = window_offset[0]
        self.window_offset_y = window_offset[1] 
        self.window_w = window_size[0]
        self.window_h = window_size[1]

    def function(self, putithere):


        #Find the middle of the screen
        self.middleHeight = int(putithere.shape[0] / 2)
        self.middleWidth = int(putithere.shape[1] / 2)
        
        #All the visual processing
        hsv_frame = cv.cvtColor(putithere, cv.COLOR_BGR2HSV)
        
        low  = np.array([10, 0, 100])
        high = np.array([30, 130 ,255])
        mask = cv.inRange(hsv_frame, low, high)
        
        contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x:cv.contourArea(x), reverse=True)

        #Contours into crosshairs
        for cnt in contours:
            (x, y, w, h) = cv.boundingRect(cnt)

            #Pinpoint the contours
            x_medium = int((x + x + w) / 2)
            y_medium = int((y + y + h) / 2)

            #Contour crosshair
            cv.line(putithere, (x_medium, 0), (x_medium, (1000)), (0, 255, 0), 2)
            cv.line(putithere, (0, y_medium), ((1000), y_medium), (0, 255, 0), 2)

            #Limit time, preventing from over targeting.
            sleep(0.02)

            #Convert window and mouse position relatives
            self.mouseXaxies = x_medium + self.window_offset_x
            self.mouseYaxies = y_medium + self.window_offset_y

            break

        cv.imshow("P", putithere)