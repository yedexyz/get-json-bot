import json

from aiogram import Bot, Dispatcher, types
import logging
import os

from aiogram.types import ContentTypes
from aiogram.utils import executor

API_TOKEN: str = os.environ["API_TOKEN"]  # 1231231231:SALAD12_SAddamsASASJDJAKSDJKSADASs

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=ContentTypes.ANY)
async def handle(message: types.Message):
    await message.answer(json.dumps(json.loads(message.as_json()), indent=4))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
