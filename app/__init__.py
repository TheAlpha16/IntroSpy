from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import logging
from .camera import modify_settings
import os

try:
    load_dotenv()
    logging.info('Environment variables loaded')
except Exception as err:
    logging.error(f'Error loading environment variables: {err}')

try:
    if not modify_settings('framesize', 11):
        logging.error('Error configuring framesize')

    if not modify_settings('led_intensity', 0):
        logging.error('Error configuring led_intensity')

    logging.info('Camera settings configured')
    
except Exception as err:
    logging.error(f'Error configuring camera settings: {err}')


app = Flask(__name__)
client = MongoClient(os.environ.get("DB_CONN"))  # Connect to MongoDB
db = client['wild']
app.config["DATABASE"] = db


if 'snaps' not in db.list_collection_names():
    db.create_collection("snaps", codec_options=None,
    validator={
            '$jsonSchema': {
                'bsonType': 'object',
                'required': ['timestamp', 'image_url', 'animal'],
                'properties': {
                    'timestamp': {
                        'bsonType': 'int',
                        'description': 'must be a date and is required'
                    },
                    'image_url': {
                        'bsonType': 'string',
                        'description': 'file path to image and is required'
                    },
                    'animal': {
                        'bsonType': 'string',
                        'description': 'animal name and is required'
                    }
                }
            }
        }
    )

from app import routes