##import the library for sys, figlet, random
from pyfiglet import Figlet
import random
import sys

figlet = Figlet()


# create a list of the fonts in the figlet
font_list: list[str] = figlet.getFonts()

# apply conditoins to expects zero or two commnad-line arguments:


if len(sys.argv) == 3:
    # the first should be "-f" or "--font"
    # if the first command is not "--f" or "--font" exit the program with errro mesage
    if str(sys.argv[1]) == "-f" or str(sys.argv[1]) == "--font":
        if str(sys.argv[2]) in font_list:
            text = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(text))
        else:
            sys.exit("please provde correct font")

    # the second should be the name of the font.
    else:
        sys.exit("please provide correct input")

elif len(sys.argv) == 1:

    text = input("Input: ")

    figlet.setFont(font=random.choice(font_list))
    print(figlet.renderText(text))
else:
    sys.exit("Invalid Usage")

# zero if the user want to output text in a random font
