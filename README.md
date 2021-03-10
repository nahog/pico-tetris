# Tetris like game for raspberry pi pico and Pimoroni's pico display

1. Uses Pimoroni's micropython
2. Requires a raspberry pi pico microcontroller
3. Requires a Pimoroni's pico display connected to the pico

## nahog/picodisplay-emulator 

Has a copy of a display emulator that draws on a windows instead of using the real pico (at least for simple graphics). Also a mock emulator for machine and utime that pass though stuff to time or simply does nothing.

## Basic usage

B = Rotate
A = Reset
Y = Move left
X = Move rigth

## Issues

* Still have collision and end game detection bugs
* Next piece does not reset the rotation
* Some times pressing a button registers double presses
* Music (if activated) usually hangs (I think is using too much memory)
* Music in the same core can create note length delays, solution is move it to the second core, but multi core tests locked the board

## TODO

* Use the A button to open a menu instead of Reset
* Improve the redraw algorithm
* Implement a drop piece button (maybe one press on A drops, long press opens menu)