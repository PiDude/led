import RPi.GPIO as GPIO
import time

# use GPIO numbering
GPIO.setmode(GPIO.BCM)

#setting up GPIO for LED segments
segments = (4,17,27,22,18,23,24)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, False)



#setting up the GPIO to ingnite motor
fire = 7
GPIO.setup(fire, GPIO.OUT)
GPIO.output(fire, False)


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


# this is the backwards array starting at 5, ending at 0
array=[1,0,1,1,0,1,1],[0,1,1,0,0,1,1],[1,1,1,1,0,0,1],[1,1,0,1,1,0,1],[0,1,1,0,0,0,0],[1,1,1,1,1,1,0]

# this is the forward array
#array=[1,1,1,1,1,1,1],[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1]

#countdown from 5 to 0.
#when at 0 (x=5), then fire launch GPIO
for x in range(0,6):

    GPIO.output(4, array[x][0])
    GPIO.output(17, array[x][1])
    GPIO.output(27, array[x][2])
    GPIO.output(22, array[x][3])
    GPIO.output(18, array[x][4])
    GPIO.output(23, array[x][5])
    GPIO.output(24, array[x][6])


    if x == 5:
        for y in range(0,1):
            GPIO.output(fire, True)
            time.sleep(0.8)

    time.sleep(0.8)

#turn all GPIO off
for segment in segments:
    GPIO.output(segment, False)

GPIO.output(fire, False)


GPIO.cleanup()


#for x in range(0,10):

#try:

#    while True:

#except KeyboardInterrupt:
#    GPIO.cleanup()




