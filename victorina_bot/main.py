import logging

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '5992006176:AAE-uprtVKllQKDLbi-2BDuf420C5GC7-ZM'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello")

@dp.message_handler(text="viktorina")
async def send_welcome(message: types.Message):
    await message.answer_poll(
                              question="Ronaldo qachon tug'ilgan?",
                              options=["1987", "1985", "1890"],
                              is_anonymous=False,
                              correct_option_id=1,
                              type="quiz"
        )

@dp.message_handler(text="viktorina2")
async def send_welcome(message: types.Message):
    await message.answer_poll(
                              question="Ispaniyani poytaxti?",
                              options=["Valensiya", "Barcelona", "Madrid"],
                              is_anonymous=False,
                              correct_option_id=2,
                              type="quiz"
        )

@dp.message_handler(text="viktorina3")
async def send_welcome(message: types.Message):
    await message.answer_poll(
                              question="Mars qachon ochilgan?",
                              options=["2020", "2021", "2022"],
                              is_anonymous=False,
                              correct_option_id=1,
                              type="quiz"
        )

@dp.message_handler(text="viktorina4")
async def send_welcome(message: types.Message):
    await message.answer_poll(
                              question="Apllening glavniy ofisi qayerda?",
                              options=["Bilmiman", "Ofisida", "Ikkala javob to'ri"],
                              is_anonymous=False,
                              correct_option_id=2,
                              type="quiz"
        )

@dp.message_handler(text="viktorina5")
async def send_welcome(message: types.Message):
    await message.answer_poll(
                              question="O'zbekistoning prezidenti kim?",
                              options=["Esimda yo'q", "O'zbekiston prezidenti yo'q", "Birinchi savol to'ri"],
                              is_anonymous=False,
                              correct_option_id=0,
                              type="quiz"
        )

@dp.message_handler(text="viktorina6")
async def send_welcome(message: types.Message):
    await message.answer_poll(
                              question="Benzemada nechta oltin top bor?",
                              options=["0", "1", "3"],
                              is_anonymous=False,
                              correct_option_id=1,
                              type="quiz"
        )

@dp.message_handler(text="viktorina7")
async def send_welcome(message: types.Message):
    await message.answer_poll(
                              question="Qaysi jamoa oxirgi bo'lib LCH ni yutdi?",
                              options=["Real Madrid", "Chelsea", "Manchester City"],
                              is_anonymous=False,
                              correct_option_id=2,
                              type="quiz"
        )

@dp.message_handler(text="viktorina8")
async def send_welcome(message: types.Message):
    await message.answer_poll(
                              question="Qaysi kino yaxshiroq?",
                              options=["Forsaj", "Garri Potter", "Bilmiman"],
                              is_anonymous=False,
                              correct_option_id=0,
                              type="quiz"
        )

@dp.message_handler(text="viktorina9")
async def send_welcome(message: types.Message):
    await message.answer_poll(
                              question="Disneyni qaysi Printsessiyasi yaxshiroq?",
                              options=["Rapunzel", "Belasnejka", "Eldor"],
                              is_anonymous=False,
                              correct_option_id=2,
                              type="quiz"
        )

@dp.message_handler(text="viktorina10")
async def send_welcome(message: types.Message):
    await message.answer_poll(
                              question="Hozir soat nechi?",
                              options=["17:00", "15:07", "18:23"],
                              is_anonymous=False,
                              correct_option_id=0,
                              type="quiz"
        )


    
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)