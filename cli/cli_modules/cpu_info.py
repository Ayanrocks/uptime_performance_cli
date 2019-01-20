# Info about the cpu

# Dependencies

import psutil
from .utilities import utilities

# Exports


def cpu_info():
    cpu_times = psutil.cpu_times()
    utilities.vertical_space()
    utilities.centered("CPU Details")
    utilities.horizontal_line()
    print("\nCPU Times: \n")
    print("On User: " + str(round(cpu_times[0] / 60, 2)) + " mins")
    print("On System: " + str(round(cpu_times[2] / 60, 2)) + " mins")
    print("On Idle: " + str(round(cpu_times[3] / 60, 2)) + " mins")
    print("\n")
