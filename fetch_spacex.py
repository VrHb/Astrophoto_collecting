import requests

from file_operations import download_image, get_file_extension_from_link

LAUNCH_ID = "6243ad8baf52800c6e919252"
IMAGES_DIR = "images/"


def fetch_spacex_launch(launch_id: str) -> None:
    """fetch sacex launch by launch_id"""
    response = requests.get(
        url=f"https://api.spacexdata.com/v4/launches/{launch_id}"
    )
    spacex_launches_list = response.json()
    spacex_image_links = spacex_launches_list["links"]["flickr"]["original"]
    for index, link in enumerate(spacex_image_links, start=1):
        download_image(
            url=link,
            path=IMAGES_DIR,
            name=f"spacex_launch_{launch_id}_{index}{get_file_extension_from_link(link)}"
        )


def main():
    fetch_spacex_launch(LAUNCH_ID)

if __name__ == "__main__":
    main()

