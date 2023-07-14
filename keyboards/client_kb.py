from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


button_par = InlineKeyboardMarkup(row_width=1)


#Кнопки старта игры
button_quick_game = InlineKeyboardButton(text='Быстрая игра', callback_data='quick_game')
button_PM = InlineKeyboardButton(text='Перейти в лс', url='https://t.me/RockPaperScissors01Bot')
button_VQR_game = InlineKeyboardButton(text='Играть на VQR', callback_data='vqr_game')

button_par.add(button_PM).add(button_quick_game).add(button_VQR_game)

#Кнопки быстрой игры
button_move = InlineKeyboardMarkup(row_width=2)

button_kamen = InlineKeyboardButton(text='Камень', callback_data='move_stone')
button_nozhnicy = InlineKeyboardButton(text='Ножницы', callback_data='move_scissors')
button_bumaga = InlineKeyboardButton(text='Бумага', callback_data='move_paper')
button_kolodec = InlineKeyboardButton(text='Колодец', callback_data='move_well')

button_move.add(button_kamen, button_bumaga, button_nozhnicy, button_kolodec)

button_move2 = InlineKeyboardMarkup(row_width=2)

button_kamen2 = InlineKeyboardButton(text='Камень2', callback_data='krb_stone')
button_nozhnicy2 = InlineKeyboardButton(text='Ножницы2', callback_data='krb_scissors')
button_bumaga2 = InlineKeyboardButton(text='Бумага2', callback_data='krb_paper')
button_kolodec2 = InlineKeyboardButton(text='Колодец2', callback_data='krb_well')

button_move2.add(button_kamen2, button_bumaga2, button_nozhnicy2, button_kolodec2)