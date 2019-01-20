from .utilities import utilities
import sys

import psutil


def display_details(mem, swap_mem):

    utilities.horizontal_line()
    utilities.centered("Memory Info")
    utilities.horizontal_line()
    utilities.vertical_space(2)

    total_memory = mem[0] / 1024 / 1024 / 1024
    available_memory = mem[1] / 1024 / 1024 / 1024
    total_swap_memory = swap_mem[0] / 1024 / 1024 / 1024
    print("\033[91mPhysical Memory:\033[0m \n")
    print("\033[93mTotal Memory:\033[0m " +
          str(round(total_memory, 2)) + " GB")
    print("\033[93mAvailable memory:\033[0m " +
          str(round(available_memory, 2)) + " GB")
    print("\033[93mUsed Memory:\033[0m " + str(mem[2]) + "%")
    print("\033[93mUsed Memory:\033[0m " +
          str(round(total_memory - available_memory, 2)) + " GB")
    try:
        print("\033[93mBuffers:\033[0m " +
              str(round(mem[7] / 1024 / 1024 / 1024, 2)) + " GB")
        print("\033[93mCached:\033[0m " +
              str(round(mem[8] / 1024 / 1024 / 1024, 2)) + " GB")
        print("\033[93mShared:\033[0m " +
              str(round(mem[9] / 1024 / 1024 / 1024, 2)) + " GB")

    except:
        pass

    finally:

        print("\n\033[91mSWAP MEMORY:\033[0m \n ")
        print("\033[93mTotal Swap Memory:\033[0m " +
              str(round(total_swap_memory, 2)) + " GB")
        print("\033[93mUsed Swap Memory:\033[0m " +
              str(round(swap_mem[2] / 1024 / 1024 / 1024, 2)) + " GB")
        print("\033[93mAvailable Swap Memory:\033[0m " +
              str(round(swap_mem[3] / 1024 / 1024 / 1024, 2)) + " GB")


def memory_info():

    mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()

    display_details(mem, swap_mem)
    print("\n")
    return
