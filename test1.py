import time
# import board
import pandas as pd
import csv
import busio
import adafruit_adxl34x
import math

def read_data(cordinates,number,li):
    x,y,z=cordinates
    d=dict()
    xx="%0.7f" % x
    yy="%0.7f" % y
    zz="%0.7f" % z
    # math.trunc(float(xx)*100)
    d['x-axis']=float(xx)
    d['y-axis']=float(yy)
    d['z-axis']=float(zz)
    d['number']=number
    li.append(d)


def write_data(l):
    n=len(l)
    seen = set()
    new_l = [] 
    for d in l:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_l.append(d)
    
    print("len",len(new_l))
    return new_l

if __name__ == '__main__':    
    i2c=busio.I2C(3, 2)# use GPIO3 (SCL) and GPIO2 (SDA)
    ac=adafruit_adxl34x.ADXL345(i2c)
    ac.enable_motion_detection(threshold=18)
    ac.data_rate = adafruit_adxl34x.DataRate.RATE_5_HZ
    ac.range = adafruit_adxl34x.Range.RANGE_16_G

    ac.enable_tap_detection(tap_count=2,threshold=200,duration=50,latency=20,window=255)
    c=0
    
    data_points=[]
    while True:
        if ac.events['tap']:
            print("Reading input for 2 sec!!..") 
            t_end = time.time() + 2
            c=c+1
            while time.time() < t_end: #records input for 1.5 seconds
                read_data(ac.acceleration,2,data_points)
            
            data=write_data(data_points)
            if(c==1):
                break
    print(data)
    df=pd.DataFrame(data)
    df.to_csv('test.csv',mode='w',header=None,index=False)