# Ultrasonic Ranger Radar

This project is a radar system that utilizes an ultrasonic sensor and a servo motor to scan the surroundings. The radar system is controlled using C# and Python for data processing and visualization. The ultrasonic sensor measures the distance of objects, and the servo motor sweeps the sensor to create a 2D map of the environment using the pygame drawing library.

## Features

• Distance Measurement: Use an ultrasonic sensor to measure the distance to nearby objects. <br>
• Scanning: A servo motor rotates the sensor to scan the surroundings. <br>
• Data Visualization: Display the detected distances in a visual radar-style graph. <br>
• Multi-Language Support: C# for device control and Python for visualization. <br>

## Requirements

### Hardware

For this project, I've used the Grove Ecosystem, so all the hardware/software corresponds to it. It is possible to avoid using the grove ecosystem, although the c# script won't be adapted to such hardware.

• Computer (for running Python scripts for visualization) <br>
• Arduino UNO with USB-B cable <br>
• Arduino Grove base hat <br>
• Ultrasonic Sensor (e.g. Grove - Ultrasonic Ranger) <br>
• Servo Motor (e.g. Grove - Servo) <br> 
• Grove - Universal 4 Pin Cables <br>

### Software

• Code editor (e.g. VS Code) <br>
• Arduino IDE <br>
• Python 3.x <br>
• C# <br>
• pyserial module <br>
• pygame module <br>
• Grove Servo library <br>
• Grove Ultrasonic Ranger Library <br>

## Usage

The arduino communicates its recorded data through the COM3 serial port to the computer. <br>

To start the program, upload the .ino script to the arduino and then close the IDE. Otherwise, the python script cannot read from the COM3 serial port as it is being used by an other program.
Next, run the python script on your computer and a window with a radar interface should appear (note that there is a 2 seconds cooldown to setup the ultrasonic ranger at exactly 0 degrees).

Finally, enjoy your radar.

## Program

You can manually change the detection range of the ultrasonic ranger. To do so, go to the visualization.py file and change the detection_range var to whatever you want.

## Contributing
Feel free to open issues or create pull requests to suggest improvements!

## License
This project is licensed under the MIT License. See the LICENSE file for details.
