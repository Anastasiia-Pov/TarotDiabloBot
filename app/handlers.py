from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, FSInputFile
from aiogram.filters import ChatMemberUpdatedFilter, KICKED
from aiogram.types import ChatMemberUpdated, CallbackQuery
from aiogram.filters import BaseFilter
import asyncio
import re
from aiogram.methods.send_photo import SendPhoto
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext

from app.performing_layout import perform_layout
from tarot_cards.arcanas import all_arcanas
from tarot_cards.arcanas_interpretation import arcanas_interpretation
from app.messages import layout_questions
from config import support
from app.keyboards import CreateKeyboards
import app.messages as mg


router = Router()


create_keybords = CreateKeyboards()


class FSMAskQuestion(StatesGroup):
    question = State()
    layout = State()
    arcanas = State()


# Команда "/start"
@router.message(Command('start'))
async def start(message: Message):
    await message.answer('''
Здравствуй, странник.
Что привело тебя ко мне?
У тебя есть вопросы, на которые ты хочешь узнать ответ? Давай раскинем карты? - /new_layout
Могу рассказать о расскладах, которыми владею. - /about_layouts
Или же ты новичок во всем этом и хочешь узнать основы? - /how_to_use
''')


# Команда "/about_layouts - о раскладах"
@router.message(Command('how_to_use'))
async def how_to_use(message: Message):
    await message.answer(text=mg.how_to_use)


# Команда "/about_layouts - о раскладах"
@router.message(Command('about_layouts'))
async def about_layout(message: Message):
    await message.answer(text=mg.layouts['about_layouts'],
                         reply_markup=create_keybords.create_reply_keyboard('layout_btn'))


# layout ReplyKeyboardMarkup - Информация о раскладе 'Карта Дня'
@router.message(F.text == 'Карта Дня')
async def card_of_the_day_spread_info(message: Message):
    await message.answer(
        mg.layouts['card_of_the_day'],
        parse_mode='html'
                        )


# layout ReplyKeyboardMarkup - Информация о раскладе 'Предсказание будущего'
@router.message(F.text == 'Предсказание Будущего')
async def scrying_the_future_spread_info(message: Message):
    await message.answer(
        mg.layouts['scrying_the_future_spread'],
        parse_mode='html'
                        )
    file_path = FSInputFile('cards_layouts/scrying_the_future_spread.png')
    await message.bot.send_photo(chat_id=message.chat.id,
                                 photo=file_path)


# layout ReplyKeyboardMarkup - Информация о раскладе 'Расклад-совет'
@router.message(F.text == 'Расклад - Совет')
async def advice_spread_info(message: Message):
    await message.answer(
        mg.layouts['advice_spread'],
        parse_mode='html'
                        )
    file_path = FSInputFile('cards_layouts/advice_spread.png')
    await message.bot.send_photo(chat_id=message.chat.id,
                                 photo=file_path)


# layout ReplyKeyboardMarkup - Информация о раскладе 'Пятикарточный расклад'
@router.message(F.text == 'Пятикарточный Расклад')
async def five_card_overview_spread_info(message: Message):
    await message.answer(
        mg.layouts['five_card_overview_spread'],
        parse_mode='html'
                        )
    file_path = FSInputFile('cards_layouts/five_card_overview_spread.png')
    await message.bot.send_photo(chat_id=message.chat.id,
                                 photo=file_path)


# layout ReplyKeyboardMarkup - Информация о раскладе 'От Рая до Ада'
@router.message(F.text == 'От Рая до Ада')
async def from_heavens_to_hell_spread_info(message: Message):
    await message.answer(
        mg.layouts['from_heavens_to_hell_spread'],
        parse_mode='html'
                        )
    file_path = FSInputFile('cards_layouts/from_heavens_to_hell_spread.png')
    await message.bot.send_photo(chat_id=message.chat.id,
                                 photo=file_path)


# Команда "/help"
@router.message(Command('help'))
async def help_btn(message: Message):
    await message.answer(text="Что ты хочешь узнать?",
                         reply_markup=create_keybords.create_reply_keyboard('help_btn'))  # ReplyKeyboardMarkup


# help ReplyKeyboardMarkup - Информация о проекте
@router.message(F.text == 'Зачем все это?')
async def project_info(message: Message):
    await message.answer(mg.about_project,
                         parse_mode='html')


# help ReplyKeyboardMarkup - Сообщить об ошибке
@router.message(F.text == 'Нашел ошибку?')
async def error_inform(message: Message):
    await message.answer(f'Сообщите нам о ней в группе поддержки: {support}')


# help ReplyKeyboardMarkup - Информация о проекте
@router.message(F.text == 'Установить связь с создателем...')
async def contact_creator(message: Message):
    await message.answer(text='Каким способом?',
                         reply_markup=create_keybords.create_inline_kb('links'))


# Команда "/about_arcanas - больше информации об арканах: Cтаршие, младшие, мечи, жезлы, чаши, пентакли"
@router.message(Command('about_arcanas'))
async def about_arcanas(message: Message):
    keyboard = create_keybords.create_inline_kb('about_arcanas')
    await message.answer(text='О каких арканах хотите узнать больше?',
                         reply_markup=keyboard)


# Команда "/about_arcanas - больше информации об арканах: Cтаршие, младшие, мечи, жезлы, чаши, пентакли"
@router.callback_query(F.data.in_(mg.about_arcanas))
async def about_arcana_1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(f'Вы выбрали <b>{callback.data}</b>',
                                  parse_mode='html')
    await callback.message.answer(text=f"{mg.about_arcanas[callback.data]}",
                                  parse_mode='html')
    # await callback.message.delete()


# Этот хэндлер будет срабатывать на команду /new_layout
@router.message(Command('new_layout'), StateFilter(default_state))
async def new_layout(message: Message, state: FSMContext):
    await message.answer(text="<b>Задайте интересующий вас вопрос...</b>",
                         parse_mode='html')
    await state.set_state(FSMAskQuestion.question)


# Этот хэндлер будет срабатывать после команды /new_layout - пользователь задает вопрос
@router.message(StateFilter(FSMAskQuestion.question))
async def process_question(message: Message, state: FSMContext):
    await state.update_data(question=message.text)
    await message.answer(text="<b>Ваш вопрос услышан...</b>",
                         parse_mode='html')
    await state.set_state(FSMAskQuestion.layout)
    await message.answer(text="<b>Какой расклад предпочтете?</b>",
                         parse_mode='html',
                         reply_markup=create_keybords.create_inline_kb('layout_btn'))


# Этот хэндлер будет срабатывать после команды /new_layout - выбор расклада
@router.message(StateFilter(FSMAskQuestion.question))
async def process_layout(message: Message, state: FSMContext):
    await message.answer(text="<b>Какой расклад предпочтете?</b>",
                         parse_mode='html',
                         reply_markup=create_keybords.create_inline_kb('layout_btn'))

    # Устанавливаем состояние ожидания выбора расклада
    await state.set_state(FSMAskQuestion.layout)


# Этот хэндлер будет срабатывать на нажатие кнопки при
# выборе расклада и переводить в состояние выбора арканов
@router.callback_query(StateFilter(FSMAskQuestion.layout),
                       F.data.in_(layout_questions))
async def process_arcanas(callback: CallbackQuery,
                          state: FSMContext):
    await state.update_data(layout=callback.data)
    await callback.answer()
    await callback.message.answer(f'Вы выбрали расклад: <b>{callback.data}</b>',
                                  parse_mode='html')
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer(text="<b>Какие арканы будем использовать для расклада?</b>",
                                  parse_mode='html',
                                  reply_markup=create_keybords.create_inline_kb('choose_arcanas'))
    # Устанавливаем состояние ожидания выбора арканов
    await state.set_state(FSMAskQuestion.arcanas)


# Функция расклада
# Этот хэндлер будет срабатывать после команды /new_layout - выбор расклада - выбор арканов
@router.callback_query(StateFilter(FSMAskQuestion.arcanas),
                       F.data.in_(['Все Арканы', 'Только Старшие Арканы']))
async def finish_input_for_layout(callback: CallbackQuery,
                                  state: FSMContext):
    await state.update_data(arcanas=callback.data)
    await callback.message.answer(f'Вы выбрали <b>{callback.data}</b> для расклада',
                                  parse_mode='html')
    await callback.message.delete()
    data = await state.get_data()
    await callback.message.answer('''Выполняю расклад 🔮\nОжидайте...''')
    await asyncio.sleep(4)
    result = perform_layout(data)
    # проверка длины сообщения
    if len(result) >= 4096:
        result = re.split('<b>6.-9.', result)
        await callback.message.answer(text=result[0],
                                      parse_mode='html')
        await callback.message.answer(text='<b>6.-9.' + result[1],
                                      parse_mode='html')
    else:
        await callback.message.answer(text=result,
                                      parse_mode='html')
    # Завершаем машину состояний
    await state.clear()


# Вызов фукнции интерпретация отдельной карты - /interpretation
@router.message(Command('interpretation'))
async def interpretation(message: Message):
    await message.answer(text='Карту какой масти проинтерпритировать?',
                         reply_markup=create_keybords.create_reply_keyboard('interpretation'))


# Вызов фукнции интерпретация отдельной карты в Старших Арканах
@router.message(F.text == 'Старшие Арканы')
async def interpretation_majors(message: Message):
    keyboard = create_keybords.create_inline_kb('major_arcanas')
    await message.answer(text='Выберите Аркан',
                         reply_markup=keyboard)


# Вызов фукнции интерпретация отдельной карты в Мечах
@router.message(F.text == 'Мечи')
async def interpretation_swords(message: Message):
    keyboard = create_keybords.create_inline_kb('swords')
    await message.answer(text='Выберитер Аркан',
                         reply_markup=keyboard)


# Вызов фукнции интерпретация отдельной карты в Жезлах
@router.message(F.text == 'Жезлы')
async def interpretation_wands(message: Message):
    keyboard = create_keybords.create_inline_kb('wands')
    await message.answer(text='Выберитер Аркан',
                         reply_markup=keyboard)


# Вызов фукнции интерпретация отдельной карты в кубках
@router.message(F.text == 'Кубки')
async def interpretation_cups(message: Message):
    keyboard = create_keybords.create_inline_kb('cups')
    await message.answer(text='Выберитер Аркан',
                         reply_markup=keyboard)


# Вызов фукнции интерпретация отдельной карты в Пентаклях
@router.message(F.text == 'Пентакли')
async def interpretation_pentacles(message: Message):
    keyboard = create_keybords.create_inline_kb('pentacles')
    await message.answer(text='Выберитер Аркан',
                         reply_markup=keyboard)


# Вызов фукнции интерпретация отдельной карты в двух смыслах
@router.callback_query(F.data.in_(all_arcanas))
async def reading_arcana(callback: CallbackQuery):
    await callback.message.answer(f'Вы выбрали аркан <b>{callback.data}</b>',
                                  parse_mode='html')
    await callback.message.answer(f'Прямое значение: {list(arcanas_interpretation[callback.data].values())[0]}',
                                  parse_mode='html')
    await callback.message.answer(f'Перевернутое значение: {list(arcanas_interpretation[callback.data].values())[1]}',
                                  parse_mode='html')
    await callback.message.delete()


# Хэндлер
# если введен текст с клавиатуры - бот попросит выбрать команду из меню
@router.message(F.text)
async def random_text(message: Message):
    await message.answer(text='''Не совсем понимаю о чем вы.
Выберете команду из меню, чтобы мы могли продолжить общение.''')
