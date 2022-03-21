# Space-Explorer
Introspective and intergalactic Python game built with the pygame library that utilizes ESP32, potentiometer, joystick, and button hardware.

![Enclosure](https://user-images.githubusercontent.com/60529049/159200595-6b7e5fe0-15ae-4ebb-ac9e-38d288315d3e.jpg)

Link to Medium blog post [here](https://medium.com/@ambermildenhall/interactive-devices-space-explorer-game-2bf27f321ce0) with more information.

The Arduino IDE version 1.8.19 for MacOS was used to write the code for this project. An ESP32 TTGO T-Display was connected to the host computer via a USB cable which was selected as the port under Tools in the IDE preferences. 

## Materials:
- ESP32 TTGO T-Display
- USB compatible with computer
- Button
- Potentiometer
- Joystick

## Hardware and Software Setup:
- Connect ESP32 TTGO T-Display to computer with [Arduino IDE](https://www.arduino.cc/en/software) with a power and data transferring USB cable
- Go into preferences in the Arduino IDE and enable the ESP32 board by adding the following URL to the board manager:
  - https://dl.espressif.com/dl/package_esp32_index.json
- Under Tools, go to Board and select TTGO T1 under ESP32 Arduino
- Select the correct port for your USB
- Connect button, potentiometer, and joystick to ESP32 (instructions can be found [here](https://docs.google.com/document/d/1T4hlk-eF1qglwRK2hx12-jN0KnyRpw9Z82uum1wyHaM/edit?usp=sharing))
- Upload space-explorer.ino to ESP32
- Run space-explorer.py in IDE of choice
- Play the game using the connected hardware!

## Enclosure Setup
- Use or create a box with an open side such that the USB cable is accessible
- Poke the joystick, button, and potentiometer through the box so that it is exposed to the user
- Design as you wish! See picture at the top for inspiration.

## Demonstration
<img width="930" alt="cover" src="https://user-images.githubusercontent.com/60529049/159202175-58164060-fe8d-48c8-87b7-c77ea0bc445d.png">
https://youtu.be/812txpMeIHI

# Music
Space Ambience by Alexander Nakarada | https://www.serpentsoundstudios.com
Music promoted by https://www.free-stock-music.com
Attribution 4.0 International (CC BY 4.0)
https://creativecommons.org/licenses/by/4.0/
