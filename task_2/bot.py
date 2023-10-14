import asyncio
import logging
import pytz
import os
from datetime import datetime

from aiogram import Bot, Dispatcher, types

from google_file import GoogleSheets
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token=token)
dp = Dispatcher()
TZ = 'Europe/Moscow'

logging.basicConfig(
    level=logging.ERROR,
    filename='logs.log',
    format="%(asctime)s  %(message)s"
    )


@dp.message()
async def anything_message(msg: types.Message):
    try:
        user_id = msg.from_user.id
        login = msg.from_user.full_name
        time = datetime.now().astimezone(pytz.timezone(TZ))
        time = time.strftime('%Y-%m-%d %H:%M:%S')
        text = msg.text
        gs = GoogleSheets()
        gs.get_last_rows()
        last = gs.last_rows
        ranges = f'Test List!A{last+1}:C{last+1}'
        values = [
            [login, text, time]
        ]
        data = [{
            'range': ranges,
            'values': values
        }]
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }
        gs.add_new_info(body)
        await bot.send_message(user_id,
                               f'Hello, {login}, you can check google sheets')
    except Exception as e:
        logging.error(e)


async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    asyncio.run(main())
