# Space Telegram

Project can download space images from different source like NASA, SpaceX, after that publish to a telegram channel or group.

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
Also you need to set NASA_TOKEN in .env file. You can get token in [api.nasa](https://api.nasa.gov/)
```
NASA_TOKEN=
```
### How to use

For download the latest flight photo from SpaceX:

```
python3 fetch_spacex_images.py 
```
You can use **--flight_id** flag for download specific flight photo, for example:
```
python3 fetch_spacex_images.py --flight_id 5a9fc479ab70786ba5a1eaaa
```
For download the EPIC photo from NASA:
```
python3 fetch_nasa_epic_images.py
```
For download the APOD photo from NASA:
```
fetch_nasa_apod_images.py
```
Before use tg_bot.py script you need to set TG_TOKEN in .env file. Telegram channel and bot should be already exists
```
TG_TOKEN=
```
For publish photo to telegram channel or group run tg_bot.py script.
```
python3 tg_bot.py
```
Use **--delay_time** flag for specify the publication frequency in hours
```
python3 tg_bot.py --delay_time 6
```
### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).