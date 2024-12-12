from picamera2 import Picamera2, Preview
import time
import numpy as np
from PIL import Image
import cython

BRIGHTNESS_THRESHOLD = 240

STARTX = 29
ENDX = 54

timer = 0

RESOLUTION_WIDTH = 83
RESOLUTION_HEIGHT = 64

old_image_array0 = []
old_image_array1 = []

picam0 = Picamera2(0)
picam1 = Picamera2(1)


#picam0.set_controls({"AeMode": 0, "AwbMode": 0, "AfMode": 0})
#picam1.set_controls({"AeMode": 0, "AwbMode": 0, "AfMode": 0})




camera_config0 = picam0.create_still_configuration(
    main={"size": (RESOLUTION_WIDTH, RESOLUTION_HEIGHT)}, 
    lores={"size": (RESOLUTION_WIDTH, RESOLUTION_HEIGHT)}, 
    raw={"size": (26, 20)}, 
    display="lores",
    buffer_count=25
    )
camera_config1 = picam1.create_still_configuration(
    main={"size": (RESOLUTION_WIDTH, RESOLUTION_HEIGHT)}, 
    lores={"size": (RESOLUTION_WIDTH, RESOLUTION_HEIGHT)}, 
    raw={"size": (26, 20)}, 
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

picam0.set_controls({'ExposureTime': 3500})#need 4000
picam1.set_controls({'ExposureTime': 3500})
picam0.set_controls({"AeEnable": 0, "AwbEnable": 0, "FrameRate": 200})
picam1.set_controls({"AeEnable": 0, "AwbEnable": 0, "FrameRate": 200})

time.sleep(4)

#def averageSquare(x, y, radius, array):
    #valueSum = 0
    #for x in range(0,radius):
        

def run_recognition():
    
    image_array0 = picam0.capture_array()
    image_array1 = picam1.capture_array()

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
    
    brightpixels0 = []
    brightpixels1 = []
    """
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
                brightpixels0.append([i,j])
            if image_array1[i][j][0] + image_array1[i][j][1] + image_array1[i][j][2] > BRIGHTNESS_THRESHOLD:
                brightpixels1.append([i,j])
            
    #print(brightpixels0)
    #print(" - GAP - ")
    #print(brightpixels1)
    
    #print(image_array)
    
    
    old_image_array0 = image_array0
    old_image_array1 = image_array1
    
    #time.sleep(2)
    #picam0.capture_file("test0.jpg")
    #picam1.capture_file("test1.jpg")


times = []
timesSum = 0
testNumber = 49

if __name__ == "__main__":
    for i in range(0, testNumber):
        time1 = time.time_ns()
        run_recognition()
        time2 = time.time_ns()
        print((time2-time1)/1000000000)
        times.append((time2-time1)/1000000000)
    times.sort()
    for i in range(0,testNumber):
        timesSum += times[i]
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
    print(times[testNumber//2])
    pass
    
