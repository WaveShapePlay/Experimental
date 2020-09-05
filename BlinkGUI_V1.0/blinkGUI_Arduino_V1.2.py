import serial
from tkinter import *
import tkinter as tk
import time 
ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)

def turnOnLED():
    ser.write(b'o')

def turnOffLED():
    ser.write(b'x')

def blinkLED():
    ser.write(b'b')
    time.sleep(1)
    delay = entry_Blink.get()
    ser.write(delay.encode())
    print(entry_Blink.get())
    

# creating tkinter window 
root = Tk() 
root.title('Blink GUI')

btn_On= tk.Button(root, text="Turn ON", command=turnOnLED)
btn_On.grid(row=0, column=0)

btn_Off = tk.Button(root, text="Turn Off", command=turnOffLED)
btn_Off.grid(row=0, column=1)

btn_Blink = tk.Button(root, text="Blink", command=blinkLED)
btn_Blink.grid(row=1, column=0)

entry_Blink = Entry(root)
entry_Blink.grid(row = 1, column=1)

root.geometry("350x350")
