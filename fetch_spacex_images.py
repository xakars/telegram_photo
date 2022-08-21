import requests
import argparse
from useful_tools import save_image


def feth_spacex_last_launch(url, flight_id=None):
	payload = {
        	'flight_id': flight_id
	}
	response = requests.get(url, params=payload)
	response.raise_for_status
	all_img_url = response.json()[0]['links']['flickr_images']
	for img_index, img_url in enumerate(all_img_url):
		img_name = 'spacex' + str(img_index) + '.jpg'
		save_image(img_url, 'images_spacex', img_name)


def  main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--flight_id', help='enter flight_id')
	args = parser.parse_args()
	flight_id = args.flight_id
	if not flight_id:
		url = 'https://api.spacexdata.com/v5/launches/latest'
	else:
		url = "https://api.spacexdata.com/v3/launches/past"
	try:
		feth_spacex_last_launch(url, flight_id)
	except KeyError:
		print("No latest spacex flight, please enter flight_id and try again")

if __name__ == '__main__':
	main()
