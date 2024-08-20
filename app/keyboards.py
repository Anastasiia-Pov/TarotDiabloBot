from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import (InlineKeyboardBuilder,
                                    ReplyKeyboardBuilder)

from config import tg_url, git_url
from tarot_cards.arcanas import major_arcanas, swords, wands, cups, pentacles


class CreateKeyboards:
    def __init__(self):

        self.help = ['Зачем все это?', 'Нашел ошибку?', 'Установить связь с создателем...']
        self.layouts = ['Карта Дня', 'Предсказание Будущего', 'Расклад - Совет', 'Пятикарточный Расклад', 'От Рая до Ада']
        self.choose_arcanas = ['Все Арканы', 'Только Старшие Арканы']
        self.about_arcanas = ['Старшие Арканы', 'Младшие Арканы', 'Мечи', 'Жезлы', 'Кубки', 'Пентакли']
        self.interpretation = ['Мечи', 'Жезлы', 'Кубки', 'Пентакли', 'Старшие Арканы']
        self.major_arcanas = major_arcanas
        self.swords = swords
        self.wands = wands
        self.cups = cups
        self.pentacles = pentacles
        self.links = {'Telegram': tg_url, 'Github': git_url}

        self.result_request = {'help_btn': self.help,
                               'layout_btn': self.layouts,
                               'choose_arcanas': self.choose_arcanas,
                               'about_arcanas': self.about_arcanas,
                               'interpretation': self.interpretation,
                               'major_arcanas': self.major_arcanas,
                               'swords': self.swords,
                               'wands': self.wands,
                               'cups': self.cups,
                               'pentacles': self.pentacles,
                               'links': self.links
                               }

    def create_inline_kb(self, request: str) -> InlineKeyboardMarkup:
        self.request = request
        # Инициализируем билдер
        kb_builder = InlineKeyboardBuilder()
        # Инициализируем список для кнопок
        buttons: list[InlineKeyboardButton] = []
        values = self.result_request[request]
        # словари со ссылками: проверка, если список - обычная сборка,
        # если словарь, есть ссылки (values в словаре), то указываем url при сборе кнопки
        if isinstance(values, list):
            for el in values:

                buttons.append(InlineKeyboardButton(text=el,
                                                    callback_data=el))
        else:
            for el in values:
                buttons.append(InlineKeyboardButton(text=el,
                                                    url=values[el]))
        kb_builder.row(*buttons, width=1 if len(values) <= 5 else 2)
        return kb_builder.as_markup()

    def create_reply_keyboard(self,
                              request) -> ReplyKeyboardMarkup:
        values = self.result_request[request]

        kb_builder = ReplyKeyboardBuilder()
        buttons: list[KeyboardButton] = [KeyboardButton(text=i) for i in values]
        kb_builder.row(*buttons, width=2)
        return kb_builder.as_markup(resize_keyboard=True, input_field_placeholder="Выберите раздел из меню ниже...")
