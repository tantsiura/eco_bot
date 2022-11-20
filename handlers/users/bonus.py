from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp
from states import bonus


@dp.message_handler(Command('bonus'))
async def bonus_(message: types.Message):
    await message.answer(f'''
🌎🌍🌏

Введи количество планет, необходимых для компенсации
твоего текущего потребления в формате целого числа (0-19) ...
''',
protect_content=True
)
    await bonus.test1.set()


@dp.message_handler(state = bonus.test1)
async def state(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.update_data(test1 = answer)
    data = await state.get_data()
    users_choice = int(data.get('test1'))

    category_1 = range(0,6)
    category_2 = range(7,12)
    category_3 = range(13,20)
    
    photo_bytes_1 = InputFile(path_or_bytesio = 'media/category_1.jpg')
    photo_bytes_2 = InputFile(path_or_bytesio = 'media/category_3.jpg')
    video_bytes = InputFile(path_or_bytesio = 'media/animation.gif.mp4')
    
    chat_id = message.from_user.id

    if users_choice in category_1:
        await dp.bot.send_photo(
            chat_id = chat_id,
            photo = photo_bytes_1,
            protect_content=True,
            caption = (f'''
🌿🌿🌿
Поздравляю!
Ты настоящий ценитель концепций ESG!
'''))
        
    elif users_choice in category_2:
        await dp.bot.send_video(
            chat_id = chat_id,
            video = video_bytes,
            protect_content=True,
            caption = (f'''
⚡️⚡️⚡️
Неплохо, но есть над чем задуматься!
Помни: ты всегда можешь вернуться к моим материалам
и изменить свои привычки к лучшему!
'''))
        
    elif users_choice in category_3:
        await dp.bot.send_photo(
            chat_id = chat_id,
            photo = photo_bytes_2,
            protect_content=True,
            caption = (f'''
‼️‼️‼️
Где-то грустит мой друг, робот WALL-E...

Я надеюсь, ты вернешься к материалам и сможешь взять из них
те идеи, которые подходят под твой ритм жизни.

Давай беречь нашу планету! 🥊💪🏻
'''))
        
    else:
        await message.answer(f'''
Введи количество планет из полученного результата теста.
Для выхода нажми: "/finish".
''')
    await state.finish()

    