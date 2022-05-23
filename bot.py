import os
import time

from dotenv import load_dotenv

import asyncio
import telegram

PHOTO_DIR = "images"


def get_filenames_list() -> list[str] | None:
    """Get list filenames of photos from directory"""
    photo_dir = os.walk(PHOTO_DIR)
    for item in photo_dir:
        list_filenames = item[2]
        return list_filenames
   

async def main():
    bot = telegram.Bot(str(os.getenv("BOT_TOKEN")))
    async with bot:
        await bot.send_message(
                text="Hi There, a'm a Space Owl!",
                chat_id=str(os.getenv("CHAT_ID"))
        )
        await bot.send_photo(
            chat_id=str(os.getenv("CHAT_ID")),
            photo=open(f"images/{file}", "rb")
        )


if __name__ == "__main__":
    load_dotenv()
    list_files = get_filenames_list()
    while True:
        for file in list_files:
            asyncio.run(main())
            time.sleep(int(os.getenv("LATENCY")))

