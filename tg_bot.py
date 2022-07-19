from aiogram import Bot, Dispatcher, executor, types
from config import token
import json



bot = Bot(token=token)
dp = Dispatcher(bot)


# @dp.message_handler(commands='start')
# async def start(message: types.Message):
#   await message.reply('Go to the Dream')


@dp.message_handler(commands='all_news')
async def get_all_news(message: types.Message):
  with open("news_dict.json") as file:
    news_dict = json.load(file)

  print(news_dict)


if __name__ == '__main__':
  executor.start_polling(dp)