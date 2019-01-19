#!/usr/bin/env python3


import cli
import time


def start():
    try:
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
        start()
    except Exception as e:

        print("Some Error Occured. Restarting Terminal")
        time.sleep(2)
        main()


if __name__ == "__main__":
    main()
