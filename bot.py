import os
import time
import random

from dotenv import load_dotenv

import asyncio
import telegram



load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

LATENCY = os.getenv("LATENCY")


def choice_photo() -> str | None:
    """Choice photo from directory"""
    photos = os.walk("epic_images")
    for photo in photos:
        random_photo = random.choice(photo[2])
        return random_photo
   

async def main():
    bot = telegram.Bot(str(BOT_TOKEN))
    async with bot:
        await bot.send_message(
                text="Hi There, a'm a Space Owl!", 
                chat_id=-642797640
        )
        await bot.send_photo(
            chat_id=-642797640, 
            photo=open(f"epic_images/{choice_photo()}", "rb")
            )

if __name__ == "__main__":
    while True:
        asyncio.run(main())
        time.sleep(int(LATENCY))