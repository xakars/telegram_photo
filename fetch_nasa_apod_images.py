import argparse
import os
import requests
from dotenv import load_dotenv
from useful_tools import get_extension_from_url, save_image


def fetch_nasa_daily_photo(token: str, count_img: int):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {"api_key": token, "count": count_img}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    all_img_url = [response.get("hdurl") for response in response.json()]

    for img_index, img_url in enumerate(all_img_url):
        if not img_url:
            continue
        pic_name = f"nasa{img_index}{get_extension_from_url(img_url)}"
        save_image(img_url, "images", pic_name)


def main():
    token = os.environ["NASA_TOKEN"]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--count_img", default=30, help="enter amount of images", type=int
    )
    args = parser.parse_args()
    count_img = args.count_img
    fetch_nasa_daily_photo(token, count_img)


if __name__ == "__main__":
    load_dotenv()
    main()
