# IntroSpy

IntroSpy is a low powered IoT device that can be deployed at a fence or a gate to detect the presence of an animal. It uses a camera to capture images. The images are then processed using a machine learning model to detect the presence of the animal.


## Features:
- Realtime detection of animals
- Scalable
- Live feed
- Active database

## Tech Stack
- Python
- MongoDB
- Docker
- Flask
- YOLOv3

## Installation

```bash
$ git clone https://github.com/TheAlpha16/IntroSpy
$ cd IntroSpy
$ docker compose up -d

$ pip install -r requirements.txt
$ python main.py
```

To know about docker installation check [this](https://docs.docker.com/engine/install/)

This project was done under the mentorship of Prof. Tarachand Amgoth, students: [@TheAlpha16](https://github.com/TheAlpha16) and [@JBadgujar](https://github.com/JBadgujar)