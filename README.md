# Air_writing


## Installation

1. Install my-project with npm
```bash
  apt-get update && apt-get upgrade -y
  sudo raspi-config
```
2. raspi-config > Interface Options > I2C > Yes
3. reboot
```bash
    sudo reboot
```
4. Installing python
```bash
    sudo apt-get install python3-dev python3-pip python3-smbus i2c-tools -y
```
5. Check the ADXL345 working :  “53“
```bash
    sudo i2cdetect -y 1
```
6. Installing python pakages
```
    sudo pip3 install adafruit-circuitpython-ADXL34x
```
