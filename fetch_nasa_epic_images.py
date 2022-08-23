import requests
import argparse
import os
from dotenv import load_dotenv
from useful_tools import save_image


def feth_epic_photo(amount_of_images: int):
	url = "https://api.nasa.gov/EPIC/api/natural/all"
	payload = {
		'api_key': os.environ['NASA_TOKEN']
	}
	response = requests.get(url, params=payload)
	response.raise_for_status()
	for response in response.json()[:amount_of_images]:
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
		picname = f"{image}.png"
		save_image(response.url, 'images', picname)


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--amount_of_images', default=6,
						help='enter amount of images', type=int)
	args = parser.parse_args()
	amount_of_images = args.amount_of_images
	feth_epic_photo(amount_of_images)

if __name__ == '__main__':
	load_dotenv()
	main()