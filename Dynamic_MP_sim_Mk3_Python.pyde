"""
Bounce.
When the shape hits the edge of the window, it reverses its direction.
"""

# Half width of the shape.
Radius = 60

# Speed of the shape.
XSpeed = 2.8
YSpeed = 2.2

# Starting position of shape.
xpos = 0
ypos = 0

# Left to Right.
xdirection = 1

# Top to Bottom.
ydirection = 1












adjust = 60
topAdjust = 60

extraAdjust = 1

time = 0
totalTopEnd = 0
totalBotEnd = 0
    
mpArr = [ [0,0,True, [50,50,50]]]
riverLength = 1500


def setup():
    size(1535, 860)
    global xpos, ypos, time, riverLength, mpLevelTOP, pastLevelTOP, mpLevelBOT, pastLevelBOT, topAdjust, adjust, extraAdjust, mpArr
    noStroke()
    frameRate(30)
    ellipseMode(RADIUS)
    # Set the starting position of the shape.
    xpos = width / 2
    ypos = height / 2


def draw():
    global xpos, ypos, xdirection, ydirection, time, riverLength, mpLevelTOP, pastLevelTOP, mpLevelBOT, pastLevelBOT, topAdjust, adjust, extraAdjust, mpArr, totalTopEnd, totalBotEnd
    time = time+1

    background(220)
    stroke(0)
    strokeWeight(8)
    
    line(-20, 404+topAdjust, 2000, 404+topAdjust)
    
    noStroke()
    
    fill(69, 91, 255)
    rect(100, 300+topAdjust, riverLength, 100)
    
    
    strokeWeight(2)
    stroke(0,0,0)
    
    
    mpLevelTOP = 0 
    pastLevelTOP = 0
    mpLevelBOT = 0 
    pastLevelBOT = 0

    
    for iter in range(0, riverLength):
        #print("hello world 2.0!")
        for ja in range(0, len(mpArr)):
            
            i = riverLength - iter
            j = len(mpArr) - ja -1
            #print(i)
            if abs(mpArr[j][0] - i) < 12  and mpArr[j][1] < 400+topAdjust and mpArr[j][2] is True:
                mpLevelTOP -= 10*extraAdjust
            elif abs(mpArr[j][0] - i) < 12 and mpArr[j][1] > 400+topAdjust and mpArr[j][2] is True:
                mpLevelBOT -= 10*extraAdjust
        if mpLevelTOP*extraAdjust < -260 or mpLevelBOT*extraAdjust < -260:
            extraAdjust *= 0.96
        
        strokeWeight(1)
        line(i+1, extraAdjust*(pastLevelTOP)+300+topAdjust, i, extraAdjust*(mpLevelTOP)+300+topAdjust)
        line(i+1, extraAdjust*(pastLevelBOT)+700+adjust, i, extraAdjust*(mpLevelBOT)+700+adjust)
        if i == 101:
            totalTopEnd += mpLevelTOP
            totalBotEnd += mpLevelBOT
        pastLevelTOP = mpLevelTOP
        pastLevelBOT = mpLevelBOT
        
        mpLevelTOP = 0
        mpLevelBOT = 0
    
    for i in range(len(mpArr)):
        
        stroke(mpArr[i][3][0],mpArr[i][3][1],mpArr[i][3][2])
        strokeWeight(2)
        if mpArr[i][2] == True:
            point(mpArr[i][0], mpArr[i][1])
        mpArr[i][0]-=0.5
        
        if mpArr[i][0] % (riverLength/10) < 1 and random(0,1) < 0.724 and mpArr[i][1] < 400+topAdjust:
            mpArr[i][2] = False
            
    for i in range (0,4):
        mpArr.append([random(110, riverLength), random(310+topAdjust,390+topAdjust), True, [random(0,255),random(0,255),random(0,255)]])
    noStroke()

    fill(69, 91, 255)
    rect(100, 700+adjust, riverLength, 100)
    
    strokeWeight(2)
    stroke(0,0,0)

    mpLevel = 0
    
    for i in range(0, len(mpArr)):
        if mpArr[i][0] < 0:
            pass
            #mpArr.pop(i)
        stroke(mpArr[i][3][0],mpArr[i][3][1],mpArr[i][3][2])
        strokeWeight(2)
        if mpArr[i][2]:
            point(mpArr[i][0], mpArr[i][1])
        mpArr[i][0]-=0.5
        
    for i in range (0,4):
        mpArr.append([random(110, riverLength), random(710+adjust,790+adjust), True, [random(0,255),random(0,255),random(0,255)]])
    
    # Update the position of the shape.
    
