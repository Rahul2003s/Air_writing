# Air_writing


## Installation

1. update and upgrade raspberrypi
```bash
  sudo apt-get update && apt-get upgrade -y
  
```
2. install 
```bash
```
3. 
```bash

```
4. 
```bash
   
```
5. 
```bash
    
```
6. Installing python pakages
```
    sudo raspi-config
    raspi-config > Interface Options > I2C > Yes
    sudo reboot
    sudo apt-get install python3-dev python3-pip python3-smbus i2c-tools -y
    Check the ADXL345 working :  “53“
    sudo i2cdetect -y 1
    sudo pip3 install adafruit-circuitpython-ADXL34x
```



    sudo apt update
    sudo apt full-upgrade
Check python version: python -V
Check available .whl's here https://github.com/PINTO0309/Tensorfl...
Be sure to match your python version and architecture

**Use pyenv if you need a different python version - LINK TO PYENV TUTORIAL:   

 • Install Multiple ...   

2:45   2. Make your project directory:
cd Desktop
mkdir project
cd project

3:00   3. Make a virtual environment:
python3 -m pip install virtualenv
python3 -m virtualenv env
source env/bin/activate

3:34   4. Run the commands from https://github.com/PINTO0309/Tensorfl...
sudo apt-get install -y libhdf5-dev libc-ares-dev libeigen3-dev gcc gfortran libgfortran5 libatlas3-base libatlas-base-dev libopenblas-dev libopenblas-base libblas-dev liblapack-dev cython3 libatlas-base-dev openmpi-bin libopenmpi-dev python3-dev
pip install -U wheel mock six

3:58   5. Select the .whl from https://github.com/PINTO0309/Tensorfl...
Select "view raw" then copy the URL
Run:
wget [Raw file URL]
sudo chmod +x [Raw file URL]
./[Tensorflow file]
sudo pip uninstall tensorflow
pip uninstall tensorflow
pip install  tensorflow-[Your version here].whl

6:00   6. Restart the shell
exec $SHELL

6:11   7. Reactivate your virtual environment:
cd Desktop
cd project
source env/bin/activate

6:24   8. Test:
python 
import tensorflow
tensorflow.__version__
quit()

6:55   9. (optional) If there's an hdf5 warning run this command:
This is from: https://docs.h5py.org/en/stable/build... 
pip uninstall h5py
HDF5_VERSION=[Desired version] pip install --no-binary=h5py h5py==3.1.0