import pandas as pd
import numpy as np
from keras.models import load_model
import scipy.stats as stats

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

model=load_model('fmodel.h5')
l=['test.csv']
for file in l:
    df=pd.read_csv(file)
    df.to_csv('test1.csv',mode='w',header=None,index=False)

df=pd.read_csv('test1.csv')
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