from requests import get
import os
import logging

CAMERA_ENDPOINT = os.getenv('CAMERA_ENDPOINT')
OPTIONS = [
    "framesize",
    "led_intensity",
]


def modify_settings(key, value):
    if key not in OPTIONS:
        logging.error(f'Invalid camera setting: {key}')
        return False
    
    try:
        response = get(f'{CAMERA_ENDPOINT}/control?var={key}&val={value}')
        return response.status_code == 200
    
    except Exception as err:
        logging.error(f'Error configuring camera: {err}')
        return False


def take_snapshot():
    try:
        response = get(f'{CAMERA_ENDPOINT}/capture')
        return response.content
    
    except Exception as err:
        logging.error(f'Error taking snapshot: {err}')
        return None
