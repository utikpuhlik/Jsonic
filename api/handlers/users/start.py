from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Hi!\nWork in progress now")
    await message.reply(f"Your telegram is {message.from_user.id}")


@dp.message_handler(
    content_types=types.ContentTypes.DOCUMENT | types.ContentTypes.VIDEO | types.ContentTypes.PHOTO | types.ContentTypes.VIDEO_NOTE,
    user_id=[785145654])
async def content_gripper(message: types.Message):
    if message.content_type == 'document':
        await message.reply(message.document.file_id)
        await sleep(1.0)
    elif message.content_type == 'video':
        await message.reply(message.video.file_id)
        await sleep(1.0)
    elif message.content_type == 'photo':
        await message.reply(message.photo[0].file_id)
        await sleep(1.0)
    elif message.content_type == 'video_note':
        await message.reply(message.video_note.file_id)
        await sleep(1.0)
    else:
        await message.reply('Error. Unknown content type')
