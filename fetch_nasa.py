import os
import os.path

import requests
from dotenv import load_dotenv
from dateutil.parser import parse

from api_operations import download_image, get_file_extensions



def get_apod_photo() -> None:
    payload = {
    "api_key": os.getenv("NASA_API_KEY"),
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
    "api_key": os.getenv("NASA_API_KEY")
    }
    response = requests.get(
            "https://api.nasa.gov/EPIC/api/natural/images", 
            params=payload
            )
    json_response = response.json()
    for item in json_response:
        dt = parse(item["date"])
        nasa_epic_link = f"https://api.nasa.gov/EPIC/archive/natural/{dt.strftime('%Y/%m/%d')}/png/{item['image']}.png?api_key={os.getenv('NASA_API_KEY')}"
        download_image(
                url=nasa_epic_link, 
                path="nasa_epic_images/", 
                name=f"{item['image']}{get_file_extensions(nasa_epic_link)}"
                )


def main():
    load_dotenv()
    get_epic_photo()
    get_apod_photo()

if __name__ == "__main__":
    main()

