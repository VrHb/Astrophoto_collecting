import os
import os.path

import requests
from dotenv import load_dotenv
from dateutil.parser import parse

from api_operations import download_image, get_file_extensions

START_DATE = "2022-04-01"
IMAGES_DIR = "nasa_images/"
EPIC_IMAGES_DIR = "epic_nasa_images/"


def get_apod_photo() -> None:
    payload = {
        "api_key": os.getenv("NASA_API_KEY"),
        "start_date": START_DATE
    }
    response = requests.get(
        "https://api.nasa.gov/planetary/apod",
        params=payload
    )
    nasa_apod_list = response.json()
    for index, item in enumerate(nasa_apod_list, start=1):
        download_image(
            url=item["url"],
            path=IMAGES_DIR,
            name=f"nasa_image_{index}{get_file_extensions(item['url'])}"
        )


def get_epic_photo() -> None:
    payload = {
        "api_key": os.getenv("NASA_API_KEY")
    }
    response = requests.get(
        "https://api.nasa.gov/EPIC/api/natural/images",
        params=payload
    )
    nasa_epic_images_list = response.json()
    for item in nasa_epic_images_list:
        dt = parse(item["date"])
        nasa_epic_link = f"""https://api.nasa.gov/EPIC/archive/natural/\
{dt.strftime('%Y/%m/%d')}/png/\
{item['image']}.png?api_key={os.getenv('NASA_API_KEY')}"""
        download_image(
            url=nasa_epic_link,
            path=EPIC_IMAGES_DIR,
            name=f"{item['image']}{get_file_extensions(nasa_epic_link)}"
        )


def main():
    load_dotenv()
    get_epic_photo()
    get_apod_photo()

if __name__ == "__main__":
    main()

