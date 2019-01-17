import os
import sys
import platform as pm
import cli


class CLI:
    '''
    A python CLI too for performance metrics and network pinging

    '''

    accepted_commands = ['man', 'help', 'check',
                         'free mem', 'cpu info', 'os info',
                         'get id']

    def __init__(self):
        print("Starting CLI in " + pm.platform())
        self.start()

    def start(self):
        self.cmd = input("> ")
        if(self.command_validate()):
            self.emit_command()
        else:
            print("Invalid Command. Try 'man' or 'help' for list of available commands")

    def command_validate(self):
        for i in CLI.accepted_commands:
            if(i == self.cmd):
                return True

    def emit_command(self):
        commands = {
            "man": self.man,
            "help": self.man,
            "check": self.check,
            "free mem": self.mem,
            "cpu info": self.cpu_info,
            "get id": self.get_id

        }
        commands[self.cmd]()

    def man(self):
        cli.man()

    def check(self):
        print("check")

    def mem(self):
        print("mem")

    def cpu_info(self):
        print("os info")

    def get_id(self):
        print("get id")

    def exit(self):
        print("Manual")


obj = CLI()
