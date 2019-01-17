
import requests as rq
import os
import subprocess
import time
from progress.spinner import Spinner


def get_url():
    url = input("Enter an url: ")
    validate_url(url)


def validate_url(url):
    if "https" in url:
        url.replace("http", "")

    elif "http" in url:
        url.replace("http", "")
    else:
        ping(url)


def ping(url):

    try:
        print("Waiting  for response")
        # print("Pinging " + url)
        spinner = Spinner(" Pinging" + url)
        res = subprocess.check_output("ping -c 4 " + url, shell=True)
        for i in range(100):
            spinner.next()
            time.sleep(.01)

        res = str(res)
        res_split = res.split("ping")[1].split("\\n")
        print("\n")
        print("Ping" + res_split[0])
        print("\n")

        print("Transmission Statistics \n " + res_split[1])
        print("\n")

        print("Latency: \n" + res_split[2])
        print("\n")

        input("Want to save this data to log (y/n): ")
    except subprocess.CalledProcessError:
        print("Invalid Url")
        get_url()


def monitor(cmd):
    cmd_split = cmd.split("--")
    try:
        args = cmd_split[1].split(" ")[1]
        validate_url(args)

    except IndexError:
        get_url()
