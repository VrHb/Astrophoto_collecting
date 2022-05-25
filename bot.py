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
   

async def main(bot_token: str | None, chat_id: str | None):
    bot = telegram.Bot(bot_token)
    async with bot:
        await bot.send_message(
                text="Hi There, a'm a Space Owl!",
                chat_id=chat_id
        )
        await bot.send_photo(
            chat_id=chat_id,
            photo=open(f"images/{file}", "rb")
        )


if __name__ == "__main__":
    load_dotenv()
    
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    LATENCY = int(os.getenv("LATENCY"))
    
    list_files = get_filenames_list()
    
    while True:
        for file in list_files:
            asyncio.run(main(bot_token=BOT_TOKEN, chat_id=CHAT_ID))
            time.sleep(LATENCY)

