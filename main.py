import cv2 as cv
import time
import keyboard
from windowcapture import WindowCapture
from mousecontrol import Mouse
from botcontrol import Bot

windowname = "Roblox"

# initialize the WindowCapture class
wincap = WindowCapture(windowname)
mouse = Mouse((wincap.offset_x, wincap.offset_y), (wincap.w, wincap.h))
bot = Bot()

#Start Window Capture thrread.
wincap.start()
bot.start()

toggle = True

while(True):

    # if we don't have a screenshot yet, don't run the code below this point yet
    if wincap.screenshot is None:
        continue

    #Send captured video to mousecontrol.py
    mouse.function(wincap.screenshot)

    if toggle == True:
        bot.getMouseCoords(mouse.mouseXaxies,mouse.mouseYaxies)
    else:
        pass
    
    if keyboard.is_pressed("o"):
        toggle = False
    if keyboard.is_pressed("k"):
        toggle = True

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(1)
    if key == ord('q'):
        wincap.stop()
        cv.destroyAllWindows()
        break

print('Done.')

