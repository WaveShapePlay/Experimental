import serial

ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)

def turnOnLED():
    
    ser.write(b'o')

def turnOffLED():
    ser.write(b'x')
    
while(1):

    userInput = input('Type "On" to turn on LED "Off" to turn off LED\n')
# This is a good start, but makeing a GUI is better and has the build in error
# checking if deigned well.
    if userInput == 'On':
        turnOnLED()

    if userInput == 'Off':
        turnOffLED()

