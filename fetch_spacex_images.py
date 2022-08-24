import requests
import argparse
from useful_tools import save_image


def fetch_spacex_last_launch(url):
	response = requests.get(url)
	response.raise_for_status()
	all_img_url = response.json()['links']['flickr']['original']
	for img_index, img_url in enumerate(all_img_url):
		img_name = f"spacex{str(img_index)}.jpg"
		save_image(img_url, 'images', img_name)


def  main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--flight_id', default='latest', help='enter flight_id')
	args = parser.parse_args()
	flight_id = args.flight_id
	url = f'https://api.spacexdata.com/v5/launches/{flight_id}'

	try:
		fetch_spacex_last_launch(url)
	except KeyError:
		print("No latest spacex flight, please enter flight_id and try again")

if __name__ == '__main__':
	main()
