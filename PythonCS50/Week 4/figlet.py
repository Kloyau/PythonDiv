import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    font_list=figlet.getFonts()
    try:
        if sys.argv[1] not in ['-f','--font']:
            sys.exit("Invalid usage")
        fnt = sys.argv[2]
        if fnt not in font_list:
            sys.exit("Invalid usage")
        figlet.setFont(font=fnt)
    except IndexError:
        figlet.setFont(font=random.choice(font_list))

    print(figlet.renderText(input("Input : ")))

main()
