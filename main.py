TESTFLIGHT_LINK = ""
INTERVAL = 60 # in seconds

import time
import requests
import os

print("Hello!")
while True:
    response = requests.get(TESTFLIGHT_LINK)
    if (response.status_code != 200):
        print("Error: " + str(response.status_code))
    if (response.content.find(b"This beta is full") != -1):
        print("Beta is full")
    else:
        print("Beta is not full. Opening in ur favorite browser...")
        os.system("open " + TESTFLIGHT_LINK)
        os.system("say 'Testflight link is not full.'")
        break
            
    print(f"{time.strftime('%H:%M', time.localtime())} eepy time...\n")
    time.sleep(INTERVAL)

print("Goodbye :(")