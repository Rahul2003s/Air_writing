import pandas as pd
import numpy as np
from keras.models import load_model
import scipy.stats as stats
import time
import csv
import busio
import adafruit_adxl34x
import math

fs=20
frame_size=fs*10
hop_size=fs*2

def get_frames(df,frame_size,hop_size):
    N_FEATURES=3
    
    frames=[]
    lables=[]
    for i in range(0,len(df)-frame_size,hop_size):
        x=df['x-axis'].values[i: i+frame_size]
        y=df['y-axis'].values[i: i+frame_size]
        z=df['z-axis'].values[i: i+frame_size]   
        
        lable = stats.mode(df['number'][i: i+frame_size])[0][0]
        frames.append([x,y,z])
        lables.append(lable)
    frames=np.asarray(frames).reshape(-1,frame_size,N_FEATURES)
    lables=np.asarray(lables)
    
    return frames ,lables
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
    
    c=0
    data_points = list()
    print("Double tap the pen to start reading..")
    fields=['x-axis','y-axis','z-axis','number']
    csv_file=open('test.csv','w')
    writer = csv.DictWriter(csv_file, fieldnames = fields) 
    while True:
        if ac.events['tap']:
            print("Reading input for 2 sec!!..") 
            t_end = time.time() + 2
            while time.time() < t_end: #records input for 1.5 seconds
                read_data(ac.acceleration,1,data_points)
            data=write_data(data_points)
            c=c+1
            # write_csv(data, writer)
            for i in data:
                writer.writerow(i)
            data=[]
            if(c>=1):
                break
    model=load_model('fmodel.h5',compile=False)
    model.compile(optimizer=Adam(learning_rate = 0.0005), loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
    
    
    df=pd.read_csv('test.csv')
    df.to_csv('test.csv',mode='w',header=None,index=False)

    df=pd.read_csv('test.csv')
    df.columns=['x-axis','y-axis','z-axis','number']

    X_x,Y_y=get_frames(df,frame_size,hop_size)

    s=list(X_x.shape)
    X_X=X_x.reshape(X_x[0],X_x[1],X_x[2],1)

    p=model.predict(X_x[0])
    a=max((p.max(axis=0)))
    print("MAX",a)
    print("Predicted values\n",p)
    s=np.where(p==a)#index of the max 
    #print(X_test[:1])
    l=list(s)
    print("Predected number is: ",int(l[1]))
