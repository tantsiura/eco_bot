from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboard.default import kb_lets_go
from loader import dp


@dp.message_handler(Command("lets_go"))
async def lets_go(message: types.Message):
    await message.answer(
        f'Выберите интересующий вас раздел. '
        f'Для выхода из меню используйте команду "/exit"',
        reply_markup=kb_lets_go,
        protect_content=True
        )
