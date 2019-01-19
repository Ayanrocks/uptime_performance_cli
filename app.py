#!/usr/bin/env python3


import cli
import time
import argparse
import sys


def start(cmd=""):
    try:
        if cmd != "":
            obj = cli.CLI(cmd)
        else:
            obj = cli.CLI()

    except KeyboardInterrupt:
        print(" Exiting ")
        exit(0)
    except EOFError:
        print("Exiting")
        exit(0)
    except KeyError:
        obj = cli.CLI()


def main():
    try:
        if len(sys.argv) == 2:
            cmd = sys.argv[1]
            start(cmd)
        elif len(sys.argv) > 2:
            print("Invalid argument. Starting cli...")
            time.sleep(.5)
            start()
        else:
            start()
    except Exception:

        print("Some Error Occured. Restarting Terminal...")
        time.sleep(2)
        main()


if __name__ == "__main__":
    main()
