import time  
import threading  
from pynput.mouse import Button, Controller  
  
from pynput.keyboard import Listener, KeyCode  
  
  
# delayTime = 0.001  
buttonDirection = Button.right  
startStopButton = KeyCode(char=';')
terminateButton = KeyCode(char='xw')  
  
class ClickTheMouse(threading.Thread):  
    def __init__(self, delayTime, buttonDirection):  
        super(ClickTheMouse, self).__init__()  
        self.delayTime = delayTime  
        self.buttonDirection = buttonDirection  
        self.running = False  
        self.program_running = True  
  
    def startMouseclick(self):  
        self.running = True  
  
    def stopMouseClick(self):  
        self.running = False  
  
    def exitScript(self):  
        self.stopMouseClick()  
        self.program_running = False  
          
    def run(self):  
        while self.program_running:  
            while self.running:  
                mouse.click(self.buttonDirection)  
                time.sleep(self.delayTime)  
            time.sleep(0.1)  
  
mouse = Controller()  
clickThread = ClickTheMouse(delayTime, buttonDirection)  
clickThread.start()  
  
def on_press(key):  
    if key == startStopButton:  
        if clickThread.running:  
            clickThread.stopMouseClick()  
        else:  
            clickThread.startMouseclick()  
    elif key == terminateButton:  
        clickThread.exitScript()  
        listener.stop()  
  
  
with Listener(on_press=on_press) as listener:  
    listener.join()  