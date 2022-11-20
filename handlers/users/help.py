from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('help'))
async def commands_help(message: types.Message):
    await message.answer(
        f'⏩ Для начала работы с ботом нажми "/start".'
        )

@dp.message_handler()
async def commands_help(message: types.Message):
    await message.answer(
        f'⏩ Для начала работы с ботом нажми "/start".'
        )
