import os
import sys
import time
import platform as pm
from . import cli_modules as cli


class CLI:
    '''
    A python CLI for performance metrics and network pinging

    '''

    accepted_commands = ['man', 'help', 'check', "os", "version", "-v", "clear",
                         "list_logs", "more_log_info", "exit", 'mem', 'cpu', 'get_id']

    def __init__(self):
        os.system("clear")
        print("Starting CLI in " + pm.platform())
        if sys.version[0] == "3":
            self.start()
        else:
            print("Python " + sys.version[:5] +
                  " detected. Please Use python 3.5 and above")
            print("Exiting...")
            time.sleep(2)
            exit(0)

    def start(self):
        while(1):
            try:
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
        os.system("clear")
        print("Starting CLI in " + pm.platform())

    def mem(self):
        cli.mem_info()

    def cpu_info(self):
        print("os info")

    def get_id(self):
        print("get id")

    def version(self):
        print("v1.0.2")

    def os(self):
        print("os")

    def list_logs(self):
        print("list_logs")

    def log_info(self):
        print("log_info")

    def exit(self):
        print("Exiting!!!")
        exit(1)
