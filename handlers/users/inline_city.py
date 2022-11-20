from aiogram import types
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboard.inline import ikb_city
from loader import dp


@dp.message_handler(text='Полезные ссылки 💻')
async def city(message: types.Message):
    await message.answer(f'''
Выбери интересующий тебя город. 
Для выхода используй команду "/exit"
''',
reply_markup = ikb_city,
protect_content=True
)


@dp.callback_query_handler(text='Москва 🌆')
async def city_Moscow(call: CallbackQuery):
    await call.message.answer(f'''
🌸🌸🌸
МОСКВА

www.instagram.com/sobirator.msk
https://vk.com/sobirator

♻️♻️♻️

Проект "СОБИРАТОР":

• оставьте заявку, курьер приедет бесплатно, заберет вторсырье

• можно сдать сырье следующих категорий:
 - стекло
 - металл
 - макулатура
 - ТетраПак
 - пластик 1,2, 4, 5, 6 видов
 - вещи (одежду, игрушки) для благотворительных фондов и для животных приютов

• в течение двух недель машина объезжает все районы Москвы 
• договориться о сборе можно на тот день, когда машина будет в вашем районе

Особенность проекта "Собиратор" в том, что он предоставляет 
возможность отследить движение вещей от момента сбора до
передачи фондам и переработчикам, а также рассказывает о том, 
что происходит на каждом из этапов 💰бесплатно. 

https://vk.com/razdelnysbor
🚖♻️✅

Проект "ЭКОТАКСИ":

• принимает вторсырье следующих категорий:
 - макулатуру
 - cтекло
 - пластик (1, 2, 4, 5, 6)
 - металл
 - батарейки
 - электронику
 - одежду
 - текстиль

•💰 Стоимость услуги для частного лица: 400 р. за 1 адрес, 
для организации: 600 р. за 1 адрес

https://vk.com/club145143771

🚖🌱🗑

Услуга "ЭкоВывоз" от проекта "Стекляшка Раздельный сбор":

• для жителей Бутово (Северного, Южного, Восточного), 
Парков 1, 2, 2Б и Щербинки

• вывозят в переработку:
 - стекло
 - электролом
 - твёрдый пластик (1- ПЭТ только бутылки от напитков 
 прозрачные и прозрачно цветные)
 - 5 – ПП, 6 – ПС, 2- ПНД, 4-ПВД, 3 – ПВХ (только пластиковые карты!)
 - мягкий пластик
 - пакеты (5-ПП кроме фольгированного, 2-ПНД, 4-ПВД, включая цветной)
 - ковры, постельное белье, одеяла, пледы, теплые вещи
 - сухой корм и в банках, ошейники, поводки, миски, вкусняшки для собак
 - медикаменты (бинты, шприцы, марлевые повязки и т.д.)
 для приюта собак "Щербинский"
    
• 💰 от 500 рублей

• жители других районов могут воспользоваться услугой 
по дополнительной договорённости.
    
http://zero.4fresh.ru
http://www.instagram.com/4fresh_rus  

👆🏼

Сервис Zero от онлайн-экомаркета 4fresh:

• курьер по Москве привезет ваши заказанные экотовары, 

• вывезет (в пределах МКАД) до 100 литров и 7 кг вторсырья
 – макулатура и пластик 1,2,4, типа, одежду

• Оператор по обращению с отходами -"Сфера Экологии"

• Одежду передают также в в благотворительные магазины Charity shop.
    
www.opti-com.ru/bumagovorot

🗑🗃📋

Для бизнеса: Бумаговорот (проект компании «Оптиком»):

• курьер привезет к вам в офис экологичные расходники, 
такие как бумажная продукция из вторсырья 
(туалетная бумага, полотенца, салфетки, протирочные материалы,
товары из переработанного пластика (канцтовары, пакеты для мусора),
биоразлагаемые моющие средства, одноразовая посуда из натуральных материалов

• заберет бумагу в переработку в спец.контейнерах, которые предоставляются 
бесплатно (❕заранее вмещает в себя до 20 кг бумаги, а значит вам не нужно 
выделять помещение для складирования бумаги)
    
https://rsbor-msk.ru

👆🏼👆🏼👆🏼

Отличный сайт по раздельному сбору в Москве,где можно найти 
информацию по сбору даже сложных для переработки материалов.
''',
protect_content=True, reply_markup=ReplyKeyboardRemove()
)


@dp.callback_query_handler(text='СПб 🏙')
async def city_SPB(call: CallbackQuery):
    await call.message.answer('''
🌲🌲🌲
СПб и ЛЕНИНГРАДСКАЯ ОБЛАСТЬ

https://vk.com/ecotaxispb
www.instagram.com/ecotaxi.spb

🚖♻️✅

Проект "ЭКОТАКСИ" Всеволода Василькиоти:

• территориальный охват:
в пределах КАД (+ Мурино и Ленинский пр. до Кронштадской площади)

• расчёт стоимости ведётся из объёма:
 - 3 сумки вторсырья типа «Лента», «Карусель»:
   всего за 300 руб. 
 - каждая следующая такая сумка: + 50 руб. 

• такси работает в:
 - понедельник
 - среду
 - пятницу 
 с 08:00 до 20:00

✅✅✅

Сервис экобиомагазина «БиоГрадПродукт»:

• курьер привезет заказ, заберет вторсырье
(бумага, стекло, пластик 1, 2, ТетраПак, аллюминиевые банки)

• 💰если заказ от 3000 р, то вывоз бесплатно – 
3 наполненных отходами строительных мешков или 
5 обычных пакетов. 

• если вторсырья больше лимита, то вывоз стоит 200 рублей
•  акция действует при заказе товара с доставкой по Санкт-Петербургу 
(перед сдачей нужно уведомить о желании сдать отходы)

📍📍📍
Точки сбора сырья для Ленинградской области

🔹 Всеволожск (https://vk.com/rsbor_vsevolojsk)

🔹 Гатчина (https://vk.com/rsbor_gatchina)

🔹 Кингисепп (https://vk.com/rsbor_kng)

🔹 Кириши (https://vk.com/kirishirsbor)

🔹 Колтуши (https://vk.com/rsbor_koltushi)

🔹 Кудрово (https://vk.com/rsbor_kudrovo)

🔹 Сосновый Бор (https://vk.com/eco_sbor)
''',
protect_content=True, reply_markup=ReplyKeyboardRemove()
)


@dp.callback_query_handler(text='Пермь 🌃')
async def city_Perm(call: CallbackQuery):
    await call.message.answer('''
🌷🌷🌷
ПЕРМЬ

https://vk.com/ecotaxiperm
www.instagram.com/ecotaxi_perm

🚖♻️✅

Проект "ЭКОТАКСИ": 

• принимается чистое и компактно уложенное вторсырье: 
 - стекло (рассортированное по цветам)
 - техника и провода
 - картон и макулатура
 - пластик (маркировка 1 и 2)
 - жесть и алюминий (по отдельности)
 - одежда

• такси вывозит вторсырье с периодичностью раз в 2 месяца

•  💰 стоимость услуги: 120-150 рублей

• минимальный к приёму вес: 10 кг

• заказать данную услугу можно за 4 дня то выезда

Для вызова экотакси необходимо заполнить заявку по ссылке ниже:
https://docs.google.com/forms/d/e/1FAIpQLSdHAHEBWAoSWcgplGOAL4utIxn3AGkYZZlYePYWyf5zUe3v6Q/viewform
''',
        protect_content=True, reply_markup=ReplyKeyboardRemove())