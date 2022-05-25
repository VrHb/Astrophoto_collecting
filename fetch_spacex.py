import requests

from file_operations import download_image, getting_file_extension_from_link

ID_LAUNCH = "6243ad8baf52800c6e919252"
IMAGES_DIR = "images/"


def fetch_spacex_launch(id_launch: str) -> None:
    """fetch sacex launch by id_launch"""
    response = requests.get(
        url=f"https://api.spacexdata.com/v4/launches/{id_launch}"
    )
    spacex_launches_list = response.json()
    spacex_image_links = spacex_launches_list["links"]["flickr"]["original"]
    for index, link in enumerate(spacex_image_links, start=1):
        download_image(
            url=link,
            path=IMAGES_DIR,
            name=f"spacex_launch_{id_launch}_{index}{getting_file_extension_from_link(link)}"
        )


def main():
    fetch_spacex_launch(ID_LAUNCH)

if __name__ == "__main__":
    main()

