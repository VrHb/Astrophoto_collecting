import os
import pprint

from dotenv import load_dotenv

import asyncio
import telegram


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    bot = telegram.Bot(str(BOT_TOKEN))
    async with bot:
        pprint.pprint(await bot.get_me())
        pprint.pprint((await bot.get_updates())[7])
        await bot.send_message(
                text="Hi There, a'm a Space Owl!", 
                chat_id=-642797640
        )

if __name__ == "__main__":
    asyncio.run(main())

