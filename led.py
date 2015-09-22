import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

segments = (4,17,27,22,18,23,24)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, False)


num = {'':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}


array=[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1]





for x in range(0,4):
    for y in range(0,7):
        GPIO.output(segments[x], array[x][y])
        time.sleep(0.1)


GPIO.cleanup()


#for x in range(0,10):

#try:

#    while True:

#except KeyboardInterrupt:
#    GPIO.cleanup()




