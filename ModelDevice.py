from picamera2 import Picamera2, Preview
import time
import numpy as np
from PIL import Image
import RPi.GPIO as GPIO
from gpiozero import AngularServo, Device
from gpiozero.pins.pigpio import PiGPIOFactory

#


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
#SERVO_POWER_PIN = 16  # Change this to the GPIO pin you are using

mosfetPin = 21

# Set up GPIO mode and PWM frequency
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering scheme
#GPIO.setup(SERVO_POWER_PIN, GPIO.OUT)  # Set the servo pin as an output
GPIO.setup(mosfetPin, GPIO.OUT)  # Set the servo pin as an output



#GPIO.setWarnings(False)


servo0 = AngularServo(13, min_angle=0, max_angle=160)

servo_is_open = False

old_servo_open_command = False

time_to_move = 0

stop_moving = False

time_open = 0
time_closed = 0

alreadyOpen = False

change_timestamp = 0

opening = False

thing_detected = False
thing_detection_time = 0

def move_servo(angle):
    global pwm
    duty = (angle/18) + 2
    pwm.ChangeDutyCycle(duty)

        
        

def run_recognition():
    global first_frame, image_array0, timer, MP_count, MP_now_detected, time_to_let_water_through, thing_detected, thing_detection_time, time_to_move, servo_is_open, SERVO_POWER_PIN, change_timestamp, opening, alreadyOpen, stop_moving, old_servo_open_command, servo_is_open
    #print(first_frame)

    image_array0 = picam0.capture_array()
    sum_red = 0
    pix_count = 0
    
    
    
    
    for i in range(0,len(image_array0)):
        for j in range(0,len(image_array0[0])):
            
            #sum_all = image_array0[i][j][0] + image_array0[i][j][1] + image_array0[i][j][2]343
            r = image_array0[i][j][0] + 0.1
            g = image_array0[i][j][1] + 0.1
            b = image_array0[i][j][2] + 0.1
            #sum_red+=((r / g)+(r / b))/2#/(sum_all+0.01)
            
            if i == 32 and j == 40:
                print(image_array0[i][j])
            pix_count+=1
    
    r = image_array0[32][40][2] + 0.1
    g = image_array0[32][40][1] + 0.1
    b = image_array0[32][40][0] + 0.1
    sum_red+=((r / g)+(r / b))/2
    
    
    
    
    print("`````" + str(sum_red) + "`````")
    
    if sum_red > 3:
        change_timestamp = time.time_ns()
        servo0.angle = 90
        GPIO.output(mosfetPin, True)
    elif sum_red <= 3 and time.time_ns() > change_timestamp + 1000000000 and time.time_ns() < change_timestamp + 1500000000:
        servo0.angle = 20
        GPIO.output(mosfetPin, True)
    elif sum_red <= 3 and time.time_ns() > change_timestamp + 1500000000:
        servo0.angle = 20
        GPIO.output(mosfetPin, False)
        
        
    if time.time_ns() < change_timestamp + 1000000000:
        servo0.angle = 90
        GPIO.output(mosfetPin, True)
        
    """
    if sum_red > 2 and alreadyOpen == False:
        change_timestamp = time.time_ns()
        alreadyOpen = True
        thing_detected = True
        thing_detection_time = time.time_ns()
        
    elif sum_red > 2 and alreadyOpen == True:
        opening = True
        thing_detection_time = time.time_ns()

        
    elif sum_red/pix_count <= 100 and alreadyOpen == True:
        change_timestamp = time.time_ns()
        alreadyOpen = False
        opening = False
    
    if time.time_ns() < change_timestamp + 500000000 and opening == True:
        GPIO.output(mosfetPin, True)
        servo0.angle = 90
    elif time.time_ns() < change_timestamp + 3500000000 and opening == False and time.time_ns() > thing_detection_time + 3000000000:
        GPIO.output(mosfetPin, True)
        servo0.angle = 20
    elif time.time_ns() > thing_detection_time + 4000000000:
        GPIO.output(mosfetPin, False)
        
    #print(str(thing_detection_time) + " ------ " + str(time.time_ns()) + " ------ " + str( change_timestamp + 500000000 and opening == True ))
    """

    """
    if old_servo_open_command != servo_is_open:
        stop_moving = False
        time_to_move = time.time_ns()
    if time.time_ns() > time_to_move + 1000000000:
         stop_moving = True
    
        
    
    if sum_red/pix_count > 100:
        print("red!")
        if stop_moving is False:
            GPIO.output(mosfetPin, True)
            servo0.angle = 90
        else:
            GPIO.output(mosfetPin, False)
        servo0.angle = 90
        servo_is_open = True
        #move_servo(90)
    else:
        print("not much here...")
        if stop_moving is False:
            GPIO.output(mosfetPin, True)
            servo0.angle = 20
        else:
            GPIO.output(mosfetPin, False)
        servo0.angle = 20
        servo_is_open = False
        #move_servo(20)
    print(servo_is_open)
    #time.sleep(0.1)
    old_servo_open_command = servo_is_open"""

    


times = []
timesSum = 0
testNumber = 150

if __name__ == "__main__":
    
    while time.time_ns() < start_time + 599900000000000:
        run_recognition()
        #time.sleep(1)
        #GPIO.output(mosfetPin, False)
        #time.sleep(1)
        #GPIO.output(mosfetPin, True)
        
    GPIO.cleanup()  # Clean up GPIO settings
    
    
