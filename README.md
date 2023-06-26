# MouseMoveHeart

> This is an Arduino project that emulates a mouse and moves in the shape of a heart.

[![Python](https://img.shields.io/badge/Python-3.9.1-blue.svg)](https://www.python.org/)
[![Arduino](https://img.shields.io/badge/Arduino-1.8.19-blue.svg)](https://www.arduino.cc/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

- [General Information](#general-information)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)
- [Idea Behind Project](#idea-behind-project)
- [License](#license)

## General Information

This project is Arduino-based and its main purpose is to emulate a mouse and draw the shape of a predefined function. In this case, the function represents a heart shape. This project serves as my first public Arduino project and is a step towards developing my programming skills and creating repositories.

## Technologies Used

- Python 3.9.1
- Arduino 1.8.19
- Mouse (by Arduino) 1.0.1

## Features

- Moves the mouse in the shape of a heart.

![MouseMoveHeart Demo](/images/20220418_154246.gif)

## Setup

To set up the project, you need to install the Cpp file included in the repository on 32u4 or SAMD micro-based boards such as Pro Micro, Leonardo, Esplora, Zero, Due, and MKR Family. Connect the board to your computer through its micro's native USB port.

## Usage

- Install the Cpp file onto the microcontroller and connect it to the computer via the USB port.
- Adjust the speed by editing the `delayTime` parameter in line 6 of the Cpp file:
  ```cpp
  #define delayTime 3
  ```
- Adjust the number of points by editing the `step` parameter in the `Map.py` file.

  **WARNING:** If any changes have been made in the `Map.py` file, it is necessary to copy the new map to the Cpp file and edit the `mapSize` parameter.

## Acknowledgements

- This project was inspired by a friend of mine who wanted to prevent her laptop from falling asleep.
- The heart function equation used in this project is based on Slawomir Chodnicki's article: [Plot the Shape of My Heart](https://towardsdatascience.com/plot-the-shape-of-my-heart-698d4776c51a).

## Idea Behind Project

The following link contains a GeoGebra model that shows the heart equation and the points that travel on it with an established step:
[Heart Equation GeoGebra Model](https://www.geogebra.org/calculator/evakcq4n)

The mouse in this project travels to the next points using a similar schematic.

![Heart Equation Schematic](/images/Geogebra.JPG)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Created by [@niewiaro](https://github.com/Niewiaro)  
For any inquiries, please contact me at niewiarowski.kuba@gmail.com.
