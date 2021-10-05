import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# button
btn = 16

# sampling rates
samp_rate = [1, 5, 10]

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)


# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 1,2 (CH1,CH2)
chan1 = AnalogIn(mcp, MCP.P1) # Temp
chan2 = AnalogIn(mcp, MCP.P2) # LDR



print("Raw ADC Value: ", chan1.value)
print("ADC Voltage: " + str(chan1.voltage) + "V")
