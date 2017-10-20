from time import sleep
from machine import Pin
som_led = Pin(2, mode=Pin.OUT)    # D9 on Wemos D1, LED on the SOM
sck_led = Pin(14, mode=Pin.OUT)   # D13 on Wemos D1, LED connected to SCK
for i in range(0,10):
    som_led.value(0) # Polarity inverted, pin sinks 3.3v
    sck_led.value(1) # Pin sources voltage
    sleep(0.2)
    som_led.value(1)
    sck_led.value(0)
    sleep(0.2)
