"""
Pocket Dictionary
"""
import logging
from aiogram import Bot, Dispatcher, executor, types
from oxfordLookUp import get_definitions
from googletrans import Translator

translator = Translator()

API_TOKEN = '5399942772:AAEWUxt6j1YidYHi0RqfhFHPKjXfP7JO3eY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Assalomu aleykum, Welcome to Pocket | Dictionary!.😉")


@dp.message_handler(commands='help')
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await message.reply("To start enter any word for its definitions or a sentence to translate to uzb.")


@dp.message_handler()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.answer(translator.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text

        lookup = get_definitions(word_id)
        if lookup:
            await message.answer(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
            if lookup.get('audio'):
                await message.answer_audio(lookup['audio'])
        else:
            await message.reply("Bunday so'z topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
