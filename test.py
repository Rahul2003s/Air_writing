import pandas as pd
import numpy as np
from keras.models import load_model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import Sequential
import scipy.stats as stats
import time
import csv
import busio
import adafruit_adxl34x
import math

fs = 20
frame_size = fs*10
hop_size = fs*2


def get_frames(df, frame_size, hop_size):
    N_FEATURES = 3
    frames = []
    lables = []
    for i in range(0, len(df)-frame_size, hop_size):
        x = df['x-axis'].values[i: i+frame_size]
        y = df['y-axis'].values[i: i+frame_size]
        z = df['z-axis'].values[i: i+frame_size]

        lable = stats.mode(df['number'][i: i+frame_size])[0][0]
        frames.append([x, y, z])
        lables.append(lable)
    frames = np.asarray(frames).reshape(-1, frame_size, N_FEATURES)
    lables = np.asarray(lables)

    return frames, lables


if __name__ == '__main__':

    i2c = busio.I2C(3, 2)  # use GPIO3 (SCL) and GPIO2 (SDA)
    ac = adafruit_adxl34x.ADXL345(i2c)
    ac.enable_motion_detection(threshold=18)
    ac.enable_tap_detection(tap_count=2, threshold=200,
                            duration=50, latency=20, window=255)

    c = 0
    df = pd.DataFrame(columns=['x-axis', 'y-axis', 'z-axis', 'number'])
    print("Double tap the pen to start reading..")
    while True:
        if ac.events['tap']:
            print("Reading input for 2 sec!!..")
            t_end = time.time() + 2
            while time.time() < t_end:  # records input for 1.5 seconds
                x, y, z = ac.acceleration
                xx = "%0.7f" % x
                yy = "%0.7f" % y
                zz = "%0.7f" % z
                df.loc[len(df.index), :] = [xx, yy, zz, 0]
            c = c+1
            print(".......")
            if(c >= 1):
                break

    model = load_model('tuned.h5', compile=False)
    model.compile(optimizer=Adam(learning_rate=0.0005),
                  loss='sparse_categorical_crossentropy', metrics=['accuracy'], run_eagerly=True)

    df = df.astype(float)

    X_x, Y_y = get_frames(df, frame_size, hop_size)
    s = list(X_x.shape)
    X_X = X_x.reshape(s[0], s[1], s[2], 1)

    p = model.predict(X_X)
    a = max((p.max(axis=0)))
    print("MAX", a)
    print("Predicted values\n", p)
    s = np.where(p == a)  # index of the max

    l = list(s)
    print("Predected number is: ", int(l[1]))
