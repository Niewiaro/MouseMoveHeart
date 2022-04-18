# MouseMoveHeart
> This is an Arduino project that emulate mouse and move in a shape of heart.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
* [Idea Behind Project](#idea-behind-project)

## General Information
- This project is Arduino based. Its main purpose is to emulate your mouse and draw shape of function that was implemented. In this case heart.
- It's my first public Arduino project. This is a step towards developing my programming habits and creating repositories.

## Technologies Used
- Python 3.9.1
- Arduino 1.8.19

## Features
- Move mouse in the shape of a heart.

## Setup
To setup project it is required to intstal on 32u4 or SAMD micro based boards (Pro Micro, Leonardo, Esplora, Zero, Due and MKR Family) an Cpp file included in repository. To control cursor movement it in needet to connect computer through their micro’s native USB port.

## Usage
- Install Cpp file into microcontroler and connect to computer via USB port.
- To adjust speed edit delayTime in 6 line.
`#define delayTime 3`
- To adjust number of points edit step parameter in Map.py file

WARNING
If any changes have been made in Map.py file it is nessesery to copy new map to Cpp file and edit mapSize parameter!

## Acknowledgements
- This project was inspired by friend of main who didn't want to her laptop fall asleep ;).
- This project was based on Slawomir Chodnicki Heart function equasion (https://towardsdatascience.com/plot-the-shape-of-my-heart-698d4776c51a).

## Idea Behind Project
https://www.geogebra.org/calculator/evakcq4n

This link contain Geogebra model that show Heart equation and points which travel on it with established step.

Simulary mouse travel to next points using this schematic.

![](/images/Geogebra.JPG)

## Contact
Created by [@niewiaro](https://github.com/Niewiaro)