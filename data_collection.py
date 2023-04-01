import time
# import board
import csv
import busio
import adafruit_adxl34x
import math
#(0.0784532, -0.1176798, 8.8652116) 

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
    ac.enable_tap_detection(tap_count=2,threshold=200,duration=50,latency=20,window=255)
    
   
    # writer.writeheader() 
    data_points = list()
    n = int(input("Enter the number to train: "))
    print("Training data set for 10 times!!!...")
    print("Double tap the pen to start reading..")
    c=0
    fields=['x-axis','y-axis','z-axis','number']
    f='./source/'+str(n)+'.csv'
    print(f)
    csv_file=open(f,'a+')
    writer = csv.DictWriter(csv_file, fieldnames = fields) 
    while True:
        if ac.events['tap']:
            print("Reading input for 2 sec!!..") 
            t_end = time.time() + 2
            while time.time() < t_end: #records input for 1.5 seconds
                read_data(ac.acceleration,n,data_points)
            p=input("Add to dataset ['y'/'n'/'q']: ")
            if p=="y":
                data=write_data(data_points)
                c=c+1
                # write_csv(data, writer)
                for i in data:
                    writer.writerow(i)
                
            elif p=="q":
                break
            elif p=="n":
                c=c
            data=[]
            if(c>10):
                break
            print("count",c)


