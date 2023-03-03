from asyncio import sleep
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from states import Mailing
from utils.mongodb import Mongo

database = Mongo()


@dp.message_handler(user_id=[785145654, 621767121, 896114308], commands=["all"])
async def mailing(message: types.Message):
    await message.answer("Введите текст сообщения:")
    await message.answer("*Чтобы покинуть меню рассылки введите «exit»")
    await Mailing.Text.set()


@dp.message_handler(state=Mailing.Text)
async def mailing(message: types.Message, state: FSMContext):
    text = message.text
    if text == "exit":
        await message.answer(f"Вы покинули меню рассылки")
        await state.finish()
    else:
        await message.answer(
            "Начинаю рассылку..\n\nНе отправляйте никаких сообщений, пока не увидите уведомление о "
            "завершенной рассылке!"
        )
        await state.finish()
        count_of_users = 0
        for user in await database.get_all_users():
            # user = user[0] deprecated SQL approach
            try:
                if user == message.from_user.id:
                    pass
                else:
                    await bot.send_message(chat_id=user, text=text)
                    await sleep(0.3)
                    count_of_users += 1
            except Exception:
                pass

        await message.answer(
            f"Рассылка выполнена успешно, сообщение было отправлено {count_of_users} пользователям"
        )
        await message.answer(
            "Чтобы создать новую рассылку воспользуйтесь командой /all"
        )
