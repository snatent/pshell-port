from colorama import init
from colorama import Fore, Back, Style
import os

init()

# COLORAMA USAGE
# print(Fore.CYAN + 'some blue text')
# print(Style.RESET_ALL)

os.chdir("data")

#START SCREEN
print("Luxury Universal [e]Xperience Operating System (version 8.1.1)\n\
(c) 1998 Luxury Universal [e]Xperience Incorporated. All rights reserved.\n\
\n\
Pontishell Suite Management Tool\n\
\
A PRODUCT OF...\n\
\n\
--------------------------------\n\
|  _        _    _    _     _  |\n\
|  ||       ||   ||   \\\\   //  |\n\
|  ||       ||   ||    \\\\ //   |\n\
|  ||       ||   ||    // \\\\   |\n\
|  ||       ||   ||   //   \\\\  |\n\
|  =======   =====    =     =  |\n\
--------------------------------\n\
110% MORE FUN THAN A REGAL CINEMA!\n\
\n\
\n\
\n\
By using this program, you acknowledge that any and all thoughts, experiences, or emotions experienced during its use become exclusive Property of LUX. Do you agree to these terms and conditions? [Agree/Disagree]")
#YOU CANNOT ESCAPE UNTIL YOU AGREE

homeport = "The Network is like a sea extending in all directions, and the computer is your ship. Welcome to your home port, Captain! From here you can plot a course to anywhere on Psuite Island! Where would you like to go?\n \n [North] - Psuite Settings \n [South] - Local Files"


agree = 0
while(agree == 0):
	startscrn = input("> ")
	if startscrn.lower() == "agree":
		print("Thank You!")
		locale = homeport
		agree = 1
	elif startscrn.lower() == "disagree": 
		print("You must agree to the terms and conditions to use this software.")
	else:
		print("I do not recognize that command.")
#GAME GOES HERE
while(True):
	print(locale)
	os.chdir("Local Files")
	with open("index.txt") as f:
		print(f.read())

	i = input("> ")
	print(i)
