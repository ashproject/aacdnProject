import RPi.GPIO as GPIO

def cyanOn():

  GPIO.setmode(GPIO.BCM)
  
  RED = 17
  GREEN = 18
  BLUE = 27
  GPIO.setup(RED,GPIO.OUT)
  GPIO.setup(GREEN,GPIO.OUT)
  GPIO.setup(BLUE,GPIO.OUT)
  GPIO.output(RED,GPIO.HIGH)
  GPIO.output(GREEN,GPIO.LOW)
  GPIO.output(BLUE,GPIO.LOW)
  
if __name__ == "__main__":
  cyanOn()