import time

from machine import Pin

device_on = 0
device_off = 1

# create an output pin on pin #0
p0 = Pin(1, Pin.OUT)


p0.value(device_on)

while True:
    t0 = time.time()#starting at noon
    while time.time() < t0 + 28800:
        p0.value(device_on)
        time.sleep(610)
        p0.value(device_off)
        time.sleep(5)
        
    while time.time() < t0 + 28800 + 14400:
        p0.value(device_off)
        time.sleep(200)
        
    while time.time() < t0 + 28800 + 28800:
        p0.value(device_on)
        time.sleep(610)
        p0.value(device_off)
        time.sleep(5)
        
    while time.time() < t0 + 28800 + 28800 + 25200:
        p0.value(device_off)
        time.sleep(200)

    while time.time() < t0 + 28800 + 28800 + 25200 + 3600:
        p0.value(device_on)
        time.sleep(610)
        p0.value(device_off)
        time.sleep(5)    

p0.value(1)
time.sleep(0.1)
p0.value(0)