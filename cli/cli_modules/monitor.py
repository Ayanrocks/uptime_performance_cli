
import os
import subprocess
import time
import datetime


def get_url_packets(logs):
    url = input("Enter an url: ")
    if(url):

        # try:
        packets = input("How many packets to transmit?: ")
        if packets == "":
            validate(url, logs)
        else:
            validate(url, logs, packets)

        # except:
        #     print("except in url")
        #     get_url_packets(logs)

    else:
        get_url_packets(logs)


def validate(url, logs, packets=4):
    if url == "":
        print("Please enter a valid url")
        get_url_packets(logs)

    elif "https" in url:
        url = url.replace("http", "")
        ping(url, logs, packets)

    elif "http" in url:
        url = url.replace("http", "")
        ping(url, logs, packets)

    else:
        ping(url, logs, packets)


def ping(url, logs, packets):

    try:
        print("Waiting  for response")
        print("Pinging " + url + " ...")
        res = subprocess.check_output(
            "ping -c " + packets + " " + url, shell=True)

        res = str(res)
        res_split = res.split("ping")[1].split("\\n")
        print("\n")
        print("Ping" + res_split[0])
        print("\n")

        print("Transmission Statistics \n " + res_split[1])
        print("\n")

        print("Latency: \n" + res_split[2])
        print("\n")

        ch = input("Want to save this data to log (y/n): ")
        if ch == 'y' or ch == 'Y':
            try:
                fs = open("../../.data/logs/" + datetime.datetime.now().strftime(
                    "%d-%m-%y:%H%M%S--" + logs), "w")
                print("Wrote: " + fs.write(res))
                print("Log Created " + fs.read())
                fs.close()
                return
            except OSError:
                print("Error creating file")

        else:
            print("Log didn't created")
            return

    except subprocess.CalledProcessError:
        print("Invalid Url")
        get_url_packets(logs)
    # except:
    #     print("lol")
    #     get_url_packets(logs)


def monitor(cmd, logs):
    cmd_split = cmd.split("--")

    try:
        args = cmd_split[1].split(" ")[1]
        try:
            packets = cmd_split[2].split(" ")[1]
            validate(args, logs, packets)

        except IndexError:
            print("No packets")
            validate(args, logs)
    except IndexError:
        print("sss")
        get_url_packets(logs)

    return
