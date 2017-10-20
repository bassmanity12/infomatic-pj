import sys
import network
from time import sleep
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
list =[1,2,3,4,5]
count =0
for j in list:
    wlan.connect("itcollege")
    if not wlan.isconnected():
          print ('Connecting ...itcollege')
          sleep(2.0)
    else:
          print ('connected')
          goto .end

if not wlan.isconnected():
    for j in list:
        wlan.connect("TTU Campus")
        if not wlan.isconnected():
            print ('Connecting ...TTU campus')
            sleep(2.0)
        else:
           print ('connected')
           goto .end

if not wlan.isconnected():
    print ('Faild to connect wifi network will turn off')
    wlan.active(False)

label .end
sys.exit()
