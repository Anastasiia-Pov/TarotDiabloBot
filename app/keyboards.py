from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import tg_url, git_url
from tarot_cards.arcanas import major_arcanas, swords, wands, cups, pentacles


# /help
help_btn = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Зачем все это?'),
     KeyboardButton(text='Нашел ошибку?')],
    [KeyboardButton(text='Установить связь с создателем...')]
    ],
                              resize_keyboard=True,
                              input_field_placeholder="Выбери из предложенного")


layout_btn = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Карта Дня')],
    [KeyboardButton(text='Предсказание Будущего'),
     KeyboardButton(text='Расклад - Совет')],
    [KeyboardButton(text='Пятикарточный Расклад'),
     KeyboardButton(text='От Рая до Ада')]
    ],
                              resize_keyboard=True,
                              input_field_placeholder="Выберите расклад из меню ниже")


# установить связь с создателем
git_tg = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Telegram',
                          url=tg_url)],
    [InlineKeyboardButton(text='Github',
                          url=git_url)]])


new_layout_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Карта Дня',
                          callback_data='Карта Дня')],
    [InlineKeyboardButton(text='Предсказание Будущего',
                          callback_data='Предсказание Будущего')],
    [InlineKeyboardButton(text='Расклад - Совет',
                          callback_data='Расклад - Совет')],
    [InlineKeyboardButton(text='Пятикарточный Расклад',
                          callback_data='Пятикарточный Расклад')],
    [InlineKeyboardButton(text='От Рая до Ада',
                          callback_data='От Рая до Ада')]])

choose_arcanas = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Все Арканы',
                          callback_data='Все Арканы')],
    [InlineKeyboardButton(text='Только Старшие Арканы',
                          callback_data='Только Старшие Арканы')]])


interpret_arcanas = ReplyKeyboardMarkup(keyboard=[
                                                  [KeyboardButton(text='Старшие Арканы')],
                                                  [KeyboardButton(text='Мечи'),
                                                   KeyboardButton(text='Жезлы')],
                                                  [KeyboardButton(text='Кубки'),
                                                   KeyboardButton(text='Пентакли')]],
                                        resize_keyboard=True,
                                        input_field_placeholder="Выберите группу арканов")


def create_inline_kb(request: str,
                     *args: str,
                     **kwargs: str) -> InlineKeyboardMarkup:
    arcanas = {'Старшие Арканы': major_arcanas,
               'Мечи': swords,
               'Жезлы': wands,
               'Кубки': cups,
               'Пентакли': pentacles,
               'about_arcanas': ['Старшие Арканы', 'Младшие Арканы', 'Мечи', 'Жезлы', 'Кубки', 'Пентакли']}
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []
    for el in arcanas[request]:
        buttons.append(InlineKeyboardButton(
                text=el,
                callback_data=el))
    kb_builder.row(*buttons, width=2)
    return kb_builder.as_markup()
