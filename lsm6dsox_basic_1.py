# LSM9DS1 Gyro example.
import time
from lsm6dsox import LSM6DSOX

#WIP
#ImportError: no module named 'lsm6dsox'

#LSM6DSOXTR 6-axis IMU
#This 6-axis IMU allows to obtain 3D gyroscopic and 3D accelerometer data. It is also possible to do machine learning on the IMU for gesture detection, offloading computation load from the main processor.

from machine import Pin, I2C
lsm = LSM6DSOX(I2C(0, scl=Pin(13), sda=Pin(12)))

while (True):
    print('Accelerometer: x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}'.format(*lsm.read_accel()))
    print('Gyroscope:     x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}'.format(*lsm.read_gyro()))
    print("")
    time.sleep_ms(100)
