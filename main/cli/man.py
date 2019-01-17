import os
import math


def horizontal_line():
    width = os.get_terminal_size()[0]
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


def man():
    commands = {
        "man": "Show the help page",
        "help": "Same as 'man' command",
        "check --(url) ": "Pinging and testing server. Takes url as an optional argument",
        "os": "Shows info about the current os",
        "version, -v": "Shows version of the cli",
        "free mem": "Shows available memory on the system",
        "cpu info": "Shows info about the cpu",
        "get id": "Shows the process id of the current process",
        "list logs": "shows available logs",
        "more log info --(id)": "Show details of a specified log file",
        "exit": "Kills the cli"
    }

    horizontal_line()
    centered("CLI Manual")
    horizontal_line()
    vertical_space(2)

    for key, val in commands.items():
        value = "\033[92m" + val + "\033[0m"
        line = "\033[94m" + key + "\033[0m"
        padding = 40 - len(line)
        while(padding):
            line += " "
            padding -= 1
        line += value
        print(line)
        vertical_space()

    vertical_space(2)
    horizontal_line()
