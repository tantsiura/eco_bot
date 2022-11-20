from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ikb_city = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text = 'Москва 🌆', callback_data = 'Москва 🌆'),
                                        InlineKeyboardButton(text = 'СПб 🏙', callback_data = 'СПб 🏙'),
                                        InlineKeyboardButton(text = 'Пермь 🌃', callback_data = 'Пермь 🌃'),
                                    ]
                                ])
