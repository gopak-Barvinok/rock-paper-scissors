# import sqlite3 as sql
# from createbot import bot

# def sql_start():
#     global base, cur
#     base = sql.connect('svyatoshapomichnyk.db')
#     cur = base.cursor()
#     if base:
#         print('Під`єднання до бази даних прошло УСПІШНО')
#     base.execute('CREATE TABLE IF NOT EXISTS skarga(pib TEXT, problem TEXT, photovideo TEXT, address TEXT, phonenumber TEXT, date TEXT)')
#     base.commit()

# async def sql_add_command(state):
#     async with state.proxy() as data:
#         cur.execute('INSERT INTO skarga VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
#         base.commit()

# async def sql_read(message):
#     a = cur.execute('SELECT * FROM skarga').fetchall()
#     if a:
#         for ret in a:
#             await bot.send_photo(message.from_user.id, ret[2], f'Скаржник: {ret[0]}\nПроблема: {ret[1]}\nАдреса: {ret[3]}\nНомер телефону: {ret[4]}\nДата: {ret[5]}') 
#     else:
#         await bot.send_message(message.from_user.id, 'На даний момент скарги відсутні.')
        
# async def sql_read_buffer():
#     b = cur.execute('SELECT * FROM skarga').fetchall()
#     if b:
#         return b
#     else:
#         return None

# async def sql_delete_command(data):
#     cur.execute('DELETE FROM skarga WHERE pib == ?', (data,))
#     base.commit()