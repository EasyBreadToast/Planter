import pydirectinput
import time 
from threading import Thread, Lock

pydirectinput.PAUSE = 0.0001

class Bot():
    
    x = 0
    y = 0
    toggle = True

    #Bot Actions/Values
    
    def getMouseCoords(self,xInput,yInput):
        if self.toggle == True:
            self.x = xInput
            self.y = yInput
        else:
            pass



    #Thread Properties

    def start(self):
        t = Thread(target=self.run)
        t.start()

    # main logic controller
    def run(self):
        while True:
            
            

            pydirectinput.move(1,1)
            pydirectinput.click(self.x,self.y)
            time.sleep(0.2)
            for move in range(642):
                pydirectinput.move(1,0)
                
                #For harvesting
                pydirectinput.keyDown("f")
            pydirectinput.keyUp("f")
            
            for move in range(316):
                pydirectinput.move(-2,0)
                pydirectinput.mouseDown()
                pass
            pydirectinput.mouseUp()

            pydirectinput.keyDown("s")
            time.sleep(0.1)
            pydirectinput.keyUp("s")
            time.sleep(0.5)
            print("Complete")
            pass

