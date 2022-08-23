import requests
import argparse
import os
from dotenv import load_dotenv
from useful_tools import save_image
from useful_tools import get_extension_from_url


def feth_nasa_daily_photo(amount_of_images: int):
	url = "https://api.nasa.gov/planetary/apod"
	payload = {
		'api_key': os.environ['NASA_TOKEN'],
		'count': amount_of_images
	}
	response = requests.get(url, params=payload)
	response.raise_for_status()
	all_img_url = []
	response_as_json = response.json()

	for response in response_as_json:
		all_img_url.append(response.get('hdurl'))

	for img_index, img_url in enumerate(all_img_url):
		if not img_url:
			continue
		pic_name = f"nasa{str(img_index)}{get_extension_from_url(img_url)}"
		save_image(img_url, 'images', pic_name)


def  main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--amount_of_images', default=30,
						help='enter amount of images', type=int)
	args = parser.parse_args()
	amount_of_images = args.amount_of_images
	feth_nasa_daily_photo(amount_of_images)

if __name__ == '__main__':
	load_dotenv()
	main()