import requests
import argparse
import os
from dotenv import load_dotenv
from useful_tools import save_image
from datetime import datetime


def fetch_epic_photo(token: str, amt_img: int):
	url = "https://api.nasa.gov/EPIC/api/natural/all"
	payload = {
		'api_key': token
	}
	response = requests.get(url, params=payload)
	response.raise_for_status()
	for images_date  in response.json()[:amt_img]:
		date = images_date['date']
		url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}"
		response = requests.get(url, params=payload)
		response.raise_for_status()
		image_metadata = response.json()[0]
		img_date = image_metadata['date'].split()[0]
		img_date_for_url = datetime.strftime(datetime.fromisoformat(img_date), "%Y/%m/%d")
		image = image_metadata['image']
		img_url = f"https://api.nasa.gov/EPIC/archive/natural/{img_date_for_url}/png/{image}.png"
		response = requests.get(img_url, params=payload)
		response.raise_for_status()
		picname = f"{image}.png"
		save_image(response.url, 'images', picname)


def main():
	token = os.environ['NASA_TOKEN']
	parser = argparse.ArgumentParser()
	parser.add_argument('--amt_img', default=6,
						help='enter amount of images', type=int)
	args = parser.parse_args()
	amt_img = args.amt_img
	fetch_epic_photo(token, amt_img)

if __name__ == '__main__':
	load_dotenv()
	main()