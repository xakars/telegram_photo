import requests
import argparse
import os
from dotenv import load_dotenv
from useful_tools import save_image


def fetch_epic_photo(token: str, amount_of_images: int):
	url = "https://api.nasa.gov/EPIC/api/natural/all"
	payload = {
		'api_key': token
	}
	response = requests.get(url, params=payload)
	response.raise_for_status()
	for response in response.json()[:amount_of_images]:
		date = response['date']
		url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}"
		response = requests.get(url, params=payload)
		response.raise_for_status()
		parsed_response = response.json()[0]
		img_date = parsed_response['date'].split()[0]
		img_date_for_url = img_date.replace('-', '/')
		image = parsed_response['image']
		img_url = f"https://api.nasa.gov/EPIC/archive/natural/{img_date_for_url}/png/{image}.png"
		response = requests.get(img_url, params=payload)
		response.raise_for_status()
		picname = f"{image}.png"
		save_image(response.url, 'images', picname)


def main():
	token = os.environ['NASA_TOKEN']
	parser = argparse.ArgumentParser()
	parser.add_argument('--amount_of_images', default=6,
						help='enter amount of images', type=int)
	args = parser.parse_args()
	amount_of_images = args.amount_of_images
	fetch_epic_photo(token, amount_of_images)

if __name__ == '__main__':
	load_dotenv()
	main()