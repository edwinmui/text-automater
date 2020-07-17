# Text Automater
Text Automater is a program that lets you send messages containing any desired text to any iMessage phone number, word by word.
Written in AppleScript and Python, this program works on all macOS devices.

## Installation

To use this program, first clone the repo to your macOS system:
```bash
git clone https://github.com/edwinmui/text-automater.git
```
I recommend using VSCode to open the program. If you use VSCode, made sure to 
download the AppleScript extension by idleberg (VSCode > Extensions > Search "AppleScript")

## Setup
In the config.py file, there is a variable called *PHONE_NUM*. Change the value
to the desired iMessage phone number you wish to send messages to.

In the spam.txt file, you are able to replace the current text with an desired text
you wish to send via iMessage.

## Usage
In terminal, navigate to the source folder and run the program with:
```bash
python3 main.py
```
Enjoy!
