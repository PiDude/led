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


array=[1,1,1,1,1,1,1],[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1]





for x in range(6,0,-1):

    GPIO.output(4, array[x][0])
    GPIO.output(17, array[x][1])
    GPIO.output(27, array[x][2])
    GPIO.output(22, array[x][3])
    GPIO.output(18, array[x][4])
    GPIO.output(23, array[x][5])
    GPIO.output(24, array[x][6])
    time.sleep(1.5)


GPIO.cleanup()


#for x in range(0,10):

#try:

#    while True:

#except KeyboardInterrupt:
#    GPIO.cleanup()




