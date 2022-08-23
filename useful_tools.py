import requests
from pathlib import Path
import os


def save_image(url, path, picname):
	Path(f"{path}").mkdir(parents=True, exist_ok=True)
	response = requests.get(url)
	response.raise_for_status()
	path_to_save = os.path.join(path, picname)
	with open(path_to_save, 'wb') as file:
		file.write(response.content)


def get_extension_from_url(url):
	return os.path.splitext(url)[1]