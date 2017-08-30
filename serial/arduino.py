import serial
import time
arduino = serial.Serial('COM3',115200, timeout=.1) # connect to COM port with the specified baud rate
time.sleep(1) # wait for a second until the connection established
while True:
  data = arduino.readline()[:-2] # read one line from the serial at a time and get rid of the end of line character
  if data:
    print(data.decode()) # convert binary to string