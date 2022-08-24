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

For download the latest flight photo from SpaceX. You can use **--flight_id** flag for download specific flight photo.

```
python3 fetch_spacex_images.py 
```
```
python3 fetch_spacex_images.py --flight_id 5eb87ce3ffd86e000604b336
```
For download the EPIC photo from NASA. You can use **--amount_of_images** flag to get specific amount of images(default=6):
```
python3 fetch_nasa_epic_images.py
```
```
python3 fetch_nasa_epic_images.py --amount_of_images 5
```
For download the APOD photo from NASA. You can use --amount_of_images flag to get specific amount of images(default=30):
```
python3 fetch_nasa_apod_images.py
```
```
python3 fetch_nasa_apod_images.py --amount_of_images 30
```
Before use tg_bot.py script you need to set TG_TOKEN and TG_CHAT_ID in .env file. Telegram channel and bot should be already exists
```
TG_TOKEN=
TG_CHAT_ID=
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