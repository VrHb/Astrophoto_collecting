import os
import os.path

import requests
from dateutil.parser import parse
from dotenv import load_dotenv

from file_operations import download_image, getting_file_extension_from_link

START_DATE = "2022-04-01"
IMAGES_DIR = "images/"


def get_apod_photo(api_key: str | None) -> None:
    payload = {
        "api_key": api_key,
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
            name=f"nasa_image_{index}{getting_file_extension_from_link(item['url'])}"
        )


def get_epic_photo(api_key: str | None) -> None:
    payload = {
        "api_key": api_key
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
{item['image']}.png?api_key={api_key}"""
        download_image(
            url=nasa_epic_link,
            path=IMAGES_DIR,
            name=f"{item['image']}{getting_file_extension_from_link(nasa_epic_link)}"
        )


def main():
    load_dotenv()
    NASA_API_KEY = os.getenv("NASA_API_KEY")
    get_epic_photo(api_key=NASA_API_KEY)
    get_apod_photo(api_key=NASA_API_KEY)

if __name__ == "__main__":
    main()

