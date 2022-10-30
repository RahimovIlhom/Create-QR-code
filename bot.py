import logging

import aiogram
from aiogram import Bot, Dispatcher, executor, types
from makeQR import make_qr


API_TOKEN = '5647979180:AAGURWpKXH8Kuv3R4EGwyj2jzSkpumjpqhM'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Assalomu alaykum. Create QR Code botimizga xush kelibsiz!")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):

    await message.reply("Botimizdan foydalanish uchun link yoki telegram username yuboring va bot sizga QRcode yasab beradi!")


@dp.message_handler()
async def send_qr_image(message: types.Message):

    url = message.text
    image = make_qr(url)

    if image == False:
        await message.reply("Bunday url ga QR Codedan foydalana olmaysiz!")
    else:
        photo = aiogram.types.input_file.InputFile(image)
        await bot.send_photo(chat_id=message.chat.id, photo=photo)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)