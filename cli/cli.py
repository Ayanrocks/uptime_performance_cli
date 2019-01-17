import os
import sys
import platform as pm
from . import cli_modules as cli


class CLI:
    '''
    A python CLI too for performance metrics and network pinging

    '''

    accepted_commands = ['man', 'help', 'check', "os", "version", "-v"
                         "list_logs", "more_log_info", "exit", 'free_mem', 'cpu_info', 'get_id']

    def __init__(self):
        os.system("clear")
        print("Starting CLI in " + pm.platform())
        self.start()

    def start(self):
        while(1):

            self.cmd = input("> ")
            if(self.command_validate()):
                self.emit_command()
            else:
                print(
                    "Invalid Command. Try 'man' or 'help' for list of available commands")

    def command_validate(self):
        cmd = self.cmd.split(" ")
        for i in CLI.accepted_commands:
            if cmd[0] in i:
                return True

    def emit_command(self):
        commands = {
            "man": self.man,
            "help": self.man,
            "check": self.check,
            "os": self.os,
            "version": self.version,
            "-v": self.version,
            "list_logs": self.list_logs,
            "more_log_info": self.log_info,
            "free_mem": self.mem,
            "cpu_info": self.cpu_info,
            "get_id": self.get_id,
            "exit": self.exit

        }
        cmd = self.cmd.split(" ")[0]
        commands[cmd]()

    def man(self):
        cli.man()

    def check(self):
        cli.check(self.cmd)

    def mem(self):
        print("mem")

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
