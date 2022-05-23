import os
import time

from dotenv import load_dotenv

import asyncio
import telegram

PHOTO_DIR = "images"


def get_filenames() -> list[str] | None:
    """Get list filenames of photos from directory"""
    photo_dir = os.walk(PHOTO_DIR)
    for item in photo_dir:
        list_photos = item[2]
        return list_photos
   

async def main():
    bot = telegram.Bot(str(os.getenv("BOT_TOKEN")))
    async with bot:
        await bot.send_message(
                text="Hi There, a'm a Space Owl!",
                chat_id=str(os.getenv("CHAT_ID"))
        )
        await bot.send_photo(
            chat_id=str(os.getenv("CHAT_ID")),
            photo=open(f"images/{photo}", "rb")
        )


if __name__ == "__main__":
    load_dotenv()
    list_photos = get_filenames()
    while True:
        for photo in list_photos:
            asyncio.run(main())
            time.sleep(int(os.getenv("LATENCY")))

