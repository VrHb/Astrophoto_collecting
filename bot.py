import asyncio
import os
import time

import telegram
from dotenv import load_dotenv
from telegram._utils.types import FileInput

PHOTO_DIR = "images"

def get_filenames_list() -> list[str] | None:
    """Get list filenames of photos from directory"""
    photo_dir = os.walk(PHOTO_DIR)
    for item in photo_dir:
        filenames = item[2]
        return filenames
   

async def main(file: FileInput):
    load_dotenv()
    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    latency = int(os.getenv("LATENCY"))
    bot = telegram.Bot(bot_token)
    async with bot:
        await bot.send_message(
            text="Hi There, a'm a Space Owl!",
            chat_id=chat_id
        )
        await bot.send_photo(
            chat_id=chat_id,
            photo=file
        )
    time.sleep(latency)

if __name__ == "__main__":
    list_files = get_filenames_list()
    while True:
        for file in list_files:
            with open(f"images/{file}", "rb") as file:
                file_input = file.read()
            asyncio.run(
                main(file=file_input)
            )

