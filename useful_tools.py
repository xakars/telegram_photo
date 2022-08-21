import requests
from pathlib import Path
import os


def save_image(url, path, picname):
	Path(f"{path}").mkdir(parents=True, exist_ok=True)
	response = requests.get(url)
	response.raise_for_status
	with open(f'{path}/{picname}', 'wb') as file:
		file.write(response.content)


def get_extension_from_url(url):
	return os.path.splitext(url)[1]