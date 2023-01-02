import time
import board
import busio
import adafruit_adxl34x
#(0.0784532, -0.1176798, 8.8652116)
i2c=busio.I2C(board.SCL, board.SDA)
ac=adafruit_adxl34x.ADXL345(i2c)
ac.enable_motion_detection(threshold=18)
ac.enable_tap_detection(tap_count=3,threshold=20,duration=50,latency=20,window=255)
while True:
#	print("tap: ",ac.events['tap'])
#	print("motion:",ac.events['motion'])
#	print("acceleration: ",ac.acceleration)
	if ac.events['tap']:
     	print("Reading input for 3 sec!!..")
		print("acceleration: %f %f %f "%ac.acceleration)
	time.sleep(0.5)

