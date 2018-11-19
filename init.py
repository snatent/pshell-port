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
agree = 0
while(agree == 0):
	startscrn = input("> ")
	if startscrn == "Agree":
		print("Thank You!")
		agree = 1
	elif startscrn == "Disagree": 
		print("You must agree to the terms and conditions to use this software.")
	else:
		print("I do not recognize that command.")
#GAME GOES HERE
while(True):
    i = input("> ")
    print(i)