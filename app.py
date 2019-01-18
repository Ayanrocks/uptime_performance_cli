#!/usr/bin/env python3


import cli
import time

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
except Exception as e:

    print("Some Error Occured. Restarting Terminal")
    time.sleep(2)
    obj = cli.CLI()
