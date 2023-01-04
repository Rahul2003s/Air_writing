import time
import board
import csv
import busio
import adafruit_adxl34x
#(0.0784532, -0.1176798, 8.8652116) 


def write_data(cordinates,number,writer):
    x,y,z=cordinates
    d=dict()
    d['x-axis']=x
    d['y-axis']=y
    d['z-axis']=z 
    d['number']=number
    writer.writerow(mydict)
    
    
    
if __name__ == '__main__':    
    i2c=busio.I2C(board.SCL, board.SDA)
    ac=adafruit_adxl34x.ADXL345(i2c)
    ac.enable_motion_detection(threshold=18)
    ac.enable_tap_detection(tap_count=2,threshold=200,duration=50,latency=20,window=255)
    
    fields=['x-axis','y-axis','z-axis','number']
    csv_file=open('data.csv','w')
    writer = csv.DictWriter(csv_file, fieldnames = fields) 
    writer.writeheader() 
     
    print("Training data set!!!...")
    while True:
        n=int(input("Enter the number (0-9):"))
        if n>=0 and n<10:
            print("Double tap the pen to start reading..")
            if ac.events['tap']:
                print("Reading input for 3 sec!!..")
                t_end = time.time() + 2 
                count=0
                while time.time() < t_end: #records input for 2 seconds
                    print(ac.acceleration)
                    write_data(ac.acceleration,n,data_csv)
                    count += 1
                print("Done",count)