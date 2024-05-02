import time
from requests import get as detection
import os
import datetime

while True:
    try:
        image_time = int(datetime.datetime.now(datetime.UTC).timestamp())
        response = detection("http://0.0.0.0:9090/detect").text
        if response == 'No animal detected':
            pass
        else:
            if " " in response:
                animal, tries = response.split(" ")
                print(f"Found {animal} at {image_time}. Scared away after {tries} tries")
            else:
                animal = response
                print(f"Found {animal} at {image_time}")
    except Exception as ex:
        print(ex)
        pass
    time.sleep(1)