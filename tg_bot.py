from aiogram import Bot, Dispatcher, executor, types
from config import token
import datetime
import json



bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


# @dp.message_handler(commands='start')
# async def start(message: types.Message):
#   await message.reply('Go to the Dream')


@dp.message_handler(commands='all_news')
async def get_all_news(message: types.Message):
  with open("news_dict.json") as file:
    news_dict = json.load(file)

  for k, v in sorted(news_dict.items()):
    news = f"<b>{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}</b>\n" \
      f"<u>{v['article_title']}</u>\n" \
      f"<code>{v['article_desc']}</code>\n" \
      f"{v['article_url']}"

    await message.answer(news)





if __name__ == '__main__':
  executor.start_polling(dp)