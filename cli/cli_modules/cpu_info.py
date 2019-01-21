# Info about the cpu

# Dependencies

import curses
import sys
import time
import psutil
from .utilities import utilities as ut

# Exports


def display_info():
    cpu_times = psutil.cpu_times()
    cpu_percent = psutil.cpu_percent(percpu=True)
    cpu_times_percent = psutil.cpu_times_percent()
    cpu_count = psutil.cpu_count()
    cpu_stats = psutil.cpu_stats()
    cpu_freq = psutil.cpu_freq()
    ut.vertical_space()
    ut.centered("CPU Details ")
    ut.horizontal_line()

    print("\n" + ut.colored_string("CPU Count:", 91) + " " + str(cpu_count))
    print("\n" + ut.colored_string("CPU Percentage -- (Core)\n", 91))
    for i, v in enumerate(cpu_percent):
        print(ut.colored_string(
            "Core " + str(i) + ": ", 91) + str(v) + "%")

    print(ut.colored_string("\nCPU percent -- (Job)\n", 91))
    print(ut.colored_string("User: ", 91) + str(cpu_times_percent[0]) + "%")
    print(ut.colored_string("Nice: ", 91) + str(cpu_times_percent[1]) + "%")
    print(ut.colored_string("System: ", 91) + str(cpu_times_percent[2]) + "%")
    print(ut.colored_string("idle: ", 91) + str(cpu_times_percent[3]) + "%")
    print(ut.colored_string("iowait: ", 91) + str(cpu_times_percent[4]) + "%")
    print(ut.colored_string("irq: ", 91) + str(cpu_times_percent[5]) + "%")
    print(ut.colored_string("softirq: ", 91) + str(cpu_times_percent[6]) + "%")
    print(ut.colored_string("steal: ", 91) + str(cpu_times_percent[7]) + "%")
    print(ut.colored_string("guest: ", 91) + str(cpu_times_percent[8]) + "%")

    print(ut.colored_string("\nCPU Times-- \n", 91))
    print(ut.colored_string("On User: ", 91) +
          str(round(cpu_times[0] / 60, 2)) + " mins")
    print(ut.colored_string("On System: ", 91) +
          str(round(cpu_times[2] / 60, 2)) + " mins")
    print(ut.colored_string("On Idle: ", 91) +
          str(round(cpu_times[3] / 60, 2)) + " mins")
    print("\n")


def cpu_info():
    display_info()
    return True
