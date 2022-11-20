from aiogram import types
from aiogram.types import InputFile, Message, ReplyKeyboardRemove

from loader import dp


@dp.message_handler(text='Вебинар: Правило 4R ♻️')
async def send_video(message:Message):
    chat_id = message.from_user.id

    video_bytes = InputFile(path_or_bytesio = 'media/project.mp4')

    await dp.bot.send_video(
        chat_id = chat_id, 
        video = video_bytes, 
        protect_content=True,
        caption = (f'''
🚮❔♻️

Данный вебинар позволит тебе узнать больше о маркировке, а также о правиле 4R.
'''
), reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text='Вебинар: Сортировка мусора 🗑')
async def send_video(message:Message):
    chat_id = message.from_user.id

    video_bytes = InputFile(path_or_bytesio = 'media/project2.mp4')

    await dp.bot.send_video(
        chat_id = chat_id, 
        video = video_bytes, 
        protect_content=True,
        caption = (f'''
🗑👀✅

Данный вебинар позволит тебе узнать больше о сортировке и переработке мусора.
'''
), reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text='Рассчитай свой экослед 🐾')
async def buttons_test(message: types.Message):
    await dp.bot.send_message(
        message.from_user.id, 
        text = (f'''
https://www.footprintcalculator.org/

✅✅✅

Воспользовавшись калькулятором от NFP Global Footprint 
Network, ты сможешь узнать, какое влияние оказываешь на окружающую среду.

🍀🍀🍀
Поделись результатом и получи свой бонус: "/bonus"!
'''),
protect_content=True, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text='Greenpeace: Карта сбора отходов 🌲')
async def buttons_test(message: types.Message):
    await dp.bot.send_message(
        message.from_user.id,
        protect_content=True,
        text = (f'''
https://recyclemap.ru/

📍📍📍

На портале Recyclemap ты сможешь найти:

• самые ближайшие точки для сдачи сырья разных категорий
• информацию о компании, обслуживающей данную точку
• режим работы данной точки
• какие категории отходов принимает данный пункт
• для каких конечных целей осуществляется сбор сырья
'''
), reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text='Карта эко-инициатив РФ 📨')
async def buttons_test(message: types.Message):
    await dp.bot.send_message(
        message.from_user.id,
        protect_content=True,
        text = (f'''
https://rsbor-msk.ru/map_eco_active/

👆🏼👆🏼👆🏼

На портале "Карта экологических инициативных групп России 
и стран СНГ" ты сможешь не только найти подробную информацию о действующих волонтёрских 
движениях, но и предложить свои идеи.
'''
), reply_markup=ReplyKeyboardRemove())
            


        

