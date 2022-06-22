import logging

from aiogram import executor, types

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    import bot

    executor.start_polling(
        bot.dp,
        allowed_updates=types.AllowedUpdates.all(),
        skip_updates=True,
    )
