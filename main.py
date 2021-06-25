"""
This is a echo bot.
It echoes any incoming text messages.
"""
import base64
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import API_TOKEN
from msg_proccess import process

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

inline_btn_1 = InlineKeyboardButton('more', callback_data='button_more')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)


def get_image(search_query, best):
    response = process(search_query=search_query, best=best)
    image_64_decode = base64.b64decode(response['outputs'])
    return image_64_decode


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm MemesBot!")


@dp.message_handler()
async def echo(message: types.Message):
    search_query = message.text
    # response = process(search_query)
    # image_64_decode = base64.b64decode(response['outputs'])
    image_64_decode = get_image(search_query, best=True)
    await message.reply_photo(image_64_decode, caption=search_query, reply_markup=inline_kb1)


@dp.callback_query_handler(lambda c: c.data == 'button_more')
async def process_callback_button_more(callback_query: types.CallbackQuery):
    search_query = callback_query.message.md_text
    # response = process(search_query)
    # image_64_decode = base64.b64decode(response['outputs'])
    image_64_decode = get_image(search_query=search_query, best=False)
    await callback_query.message.reply_photo(image_64_decode, caption=search_query,
                                             reply_markup=inline_kb1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
