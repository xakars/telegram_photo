import requests
import argparse
import os
from dotenv import load_dotenv
from useful_tools import save_image
from useful_tools import get_extension_from_url


def fetch_nasa_daily_photo(token: str, amt_img: int):
	url = "https://api.nasa.gov/planetary/apod"
	payload = {
		'api_key': token,
		'count': amt_img
	}
	response = requests.get(url, params=payload)
	response.raise_for_status()
	all_img_url = [response.get('hdurl') for response in response.json()]

	for img_index, img_url in enumerate(all_img_url):
		if not img_url:
			continue
		pic_name = f"nasa{img_index}{get_extension_from_url(img_url)}"
		save_image(img_url, 'images', pic_name)


def main():
	token = os.environ['NASA_TOKEN']
	parser = argparse.ArgumentParser()
	parser.add_argument('--amt_img', default=30,
						help='enter amount of images', type=int)
	args = parser.parse_args()
	amt_img = args.amt_img
	fetch_nasa_daily_photo(token, amt_img)

if __name__ == '__main__':
	load_dotenv()
	main()
