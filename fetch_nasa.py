import os
import os.path
import pathlib

from urllib.parse import urlparse, unquote

import requests
from dotenv import load_dotenv

from dateutil.parser import parse



load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")


def download_image(url: str, path: str, name: str) -> None:
    """Downlad image from url"""
    response = requests.get(url)
    response.raise_for_status()
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    with open(f"{path}{name}", "wb") as file:
        file.write(response.content)


def get_file_extensions(url: str) -> str:
    """Get file extension from url"""
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path)
    file = os.path.split(path)[-1]
    return os.path.splitext(file)[-1]




def get_apod_photo() -> None:
    payload = {
    "api_key": NASA_API_KEY,
    "start_date": "2022-04-01"
    }
    response = requests.get(
            "https://api.nasa.gov/planetary/apod", 
            params=payload
            )
    json_response = response.json()
    for index, item in enumerate(json_response, start=1):
        download_image(
                url=item["url"], 
                path="nasa_images/", 
                name=f"nasa_image_{index}{get_file_extensions(item['url'])}"
                )


def get_epic_photo() -> None:
    payload = {
    "api_key": NASA_API_KEY
    }
    response = requests.get(
            "https://api.nasa.gov/EPIC/api/natural/images", 
            params=payload
            )
    json_response = response.json()
    for item in json_response:
        dt = parse(item["date"])
        nasa_epic_link = f"https://api.nasa.gov/EPIC/archive/natural/{dt.strftime('%Y/%m/%d')}/png/{item['image']}.png?api_key={NASA_API_KEY}"
        download_image(
                url=nasa_epic_link, 
                path="nasa_epic_images/", 
                name=f"{item['image']}{get_file_extensions(nasa_epic_link)}"
                )

get_epic_photo()
get_apod_photo()
