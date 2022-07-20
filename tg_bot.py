from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from config import token
import datetime
import json
from main import check_news_update



bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
  start_buttons = ['All mews', 'Last five news', 'Freshh!' ]
  keyboard = types.ReplyKeyboardMarkup()
  keyboard.add(*start_buttons)
  
  await message.answer('Lent news//', reply_markup=keyboard)


@dp.message_handler(commands='all_news')
async def get_all_news(message: types.Message):
  with open("news_dict.json") as file:
    news_dict = json.load(file)

  for k, v in sorted(news_dict.items()):
    # news = f"<b>{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}</b>\n" \
    #   f"<u>{v['article_title']}</u>\n" \
    #   f"<code>{v['article_desc']}</code>\n" \
    #   f"{v['article_url']}"
    
    # news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
    #   f"{hunderline(v['article_title'])}\n" \
    #   f"{hcode(v['article_desc'])}\n" \
    #   f"{hlink(v['article_title'], v['article_url'])}"

    news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
      f"{hlink(v['article_title'], v['article_url'])}"

    await message.answer(news)



@dp.message_handler(commands='last_five')
async def get_last_five_news(message: types.Message):
  with open("news_dict.json") as file:
    news_dict = json.load(file)

  for k, v in sorted(news_dict.items())[-5:]:
    news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
      f"{hlink(v['article_title'], v['article_url'])}"

    await message.answer(news)


@dp.message_handler(commands='fresh_news')
async def get_fresh_news(message: types.Message):
  fresh_news = check_news_update()

  if len(fresh_news) >= 1:
    for k, v in sorted(fresh_news.items()):
      news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
        f"{hlink(v['article_title'], v['article_url'])}"

      await message.answer(news)

  else:
    await message.answer('not news now')








if __name__ == '__main__':
  executor.start_polling(dp)