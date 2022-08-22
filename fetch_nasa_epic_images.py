import requests
import os
from dotenv import load_dotenv
from useful_tools import save_image


def feth_epic_photo():
	url = "https://api.nasa.gov/EPIC/api/natural/all"
	payload = {
		'api_key': os.environ['NASA_TOKEN']
	}
	response = requests.get(url, params=payload)
	response.raise_for_status()
	for response in response.json()[:5]:
		date = response['date']
		url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}"
		response = requests.get(url, params=payload)
		response.raise_for_status()
		img_date = response.json()[0]['date'].split()[0]
		img_date_for_url = img_date.replace('-', '/')
		image = response.json()[0]['image']
		img_url = f"https://api.nasa.gov/EPIC/archive/natural/{img_date_for_url}/png/{image}.png"
		response = requests.get(img_url, params=payload)
		response.raise_for_status()
		picname = image + '.png'
		save_image(response.url, 'images', picname)


def main():
	feth_epic_photo()

if __name__ == '__main__':
	load_dotenv()
	main()