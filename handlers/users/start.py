from aiogram import types

from loader import dp


@dp.message_handler(text='/start')
async def commands_start(message: types.Message):
    await message.answer(f'''
Привет, человек!

Я рад видеть тебя здесь! 🐦👋🏻
Меня зовут Кеша, я - Эко-бот, познакомлю тебя с основными принципами эко-составляющей ESG.

Здесь ты сможешь найти вебинары, рассчитать свой экослед, а также получить подборку самых полезных 
сайтов и ресурсов.

Ты готов? "/lets_go"!

Нам будет очень приятно получить от тебя обратную связь! 🥰
Для этого необходимо ввести команду "/feedback."
''',
protect_content=True
)
