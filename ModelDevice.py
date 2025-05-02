from picamera2 import Picamera2, Preview
import time
import numpy as np
from PIL import Image
import RPi.GPIO as GPIO

start_time = time.time_ns()


STARTX = 29
ENDX = 54

MP_count = 0

timer = 0

RESOLUTION_WIDTH = 83
RESOLUTION_HEIGHT = 64

picam0 = Picamera2(0)

camera_config0 = picam0.create_still_configuration(
    main={"size": (RESOLUTION_WIDTH, RESOLUTION_HEIGHT)}, 
    #lores={"size": (RESOLUTION_WIDTH, RESOLUTION_HEIGHT)}, 
    #raw={"size": (83,64)}, #26,20
    #display="lores",
    buffer_count=25
    )

picam0.configure(camera_config0)

#picam0.start_preview(Preview.QTGL)
picam0.start()

time.sleep(4)

image_array0 = picam0.capture_array()

# Define the GPIO pin to which the servo is connected
SERVO_PIN = 21  # Change this to the GPIO pin you are using

# Set up GPIO mode and PWM frequency
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering scheme
GPIO.setup(SERVO_PIN, GPIO.OUT)  # Set the servo pin as an output
#GPIO.setWarnings(False)



def run_recognition():
    global first_frame, image_array0, timer, MP_count, MP_now_detected, time_to_let_water_through
    #print(first_frame)

    image_array0 = picam0.capture_array()
    sum_red = 0
    pix_count = 0
    for i in range(0,len(image_array0)):
        for j in range(0,len(image_array0[0])):
            
            #sum_all = image_array0[i][j][0] + image_array0[i][j][1] + image_array0[i][j][2]
            r = image_array0[i][j][0] + 0.1
            g = image_array0[i][j][1] + 0.1
            b = image_array0[i][j][2] + 0.1
            sum_red+=((r / g)+(r / b))/2#/(sum_all+0.01)
            #if pix_count == 1000:
                #print(image_array0[i][j])
            pix_count+=1
        
    print("`````" + str(sum_red/pix_count) + "`````")
    if sum_red > 100:
        print("red!")
    else:
        print("not much here...")


    


times = []
timesSum = 0
testNumber = 150

if __name__ == "__main__":
    
    while time.time_ns() < start_time + 5999000000000:
        run_recognition()
        
    GPIO.cleanup()  # Clean up GPIO settings
    
    
