import time
import board
import csv
import adafruit_adxl34x
#(0.0784532, -0.1176798, 8.8652116) 


def write_data(cordinates,number):
    x,y,z=cordinates
    return x
if __name__ == '__main__':    
    i2c=busio.I2C(board.SCL, board.SDA)
    ac=adafruit_adxl34x.ADXL345(i2c)
    ac.enable_motion_detection(threshold=18)
    ac.enable_tap_detection(tap_count=2,threshold=20,duration=50,latency=20,window=255)
    while True:
        if ac.events['tap']:
            print("Reading input for 3 sec!!..")
            x,y,z=ac.acceleration
            t_end = time.time() + 2 
            count=0
            while time.time() < t_end: #records input for 2 seconds
                print(x,y,z)
                count += 1
            print("Done",count)