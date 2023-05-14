# Deep Learning Based AirWriting Digit Recognition Using Accelerometer

This project is aimed at recognizing digits that are air-written using accelerometer data and a deep learning-based model. The project uses the I2C communication protocol to gather data from an accelerometer (ADXL345), preprocesses it, and feeds it to a deep learning sequential model for training. The trained model is then used to recognize digits drawn in the air in real-time on a Raspberry Pi.



## Installation and Setup

1. Clone the project repository onto your local machine using the following command:

```bash
git clone https://github.com/Rahul2003s/Air_writing.git
```
2. Install the necessary dependencies for the project using the following command:

```bash
sudo apt-get update
sudo apt-get install python3-dev python3-pip python3-smbus i2c-tools -y
```

3. Enable I2C communication on the Raspberry Pi using the following commands:

```bash
sudo raspi-config
```

Navigate to **'Interface Options > I2C'** and select **'Yes'**. Then, reboot the Raspberry Pi using the following command:

```bash
sudo reboot
```

4. Check that the ADXL345 accelerometer is working correctly using the following command:
```bash
sudo i2cdetect -y 1
```
The output should show "53" in the grid.

5. Install the Adafruit CircuitPython ADXL34x library using the following command:
```bash
sudo pip3 install adafruit-circuitpython-ADXL34x
```

6. Install TensorFlow on the Raspberry Pi by following the steps outlined in this [blog post](https://medium.com/@rahulsri073/installing-tensorflow-on-raspberry-pi-1b2c8d1ee33c).
7. Connect the ADXL345 accelerometer to the Raspberry Pi using the I2C communication protocol.
8. Run the data collection and preprocessing script to capture the data required for training the deep learning model. The script generates 2D frames or arrays of the accelerometer data, corresponding to the digits drawn in the air.
9. Train the deep learning sequential model using the generated data. The trained model is saved in a .h5 file, which is later used for real-time testing.
10. Load the trained model onto the Raspberry Pi for real-time testing of the digit recognition system.


## Usage
To use the digit recognition system, follow the steps below:

1. Run the real-time testing script on the Raspberry Pi.

2. Use your hand to draw a digit in the air. Ensure that the accelerometer is held firmly in your hand, and that the drawing is clear and distinct.

3. The digit recognition system will then recognize the digit and display the result on the screen.

## Contributing
If you find any bugs or issues with the project, feel free to submit a pull request or create an issue on the project repository. We welcome all contributions to the project.

