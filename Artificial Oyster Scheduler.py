import time

from machine import Pin, PWM, ADC

device_on = 0
device_off = 1

# create an output pin on pin #0
#read_pin = ADC(Pin(26, pull=machine.Pin.PULL_DOWN))
receive_servo_command_pin = machine.Pin(22, machine.Pin.IN, pull=machine.Pin.PULL_DOWN)
power_switch_pin = machine.Pin(19, machine.Pin.OUT)
servo_pin = machine.Pin(5)
servo_pwm = PWM(servo_pin)

servo_pwm.freq(50)

max_duty = 7864
min_duty = 1802
filter_water = int(max_duty/2)+1700
through_water = max_duty-100

spin_time = 0.5

filtering_water = False #read with question mark at end of variable name

wait_time = 1000000000

water_filter_start_time = 0

over_time = 0



def check_and_wait():
    global water_filter_start_time, wait_time, filter_water, through_water, filtering_water, receive_servo_command_pin
    t_start = time.time_ns()
    if receive_servo_command_pin.value() == True:
        servo_pwm.duty_u16(filter_water)
        filtering_water = True
        water_filter_start_time = time.time_ns()
        #time.sleep(spin_time)
        #servo_pwm.duty_u16(through_water)
        #time.sleep(spin_time)
    else:
        if time.time_ns() > water_filter_start_time + wait_time:
            servo_pwm.duty_u16(through_water)
        t_end = time.time_ns()
        if 0.001-((t_end-t_start)/1000000000) > 0:
            time.sleep(0.001-((t_end-t_start)/1000000000))
        
        
while True:
    """servo_pwm.duty_u16(filter_water)
    time.sleep(spin_time)
    servo_pwm.duty_u16(through_water)
    time.sleep(spin_time)"""
    #check_and_wait()
    power_switch_pin.off()
    print("off")
    time.sleep(1)
    power_switch_pin.on()
    print("on")
    time.sleep(1)
    #if receive_servo_command_pin.value() == 0:


#time.sleep(1)


#p0.value(device_on)

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

