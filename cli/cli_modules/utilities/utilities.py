# Utilities file

# Dependencies

import os
import shutil
import math


# Exports
def horizontal_line():
    try:

        width = os.get_terminal_size()[0]
        line = ""
        while(width):
            line += "-"
            width -= 1
        print(line)
    except:
        width = shutil.get_terminal_size()[0]
        line = ""
        while(width):
            line += "-"
            width -= 1
        print(line)


def centered(str):
    width = os.get_terminal_size()[0]
    left_padding = math.floor((width - len(str)) / 2)
    line = ""
    while(left_padding):
        line += " "
        left_padding -= 1
    line += str
    print(line)


def vertical_space(n=1):
    while(n):
        print("")
        n -= 1


def colored_string(string, color):
    new_str = "\033[" + str(color) + "m" + string + "\033[0m"
    return new_str
