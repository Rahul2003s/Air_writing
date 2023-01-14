import time
import board
import csv
import busio
import adafruit_adxl34x
#(0.0784532, -0.1176798, 8.8652116) 


def read_data(cordinates,number,list):
    x,y,z=cordinates
    d=dict()
    d['x-axis']= "%0.7f" % x
    d['y-axis']= "%0.7f" % y
    d['z-axis']= "%0.7f" % z 
    d['number']=number
    list.append(d)
    # writer.writerow(d)
    
def write_data(l):
    n=len(l)
    seen = set()
    new_l = [] 
    for d in l:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_l.append(d)
    for i in new_l:
        print(i)
    print("len",len(new_l))
    return new_l

    # print("LEN:",n)
    # for i in range(1,n):
    #     # print(i)
    #     if((l[i-1]['x-axis']==l[i]['x-axis']) and (l[i-1]['y-axis']==l[i]['y-axis']) and (l[i-1]['z-axis']==l[i]['z-axis'])):
    #         print(i)
    #         print(l[i])
    #         del l[i]

def write_csv(l,writer):
    for i in l:
        writer.writerow(d)

if __name__ == '__main__':    
    i2c=busio.I2C(board.SCL, board.SDA)
    ac=adafruit_adxl34x.ADXL345(i2c)
    ac.enable_motion_detection(threshold=18)
    ac.enable_tap_detection(tap_count=2,threshold=200,duration=50,latency=20,window=255)
    
    fields=['x-axis','y-axis','z-axis','number']
    csv_file=open('data.csv','w')
    writer = csv.DictWriter(csv_file, fieldnames = fields) 
    writer.writeheader() 
     
    data_points = list()
    n = int(input("Enter the number to train: "))
    print("Training data set for 10 times!!!...")
    print("Double tap the pen to start reading..")
    num=0
    while True:
        if ac.events['tap']:
            print("Reading input for 1.5 sec!!..")
            t_end = time.time() + 1.5
            count=0
            while time.time() < t_end: #records input for 1.5 seconds
                # print(ac.acceleration)
                read_data(ac.acceleration,n,data_points)
                count += 1
            data=write_data(data_points)
            write_csv(data, writer)
            data=[]
            data_points=[]
            print("Done",count)