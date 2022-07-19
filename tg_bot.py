from aiogram import Bot, Dispatcher, executor, types
from config import token
import datetime
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

  for k, v in sorted(news_dict.items()):
    news = f"{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}\n" \
      f"{v['article_title']}\n" \
      f"{v['article_desc']}\n" \
      f"{v['article_url']}"

    await message.answer(news)



if __name__ == '__main__':
  executor.start_polling(dp)