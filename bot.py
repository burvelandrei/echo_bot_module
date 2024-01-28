import asyncio
from aiogram import Bot, Dispatcher
from handlers import user_handler, other_handler
from config import Config, load_config


async def main():
    config:Config = load_config()
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(user_handler.rt)
    dp.include_router(other_handler.rt)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())