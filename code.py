import time
import board
import digitalio


import usb_hid
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_de import KeyboardLayout
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)


# workaround: diffirent local keyboard layout...
import conversion_dvorak


def typeIt(string):
        string = conversion_dvorak.convert_ascii_dvorak(string)
        #string += "\n"
        layout.write(string)


debug = False

bnt1_pin = board.GP15
bnt2_pin = board.GP14

btn1 = digitalio.DigitalInOut(bnt1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2= digitalio.DigitalInOut(bnt2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN


while True:
    if btn1.value:
        if debug:
                print("buttn ! 1")
        keyboard.send(Keycode.SHIFT, Keycode.SEVEN)
        time.sleep(0.5)
        typeIt("gamemode 1\n")
        
    elif btn2.value:
        if debug:
                print("buttn! 2!")
        keyboard.send(Keycode.SHIFT, Keycode.SEVEN)
        time.sleep(0.5)
        typeIt("gamemode 2\n")
    else:
        if debug:
                print(".")
    time.sleep(0.1)




