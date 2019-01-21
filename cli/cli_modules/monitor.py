
import os
import subprocess
import time
import datetime
import platform as pm


def get_url_packets():
    url = input("Enter an url: ")
    if(url != ""):

        packets = input("How many packets to transmit?: ")
        if packets != "":
            validate(url, packets)
        else:
            validate(url)

    else:
        get_url_packets()


def validate(url, packets=4):
    if url == "":
        print("Please enter a valid url")
        get_url_packets()

    elif "https" in url:
        url = url.replace("http", "")
        ping(url, packets)

    elif "http" in url:
        url = url.replace("http", "")
        ping(url, packets)

    else:
        ping(url, packets)


def ping(url, packets):
    # @TODO Fix Ping in windows
    try:
        print("Waiting  for response")
        print("Pinging " + url + " ...")

        if pm.system() == "Windows":
            print("Windows")
            res = subprocess.check_output(
                "ping -n " + str(packets) + " " + url, shell=True).decode("utf-8")
            res_split = res.split("Ping ")[1].split('\r\n')
            res_split[2].join(res_split[3])

        elif pm.system() == "Linux":
            res = subprocess.check_output(
                "ping -c " + str(packets) + " " + url, shell=True).decode("utf-8")
            res_split = res.split("ping")[1].split("\n")

        else:
            res = subprocess.check_output(
                "ping -c " + str(packets) + " " + url, shell=True).decode("utf-8")
            res_split = res.split("ping")[1].split("\n")

        print("\n")
        print("Ping " + res_split[0].replace(" ", ""))
        print("\n")

        print("Transmission Statistics \n " + res_split[1])
        print("\n")

        print("Latency: \n" + res_split[2])
        print("\n")

        ch = input("Want to save this data to log (y/n): ")
        if ch == 'y' or ch == 'Y':

            curr_dir = os.path.abspath(".data/logs/")
            if not os.path.exists(curr_dir):
                os.makedirs(curr_dir)
            file_name = datetime.datetime.now().strftime(
                "%d-%m-%y--%H%M%S") + ".log"
            file_path = os.path.join(curr_dir, file_name)
            try:
                fs = open(file_path, "w+")
                res = res.strip("b'")
                res = res.strip("'")
                print("Wrote: " + str(fs.write(res)))
                print("Log Created at: " + file_path)
                fs.close()
                return
            except OSError:
                print("Error creating file")

        else:
            print("Log didn't created")
            return True

    except subprocess.CalledProcessError:
        print("Invalid Url")
        get_url_packets()
    except:
        return False


def monitor(cmd):
    cmd_split = cmd.split("--")
    try:
        if (cmd_split[1][:4] == "url ") :
            args = cmd_split[1].split(" ")[1]
            try:
                packets = cmd_split[2].split(" ")[1]
                validate(args, packets)

            except IndexError:
                validate(args)
        elif (cmd_split[1][:2] == "u "):
            args = cmd_split[1].split(" ")[1]
            try:
                packets = cmd_split[2].split(" ")[1]
                validate(args, packets)

            except IndexError:
                validate(args)
        else:
            print("Invalid Flags. Use --u or --url")
            get_url_packets()
            
    except IndexError:
        try:
            get_url_packets()
        except:
            pass

    return True
