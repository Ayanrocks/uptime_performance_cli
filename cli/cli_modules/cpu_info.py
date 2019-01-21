# Info about the cpu

# Dependencies

import sys
import time
import psutil
import math
from .utilities import utilities as ut
import platform as pm

# Exports


def display_linux():
    cpu_times = psutil.cpu_times()
    cpu_percent = psutil.cpu_percent(percpu=True)
    cpu_times_percent = psutil.cpu_times_percent()
    cpu_count = psutil.cpu_count()
    cpu_stats = psutil.cpu_stats()
    cpu_freq = psutil.cpu_freq(percpu=True)

    print("\n" + ut.colored_string("CPU Count:", 94) + " " + str(cpu_count))
    print("\n" + ut.colored_string("CPU Percentage -- (Core)\n", 94))
    for i, v in enumerate(cpu_percent):
        print(ut.colored_string(
            "Core " + str(i) + ": ", 91) + str(v) + "%")

    print(ut.colored_string("\nCPU percent -- (Job)\n", 94))
    print(ut.colored_string("User: ", 91) + str(cpu_times_percent[0]) + "%")
    print(ut.colored_string("Nice: ", 91) + str(cpu_times_percent[1]) + "%")
    print(ut.colored_string("System: ", 91) + str(cpu_times_percent[2]) + "%")
    print(ut.colored_string("idle: ", 91) + str(cpu_times_percent[3]) + "%")
    print(ut.colored_string("iowait: ", 91) + str(cpu_times_percent[4]) + "%")
    print(ut.colored_string("irq: ", 91) + str(cpu_times_percent[5]) + "%")
    print(ut.colored_string("softirq: ", 91) + str(cpu_times_percent[6]) + "%")
    print(ut.colored_string("steal: ", 91) + str(cpu_times_percent[7]) + "%")
    print(ut.colored_string("guest: ", 91) + str(cpu_times_percent[8]) + "%")

    print(ut.colored_string("\nCPU frequency --\n", 94))
    for inx, i in enumerate(cpu_freq):
        print(ut.colored_string("\nCore " + str(inx) + " -> ", 92))
        print(ut.colored_string("Current: ", 91) +
              str(math.floor(i[0])) + "MHz")
        print(ut.colored_string("Min: ", 91) + str(math.floor(i[1])) + "MHz")
        print(ut.colored_string("Max: ", 91) + str(math.floor(i[2])) + "MHz")

    print(ut.colored_string("\nCPU Stats -- \n", 94))
    print(ut.colored_string("ctx_switches: ", 91) + str(cpu_stats[0]))
    print(ut.colored_string("interrupts: ", 91) + str(cpu_stats[1]))
    print(ut.colored_string("soft_interrupts: ", 91) + str(cpu_stats[2]))
    print(ut.colored_string("syscalls: ", 91) + str(cpu_stats[3]))

    print(ut.colored_string("\nCPU Times-- \n", 94))
    print(ut.colored_string("On User: ", 91) +
          str(round(cpu_times[0] / 60, 2)) + " mins")
    print(ut.colored_string("On System: ", 91) +
          str(round(cpu_times[2] / 60, 2)) + " mins")
    print(ut.colored_string("On Idle: ", 91) +
          str(round(cpu_times[3] / 60, 2)) + " mins")
    print("\n")


def display_windows():
    cpu_times = psutil.cpu_times()
    cpu_percent = psutil.cpu_percent(percpu=True)
    cpu_times_percent = psutil.cpu_times_percent()
    cpu_count = psutil.cpu_count()
    cpu_stats = psutil.cpu_stats()
    cpu_freq = psutil.cpu_freq()
    print("\n" + ut.colored_string("CPU Count:", 94) + " " + str(cpu_count))
    print("\n" + ut.colored_string("CPU Percentage -- (Core)\n", 94))
    for i, v in enumerate(cpu_percent):
        print(ut.colored_string(
            "Core " + str(i) + ": ", 91) + str(v) + "%")

    print(ut.colored_string("\nCPU percent -- (Job)\n", 94))
    print(ut.colored_string("User: ", 91) + str(cpu_times_percent[0]) + "%")
    print(ut.colored_string("System: ", 91) + str(cpu_times_percent[1]) + "%")
    print(ut.colored_string("idle: ", 91) + str(cpu_times_percent[2]) + "%")
    print(ut.colored_string("interrupt: ", 91) +
          str(cpu_times_percent[3]) + "%")
    print(ut.colored_string("dpc: ", 91) + str(cpu_times_percent[4]) + "%")

    print(ut.colored_string("\nCPU frequency --\n", 94))
    print(ut.colored_string("Current: ", 91) +
          str(math.floor(cpu_freq[0])) + "MHz")
    print(ut.colored_string("Min: ", 91) +
          str(math.floor(cpu_freq[1])) + "MHz")
    print(ut.colored_string("Max: ", 91) +
          str(math.floor(cpu_freq[2])) + "MHz")

    print(ut.colored_string("\nCPU Stats -- \n", 94))
    print(ut.colored_string("ctx_switches: ", 91) + str(cpu_stats[0]))
    print(ut.colored_string("interrupts: ", 91) + str(cpu_stats[1]))
    print(ut.colored_string("soft_interrupts: ", 91) + str(cpu_stats[2]))
    print(ut.colored_string("syscalls: ", 91) + str(cpu_stats[3]))

    print(ut.colored_string("\nCPU Times-- \n", 94))
    print(ut.colored_string("On User: ", 91) +
          str(round(cpu_times[0] / 60, 2)) + " mins")
    print(ut.colored_string("On System: ", 91) +
          str(round(cpu_times[2] / 60, 2)) + " mins")
    print(ut.colored_string("On Idle: ", 91) +
          str(round(cpu_times[3] / 60, 2)) + " mins")
    print("\n")


def cpu_info():
    ut.vertical_space()
    ut.centered("CPU Details ")
    ut.horizontal_line()

    if pm.system() == "Windows":
        display_windows()
    else:
        display_linux()
    return True
