from gpiozero import LED
from gpiozero import Buzzer
import time
from signal import pause
led_red = LED(16)
led_white = LED(20)
led_green = LED(21)
bz=LED(26)
led_red.off()
led_white.off()
led_green.off()
bz.off()
def door_open():
    led_red.off()
    led_white.off()
    led_green.blink(on_time=.5, off_time=.3, n=5, background=False)
    bz.blink(on_time=.4, off_time=.3, n=7, background=False)
    led_green.on()
    time.sleep(10)
    led_green.off()
    
def door_close():
    led_white.off()
    led_green.off()
    led_red.on()
def door_fail_open():
    led_white.off()
    led_green.off()
    bz.on()
    time.sleep(2)
    bz.off()
    led_red.blink(on_time=.3, off_time=.2, n=8, background=False)
    led_red.on()

def door_verify_open():
    led_red.off()
    led_green.off()
    bz.blink(on_time=.1, off_time=.2, n=6, background=False)
    led_white.on()
    time.sleep(10)
    led_white.off()

door_open()
time.sleep(10)
door_fail_open()
time.sleep(10)
door_verify_open()
time.sleep(10)
