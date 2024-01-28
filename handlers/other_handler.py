from aiogram import Router
from aiogram.types import Message
from lexicon import standard_answer


rt = Router()


@rt.message()
async def process_echo(message:Message):
    try:
        await message.send_copy(chat_id=message.from_user.id)
    except TypeError:
        await message.answer(standard_answer['no_echo'])