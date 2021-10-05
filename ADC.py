import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

import threading
import time
import RPi.GPIO as GPIO


# toggle button
toggle_btn = 16
# sampling rates
samp_rates = [1, 5, 10]
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
# create an analog input channel on pin 1,2 (CH1,CH2)
chan1 = AnalogIn(mcp, MCP.P1) # Termistor 
chan2 = AnalogIn(mcp, MCP.P2) # LDR

# readings variables 
temp_ADC = -1
temp_v_out = -1
LDR_ADC = -1


# Setup pins
def setup():
  # Setup board mode
  GPIO.setmode(GPIO.BOARD)
  
  GPIO.setup(toggle_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  # Setup debouncing and callbacks
  GPIO.add_event_detect(toggle_btn,GPIO.FALLING,callback=toggle,bouncetime=200)
  pass

# toggle sampling rate
def toggle():
  # cycle thru the list of sampling rates in asc order
  
  pass
 
# temparature conversion
def to_temp(voltage):
  # Vout = Tc*Ta + V0c (SENSOR TRANSFER FUNCTION)
  # Vout = chan1.voltage
  # Sensor: MCP9700 
  v_0c = 0.5 # Sensor Output Voltage at 0 degree C
  t_c = 0.01 # Temperature Coefficient
  t_a = (voltage-v_0c)/t_c # ambient temperature 
  return t_a

# print sensor readings
def print_readings():
  
  thread = threading.Timer(5.0, print_readings)
  thread.daemon = True  # Daemon threads exit when the program does
  thread.start()
  read_sensors()
  print(datetime.datetime.now())
  #print("Runtime Temp Reading Temp Light Reading")
  print("{}   {}   {}", temp_ADC, to_temp(temp_v_out), LDR_ADC)

def read_sensors():
  # read from sensors
  temp_ADC = chan1.value
  temp_v_out = chan1.voltage
  LDR_ADC = chan2.value
  pass


if __main__ == "__main__":
  try:
    # this
    print_readings() # call it once to start the thread
    
    # Tell our program to run indefinitely
    while True:
        pass
  except Exception as e:
    print(e)
  finally:
    # that

print("Raw ADC Value: ", chan1.value)
print("ADC Voltage: " + str(chan1.voltage) + "V")
