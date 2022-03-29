import serial
import os

moniter = '/dev/ttyACM0'

moniter = serial.Serial(moniter)
moniter.flushInput()

while True:
    try:
        data = moniter.readline()
        decoded_data = data.decode('utf-8').strip()
        print(decoded_data)
        if decoded_data != '0':

            if decoded_data == "BC43FF00": # play / pause 
                os.system('xdotool key XF86AudioPlay')
            
            elif decoded_data == "EA15FF00": # Increase volume
                os.system('xdotool key XF86AudioRaiseVolume')
            
            elif decoded_data == "F807FF00": # Reduce volume
                os.system('xdotool key XF86AudioLowerVolume')
    except:
        print("Keyboard Interrupt")
        break
