from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_lets_go = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Вебинар: Правило 4R ♻️'),
            KeyboardButton(text='Вебинар: Сортировка мусора 🗑'),
        ],
        [
            KeyboardButton(text='Рассчитай свой экослед 🐾'),
            KeyboardButton(text='Полезные ссылки 💻'),
        ],
        [
            KeyboardButton(text='Greenpeace: Карта сбора отходов 🌲'),
            KeyboardButton(text='Карта эко-инициатив РФ 📨'),
        ],
    ], 
    resize_keyboard=True
)
