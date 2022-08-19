import requests
from pathlib import Path


def save_image(url, path, picname):
	Path(f"{path}").mkdir(parents=True, exist_ok=True)
	response = requests.get(url)
	response.raise_for_status
	with open(f'{path}/{picname}', 'wb') as file:
		file.write(response.content)


def feth_spacex_last_launch():
	url = "https://api.spacexdata.com/v3/launches/past"
	payload = {
        	'flight_id': '5a9fc479ab70786ba5a1eaaa'
	}
	response = requests.get(url, params=payload)
	return response.json()[0]['links']['flickr_images']

def feth_nasa_daily_photo():
	url = "https://api.nasa.gov/planetary/apod"
	payload = {
		'api_key': 'mV7fGWbWCQCHWZx1tXnxcjQMxJEJq0QjgXRNDlE0'
	}
	response = requests.get(url, params=payload)
	return response.json()['url']

#for pic_number, picture in enumerate(feth_spacex_last_launch()):
#	pic_name = 'spacex' + str(pic_number) + '.jpg'
#	save_image(picture, 'images3', pic_name)

print(feth_nasa_daily_photo())

