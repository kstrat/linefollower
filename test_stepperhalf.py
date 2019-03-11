import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

control_pinsright = [12,16,18,22]
control_pinsleft = [7,11,13,15]

for pin in control_pinsright:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

for pin in control_pinsleft:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

halfstep_seqright = [
  [1,0,0,1],
  [0,0,0,1],
  [0,0,1,1],
  [0,0,1,0],
  [0,1,1,0],
  [0,1,0,0],
  [1,1,0,0],
  [1,0,0,0]
]
halfstep_seqleft = [
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
      GPIO.output(control_pinsright[pin], halfstep_seqright[halfstep][pin])
      GPIO.output(control_pinsleft[pin], halfstep_seqleft[halfstep][pin])
    time.sleep(0.001)

GPIO.cleanup()

