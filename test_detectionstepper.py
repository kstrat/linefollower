import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)                            #Right sensor connection
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Left sensor connection
while True:
  y=GPIO.input(3)                         #Reading output of right IR sensor
  j=GPIO.input(37)                        #Reading output of left IR sensor
  if j==1:                                #Right IR sensor detects an object
    print("Obstacle detected on Left"),i
halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

for i in range(512):
  for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
    time.sleep(0.001)

  time.sleep(0.1)
  if y==1:                              #Left IR sensor detects an object
    print("Obstacle detected on Right"),j
halfstep_seq = [
  [1,0,0,1],
  [0,0,0,1],
  [0,0,1,1],
  [0,0,1,0],
  [0,1,1,0],
  [0,1,0,0],
  [1,1,0,0],
  [1,0,0,0]
]

for i in range(512):
  for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
    time.sleep(0.001)
  time.sleep(0.1)

GPIO.setmode(GPIO.BOARD)

control_pins = [12,16,18,22]

for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)



GPIO.cleanup()

