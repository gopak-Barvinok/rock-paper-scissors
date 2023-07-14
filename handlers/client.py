from aiogram import types, Dispatcher
from createbot import bot
# from db.sql_db import sql_add_command
from keyboards import button_par, button_move, button_move2
#from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ContentType
from handlers.rules import check_winner

reserve_slots = []

#Запускаємо бот
async def start_bot(message: types.Message):
    pass

async def hello_message(message: types.Message):
    for member in message.new_chat_members:
        if member.id == bot.id:
            await message.answer("""

Приветствуем! 
Предлгаем вам поучаствовать в уличной забаве Цу-е-фа или Чу-Ва-Чи не выходя из дома или работы!

Для игры на VQR монеты необходимо зарегистрироваться в лс у бота!
Игра без регистрации - Быстрая игра.

Быстрая игра - Перейти в лс - Играть на VQR

""", reply_markup=button_par)


async def start_game(message: types.Message):
    await message.answer("""
Камень-ножницы-бумага
                         
*Обратите внимание!*
Играть на VQR можно только пользователям, зарегестрированным в боте и имеющим, при этом, сделать ставку этой монетой.
                         
Выберите тип игры:
""", reply_markup=button_par, parse_mode=types.ParseMode.MARKDOWN)

async def quick_game(callback: types.CallbackQuery):
    await callback.message.answer("Сделайте ход", reply_markup=button_move)

async def make_move(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["round_1"] = reserve_slots.append({callback.from_user.full_name: {callback.from_user.id: str(callback.data)}})
    await callback.message.answer(f"*{callback.from_user.full_name}* сделал ход\nСделать ответный ход: ", 
                                  parse_mode=types.ParseMode.MARKDOWN, reply_markup=button_move2)

async def make_second_move(callback: types.CallbackQuery, state: FSMContext):
    result_1 = dict(reserve_slots[0])
    result_2 = {callback.from_user.full_name: {callback.from_user.id: str(callback.data)}}
    result = await check_winner(result_1, result_2)
    if result:
        await callback.message.answer(f"Победитель - *{result[0]}*", reply_markup=button_par, parse_mode=types.ParseMode.MARKDOWN)
        await state.finish()
    else:
        await callback.message.answer("Ничья, сделайте ход снова", reply_markup=button_move)

async def vqr_game(callback: types.CallbackQuery):
    await callback.answer("Игра на VQR")

async def get_rules(message: types.Message):
    await message.answer("""

*Камень* бьёт ножницы и колодец.
                         
*Бумага* бьёт камень и колодец.
                         
*Ножницы* бьют бумагу.
                         
*Колодец* бьёт ножницы.
                         
""", parse_mode=types.ParseMode.MARKDOWN)

#"Реєстрація" обробників повідомлень (хендлерів)
def rhc(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start', 'help'])
    dp.register_message_handler(start_game, commands=['start_game_knb'])
    dp.register_message_handler(get_rules, commands=['game_knb_get_rules'])
    dp.register_message_handler(hello_message, content_types=types.ContentType.NEW_CHAT_MEMBERS)
    dp.register_callback_query_handler(quick_game, Text(startswith="quick_game"))
    dp.register_callback_query_handler(vqr_game, Text(startswith="vqr_game"))
    dp.register_callback_query_handler(make_move, Text(startswith='move'))
    dp.register_callback_query_handler(make_second_move, Text(startswith='krb'))
    

