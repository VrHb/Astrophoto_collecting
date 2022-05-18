import os
import os.path
import pathlib

from urllib.parse import urlparse, unquote

import requests



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


def fetch_spacex_launch(id_launch: str) -> None:
    """fetch sacex launch by id_launch"""
    response = requests.get(
        url=f"https://api.spacexdata.com/v4/launches/{id_launch}")
    response_json = response.json()
    spacex_image_links = response_json["links"]["flickr"]["original"]
    for index, link in enumerate(spacex_image_links, start=1):
        download_image(
                url=link,
                path="spacex_images/",
                name=f"spacex_launch_{id_launch}_{index}{get_file_extensions(link)}"
                )


fetch_spacex_launch("6243ad8baf52800c6e919252")

