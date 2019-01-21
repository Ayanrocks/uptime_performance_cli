# Main CLI class

# Dependencies

import os
import sys
import time
import platform as pm
from . import cli_modules as cli

# Export Class CLI


class CLI:
    '''
    A python CLI for performance metrics and network pinging

    '''

    accepted_commands = ['man', 'help', 'check', "os", "net", "disks", "version", "-v", "clear",
                         "list_logs", "more_log_info", "exit", 'mem', 'cpu', 'get_id']

    def __init__(self, cmd=""):
        if pm.system() == "Windows":
            os.system("cls")

        elif pm.system() == "Linux":
            os.system("clear")

        else:
            os.system("clear")

        print("Starting CLI in " + pm.platform())

        if sys.version[0] == "3":
            if cmd != "":
                self.start(cmd)
            else:
                self.start()
        else:
            print("Python " + sys.version[:5] +
                  " detected. Please Use python 3.5 and above")
            print("Exiting...")
            time.sleep(2)
            exit(0)

    def start(self, cmd=""):
        while(1):
            try:
                if cmd != "":
                    self.cmd = cmd
                    if(self.command_validate()):
                        self.emit_command()
                        cmd = ""
                    else:
                        print(
                            "Invalid Argument. Try 'man' or 'help' for list of available commands")
                        cmd = ""

                else:
                    self.cmd = input("> ")
                    if(self.command_validate()):
                        self.emit_command()
                    else:
                        print(
                            "Invalid Command. Try 'man' or 'help' for list of available commands")

            except KeyError:
                self.start()

    def command_validate(self):
        cmd = self.cmd.split(" ")
        if cmd[0] == "":
            return True
        for i in CLI.accepted_commands:

            if cmd[0] == i:
                return True

    def emit_command(self):
        commands = {
            "man": self.man,
            "help": self.man,
            "check": self.check,
            "clear": self.clear,
            "os": self.os,
            "net": self.net,
            "disks": self.disks,
            "version": self.version,
            "-v": self.version,
            "list_logs": self.list_logs,
            "more_log_info": self.log_info,
            "mem": self.mem,
            "cpu": self.cpu_info,
            "get_id": self.get_id,
            "exit": self.exit

        }
        cmd = self.cmd.split(" ")[0]
        commands[cmd]()

    def man(self):
        cli.man()

    def check(self):
        cli.check(self.cmd)

    def clear(self):
        if pm.system() == "Windows":
            os.system("cls")

        elif pm.system() == "Linux":
            os.system("clear")

        else:
            os.system("clear")

        print("Starting CLI in " + pm.platform())

    def mem(self):
        cli.mem_info()

    def cpu_info(self):
        cli.cpu_info()

    def get_id(self):
        print("Current Process ID: " + str(os.getpid()))

    def version(self):
        print("v1.0.2")

    def os(self):
        cli.os_info()

    def net(self):
        cli.net()

    def disks(self):
        cli.disks()

    def list_logs(self):
        print("list_logs")

    def log_info(self):
        print("log_info")

    def exit(self):
        print("Exiting!!!")
        exit(1)
