from aiogram.utils import executor
from createbot import dp
# from db import sql_db


async def startup(_):
    print("Бот вийшов в онлайн")
    # sql_db.sql_start()

from handlers import client, admin


if __name__ == '__main__':
    client.rhc(dp)
    admin.rhc(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=startup)


