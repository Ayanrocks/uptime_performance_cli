from .utilities import utilities
import os
import sys
import psutil


def display_details(mem, swap_mem):
    total_memory = mem[0] / 1024 / 1024 / 1024
    available_memory = mem[1] / 1024 / 1024 / 1024
    total_swap_memory = swap_mem[0] / 1024 / 1024 / 1024
    print("Physical Memory: \n")
    print("Total Memory: " + str(round(total_memory, 2)) + " GB")
    print("Available memory: " + str(round(available_memory, 2)) + " GB")
    print("Used Memory: " + str(mem[2]) + "%")
    print("Used Memory: " + str(round(total_memory - available_memory, 2)) + " GB")
    print("Buffers: " + str(round(mem[7] / 1024 / 1024 / 1024, 2)) + " GB")
    print("Cached: " + str(round(mem[8] / 1024 / 1024 / 1024, 2)) + " GB")
    print("Shared: " + str(round(mem[9] / 1024 / 1024 / 1024, 2)) + " GB")
    print("\nSWAP MEMORY: \n ")
    print("Total Swap Memory: " + str(round(total_swap_memory, 2)) + " GB")
    print("Used Swap Memory: " +
          str(round(swap_mem[2] / 1024 / 1024 / 1024, 2)) + " GB")
    print("Available Swap Memory: " +
          str(round(swap_mem[3] / 1024 / 1024 / 1024, 2)) + " GB")


def memory_info():
    utilities.horizontal_line()
    utilities.centered("Memory Info")
    utilities.horizontal_line()
    utilities.vertical_space(2)

    mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()

    display_details(mem, swap_mem)
    sys.stdout.flush()
