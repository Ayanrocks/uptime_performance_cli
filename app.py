#!/usr/bin/env python3


import cli

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
