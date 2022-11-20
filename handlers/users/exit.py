from aiogram import types
from aiogram.types import InputFile, ReplyKeyboardRemove

from loader import dp


@dp.message_handler(text='/exit')
async def exit_send_video(message: types.Message):
    
    photo_bytes = InputFile(path_or_bytesio = 'media/exit.png')
    
    chat_id = message.from_user.id
    
    await dp.bot.send_photo(
        chat_id = chat_id, 
        photo = photo_bytes, 
        protect_content=True,
        reply_markup=ReplyKeyboardRemove())
