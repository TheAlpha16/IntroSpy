from app import db
import logging
"""
    db.create_collection("snaps", {
        'validator': {
            '$jsonSchema': {
                'bsonType': 'object',
                'required': ['timestamp', 'image_url', 'animal'],
                'properties': {
                    'timestamp': {
                        'bsonType': 'date',
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
    })

write code for mongodb where a function exists to insert data into the database"""

def insert_data(image_path, timestamp, animal="unknown"):
    try:
        db.snaps.insert_one({
            'timestamp': timestamp,
            'image_url': image_path,
            'animal': animal
        })
    except Exception as err:
        logging.error(f'Error inserting data: {err}')
        return False
    
    return True