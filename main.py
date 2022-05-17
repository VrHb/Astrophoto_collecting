import os
import os.path
import pathlib

from urllib.parse import urlparse, unquote

import requests
from dotenv import load_dotenv

from dateutil.parser import parse


load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")
print(NASA_API_KEY)
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"


def download_image(url: str, path: str, name: str) -> None:
    response = requests.get(url)
    response.raise_for_status()
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    with open(f"{path}{name}", "wb") as file:
        file.write(response.content)


def fetch_spacex_launch(id_launch: str) -> None:
    response = requests.get(
        url=f"https://api.spacexdata.com/v4/launches/{id_launch}")
    response_json = response.json()
    spacex_image_links = response_json["links"]["flickr"]["original"]
    for index, link in enumerate(spacex_image_links, start=1):
        download_image(url=link,
                       path="images/",
                       name=f"spacex_launch_{id_launch}_{index}")


def get_file_extensions(url: str) -> str:
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path)
    file = os.path.split(path)[-1]
    return os.path.splitext(file)[-1]

# print(get_file_extensions("https://example.com/txt/hello%20world.txt?v=9#python"))
    
"""
payload = {
    "api_key": NASA_API_KEY,
    "start_date": "2022-03-03"
}

response = requests.get("https://api.nasa.gov/planetary/apod", params=payload)
json_response = response.json()
for index, item in enumerate(json_response, start=1):
    download_image(url=item["url"], path="nasa_images/", name=f"nasa_image_{index}.jpeg")
"""
    

# fetch_spacex_launch("6243ad8baf52800c6e919252")

payload = {
    "api_key": NASA_API_KEY
}

response = requests.get("https://api.nasa.gov/EPIC/api/natural/images", params=payload)
json_response = response.json()
# pprint.pprint(json_response)
for index, item in enumerate(json_response):
    dt = parse(item["date"])
    download_epic_link = f"""https://api.nasa.gov/EPIC/archive/natural/\
{dt.strftime('%Y/%m/%d')}/png/{item['image']}.png\
?api_key={NASA_API_KEY}"""
    download_image(url=download_epic_link, path="epic_images/", name=f"{item['image']}.png")
