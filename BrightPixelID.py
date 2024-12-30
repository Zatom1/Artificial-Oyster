from picamera2 import Picamera2, Preview
import time
import numpy as np
from PIL import Image
import ctypes
import numpy.ctypeslib
import RPi.GPIO as GPIO

start_time = time.time_ns()

time.sleep(10)

loopLib = ctypes.CDLL('../Running/loopLib.so')

BRIGHTNESS_THRESHOLD = 700

STARTX = 29
ENDX = 54

MP_count = 0

timer = 0

RESOLUTION_WIDTH = 83
RESOLUTION_HEIGHT = 64

#old_image_array0 = np.full((83,64, 3), 0)
#old_image_array1 = np.full((83,64, 3), 0)
#print(old_image_array0)
picam0 = Picamera2(0)
picam1 = Picamera2(1)

#picam0.set_controls({"AeMode": 0, "AwbMode": 0, "AfMode": 0})
#picam1.set_controls({"AeMode": 0, "AwbMode": 0, "AfMode": 0})

camera_config0 = picam0.create_still_configuration(
    main={"size": (RESOLUTION_WIDTH, RESOLUTION_HEIGHT)}, 
    lores={"size": (RESOLUTION_WIDTH, RESOLUTION_HEIGHT)}, 
    raw={"size": (26,20)}, #26,20
    display="lores",
    buffer_count=25
    )
camera_config1 = picam1.create_still_configuration(
    main={"size": (RESOLUTION_WIDTH, RESOLUTION_HEIGHT)}, 
    lores={"size": (RESOLUTION_WIDTH, RESOLUTION_HEIGHT)}, 
    raw={"size": (26,20)}, 
    display="lores",
    buffer_count=25
    )

#camera_config0 = picam0.create_still_configuration(main={"size": (83, 64)}, lores={"size": (26, 20)}, display="lores", output = "raw")
#camera_config1 = picam1.create_still_configuration(main={"size": (83, 64)}, lores={"size": (26, 20)}, display="lores", output = "raw")

picam0.configure(camera_config0)
picam1.configure(camera_config1)

#picam0.start_preview(Preview.QTGL)
picam0.start()
picam1.start()

picam0.set_controls({'ExposureTime': 3000})#need 4000
picam1.set_controls({'ExposureTime': 3000})
picam0.set_controls({"AeEnable": 0, "AwbEnable": 0, "FrameRate": 250})
picam1.set_controls({"AeEnable": 0, "AwbEnable": 0, "FrameRate": 250})

time.sleep(4)

#def averageSquare(x, y, radius, array):
    #valueSum = 0
    #for x in range(0,radius):'
    
image_array0 = np.array(picam0.capture_array(), dtype=np.int32)
image_array1 = np.array(picam1.capture_array(), dtype=np.int32)

old_image_array0 = image_array0
old_image_array1 = image_array1

first_frame = True

time_to_let_water_through = time.time_ns()
MP_now_detected = False


# Define the GPIO pin to which the servo is connected
SERVO_PIN = 12  # Change this to the GPIO pin you are using

# Set up GPIO mode and PWM frequency
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering scheme
GPIO.setup(SERVO_PIN, GPIO.OUT)  # Set the servo pin as an output
#GPIO.setWarnings(False)

# Set up PWM on the servo pin with a frequency of 50Hz (standard for most servos)
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)  # Start PWM with a duty cycle of 0 (initially off)

def is_close_to_time(targetTime):#check if within 1/1000 of a second
    time_now = time.time_ns()
    if abs(time_now - targetTime) < 10000000:
        return True
    return False

def turn_servo(angle):
    """
    Move the servo to a specific angle.
    
    :param angle: Desired angle in degrees (0 to 180)
    """
    # Calculate duty cycle for the angle
    duty_cycle = (angle / 18) + 2  # Conversion formula for servo control
    pwm.ChangeDutyCycle(duty_cycle)  # Set the PWM duty cycle
    #time.sleep(1)  # Wait for the servo to move
    

def run_recognition():
    global first_frame, old_image_array0, old_image_array1, image_array0, image_array1, timer, MP_count, MP_now_detected, time_to_let_water_through
    #print(first_frame)

    if first_frame == True:
        image_array0 = np.array(picam0.capture_array(), dtype=np.int16)
        image_array1 = np.array(picam1.capture_array(), dtype=np.int16)
        first_frame = False
    else:
        image_array0 = np.array(picam0.capture_array(), dtype=np.int16)
        image_array1 = np.array(picam1.capture_array(), dtype=np.int16)
    """
    if timer < 1:
        pass
    else:
        img_change0 = image_array0 - old_image_array0
        img_change1 = image_array1 - old_image_array1
    
    #Make an image from the array
    #image0 = Image.fromarray(image_array0)
    #image1 = Image.fromarray(image_array1)
    
    # Display the image using PIL
    #image0.show()
    #image1.show()
    
    #print(image_array0[0][0])
    #print(image_array0[0][0][0] + image_array0[0][0][1] + image_array0[0][0][2])
    #print(len(image_array0[0]))
    
    #brightpixels = np.full((1600,2), 0)
    
    brightpixels = [cam0, cam1]
    cam0 = [(#,#), (#,#), (#,#), (#,#), (#,#), (#,#), (#,#), (#,#)]
    cam1 = [(#,#), (#,#), (#,#), (#,#), (#,#), (#,#), (#,#), (#,#)]
    
    
    #nextValue = 0
    #brightpixels1 = np.em
    
    for i in range(STARTX, ENDX):
    
        #print("testing")
        for j in range(0, len(image_array0[i])):
            pixelvalue = 0
            pixelvalue += ((image_array0[i][j][0] + image_array0[i][j][1] + image_array0[i][j][2]))
            if pixelvalue > BRIGHTNESS_THRESHOLD:
                brightpixels0.append([i,j])
                
    for i in range(STARTX, ENDX):
        #print("testing")
        for j in range(0, len(image_array1[i])):
            pixelvalue = 0
            pixelvalue += ((image_array1[i][j][0] + image_array1[i][j][1] + image_array1[i][j][2]))
            if pixelvalue > BRIGHTNESS_THRESHOLD:
                brightpixels1.append([i,j])
    """
    #print (old_image_array0)
    #PARAMETERS: (img_arr, old_img_arr, brightness_change_required for id, MP count required for ID, rows#, cols#)
    cam0MP = loopLib.find_bright_pixels(numpy.ctypeslib.as_ctypes(image_array0), numpy.ctypeslib.as_ctypes(old_image_array0), 600, 100, 64, 83)
    cam1MP = loopLib.find_bright_pixels(numpy.ctypeslib.as_ctypes(image_array1), numpy.ctypeslib.as_ctypes(old_image_array1), 600, 100, 64, 83)
    #print(cam0MP)
    if cam0MP == 1 or cam1MP == 1:
        MP_count += 1
        MP_now_detected = True
    
    #print(timer)
    #print(image_array0[40][40])
    #print(old_image_array0[40][40])
    
    if MP_now_detected == True:
        turn_servo(65)
        print("start filtering")
        time_to_let_water_through = time.time_ns() + 1000000000

    MP_now_detected = False
    
    if is_close_to_time(time_to_let_water_through):
        turn_servo(115)
        print("stop filtering")

    

    """
    for i in range(STARTX, ENDX):
    #print("testing")
        for j in range(0, RESOLUTION_HEIGHT):
            #pixelvalue = 0
            #pixelvalue += ((image_array0[i][j][0] + image_array0[i][j][1] + image_array0[i][j][2]))
            #if pixelvalue > BRIGHTNESS_THRESHOLD:
                #brightpixels0.append([i,j])
            # a = image_array0[i][j][2]
            #b = image_array1[i][j][2]
            
            #if a+b > BRIGHTNESS_THRESHOLD*(2/3):
                #pass

            


            if image_array0[i][j][0] + image_array0[i][j][1] + image_array0[i][j][2] > BRIGHTNESS_THRESHOLD:
                pass
                brightpixels[nextValue, 0] = np.array([i,j])
                #brightpixels0.append([i,j])
            if image_array1[i][j][0] + image_array1[i][j][1] + image_array1[i][j][2] > BRIGHTNESS_THRESHOLD:
                pass
                brightpixels[nextValue, 1] = np.array([i,j])
                #brightpixels1.append([i,j])
            """
    #print(brightpixels0)
    #print(" - GAP - ")
    #print(brightpixels1)
    
    #print(image_array)
    #timer += 1
    old_image_array0 = image_array0
    old_image_array1 = image_array1
 
    #time.sleep(2)
    #picam0.capture_file(str(timer) + "-0.jpg")
    #picam1.capture_file(str(timer) + "-1.jpg")


times = []
timesSum = 0
testNumber = 150

if __name__ == "__main__":
    
    while time.time_ns() < start_time + 599000000000:
        run_recognition()
        #print('recognition ran')
    """for i in range(0, testNumber):
        time1 = time.time_ns()
        run_recognition()
        time2 = time.time_ns()
        print((time2-time1)/1000000000)
        times.append((time2-time1)/1000000000)
    times.sort()
    for i in range(0,testNumber):
        timesSum += times[i]
    print(MP_count)
    print("MEAN - ")
    print(timesSum/(testNumber+1))
    print("MIN - ")
    print(times[0])
    print("MAX - ")
    print(times[testNumber-1])
    print("MEDIAN - ")
    print(times[testNumber//2])
    print("FPS - ")
    print(1/(timesSum/(testNumber+1)))
    print(" ---------------------- ")
    print(timesSum/(testNumber+1))
    print(times[0])
    print(times[testNumber-1])
    print(times[testNumber//2])"""
    pwm.stop()  # Stop PWM
    GPIO.cleanup()  # Clean up GPIO settings
    
    
