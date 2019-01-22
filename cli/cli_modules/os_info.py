import os
import platform as pm
import psutil as ps
from .utilities import utilities as ut
import datetime


def system_info():
    users = ps.users()
    print(ut.colored_string("\n    Users  \n", 93))
    for i in users:
        for v in i._fields:
            print(ut.colored_string(v.replace("_", " ").title(), 92) + ": " +
                  str(getattr(i, v)))
        print("\n")

    print(ut.colored_string("\n    System Info  \n", 93))
    print(ut.colored_string("Boot Time: ", 92) +
          datetime.datetime.fromtimestamp(ps.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
    print(ut.colored_string("Running Processes: ", 92) +
          str(len(ps.pids())) + " process")


def display_info():
    print(ut.colored_string("User: ", 92) + os.getlogin())
    print(ut.colored_string("OS: ", 92) + str(pm.platform()))

    print(ut.colored_string("OS Standard: ", 92) + os.name)
    print(ut.colored_string("Architecture: ", 92) + pm.machine())
    print(ut.colored_string("Network Name: ", 92) + pm.node())
    print(ut.colored_string("Processor: ", 92) + pm.processor())

    print(ut.colored_string("Release: ", 92) + str(pm.release()))
    print(ut.colored_string("System: ", 92) + str(pm.system()))
    print(ut.colored_string("Version: ", 92) + str(pm.version()))

    print(ut.colored_string("\nPython Build: ", 92) +
          str(pm.python_version()))
    print(ut.colored_string("Python Build Date: ", 92) +
          str(pm.python_build()[1]))

    if pm.platform() == "Windows":
        info = pm.win32_ver()

        try:
            print(ut.colored_string("\nCSD: ", 92) + str(info[2]))
            print(ut.colored_string("\nptype: ", 92) + str(info[3]))
        except:
            pass
    system_info()


def os_info():
    ut.vertical_space()
    ut.horizontal_line()
    ut.centered("Operating System")
    ut.horizontal_line()
    ut.vertical_space(2)

    display_info()
    return
