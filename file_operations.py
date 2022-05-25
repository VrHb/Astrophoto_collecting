import os.path
import pathlib
from urllib.parse import urlparse, unquote

import requests



def download_image(url: str, path: str, name: str) -> None:
    """Download image from url"""
    response = requests.get(url)
    response.raise_for_status()
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    with open(f"{path}{name}", "wb") as file:
        file.write(response.content)


def getting_file_extension_from_link(url: str) -> str:
    """Getting file extension from url"""
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path)
    file = os.path.split(path)[-1]
    return os.path.splitext(file)[-1]

