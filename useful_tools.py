import requests
from pathlib import Path
from urllib.parse import urlparse, unquote, urlsplit
import os


def save_image(url, path, picname):
    Path(f"{path}").mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    path_to_save = os.path.join(path, picname)
    with open(path_to_save, "wb") as file:
        file.write(response.content)


def get_extension_from_url(url):
    parsed_url = urlparse(unquote(url))
    filename = os.path.split(parsed_url.path)[1]
    extension = os.path.splitext(filename)[1]
    return extension
