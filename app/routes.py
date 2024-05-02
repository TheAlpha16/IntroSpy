from flask import request
from app import app
from .camera import take_snapshot
from .database import insert_data
import datetime
import logging
from .detect import detect_animal
import os

from pydub import AudioSegment
from pydub.playback import play

@app.route('/detect', methods=['GET'])
def detect():
    if request.method == 'GET':
        # Take a snapshot using ESP32 camera
        image_data = take_snapshot()
        image_time = int(datetime.datetime.now(datetime.UTC).timestamp())
        image_path = f'data/{image_time}.jpg'

        try:
            open(image_path, 'wb').write(image_data)
        except Exception as err:
            logging.error(f'Error saving image: {err}')
            return f'Error saving image: {err}'
        
        # Detect animal in the snapshot
        animal = detect_animal(image_path)

        # Trigger actions based on the detected animal
        if animal == "":
            os.remove(image_path)
            return f'No animal detected'
        
        # Insert the snapshot data into the database
        
        if not insert_data(image_path, image_time, animal):
            return 'Error inserting data into the database'
        
        # Play a sound based on the detected animal
        original_animal = animal
        for i in range(int(os.getenv('MAX_TRIES'))):
            audio = AudioSegment.from_file(f'sounds/scare.mp3')
            play(audio)

            image_data = take_snapshot()
            image_time = int(datetime.datetime.now(datetime.UTC).timestamp())
            image_path = f'data/{image_time}.jpg'

            try:
                open(image_path, 'wb').write(image_data)
            except Exception as err:
                logging.error(f'Error saving image: {err}')
                return f'Error saving image: {err}'
            
            # Detect animal in the snapshot
            animal = detect_animal(image_path)

            if animal == "":
                os.remove(image_path)
                return f'{original_animal} {i + 1}'
        
        return f'{animal}'
