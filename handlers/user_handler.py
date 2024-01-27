from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon import standard_answer

rt = Router()

# Этот хэндлер сработает на команду /start
@rt.message(CommandStart())
async def process_start(message:Message):
    await message.answer(standard_answer['start'])

# Этот хэндлер сработает на команду /help
@rt.message(Command(commands='help'))
async def process_help(message:Message):
    await message.answer(standard_answer['help'])
