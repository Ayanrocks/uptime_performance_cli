import os
import subprocess

url = input("Enter the url: ")
if(url.find("https") | url.find("http")):
    res = os.system("ping -c 4 " + url)
else:
    try:
        res = os.system("ping -c 4 https://" + url)
    except:
        raise NameError("Error with hostname")
    else:
        res = os.system("ping -c 4 http://" + url)
