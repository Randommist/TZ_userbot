from pyrogram import filters
from pyrogram.client import Client
from pyrogram.types import Message

from loader import app, worksheet
from utils import parse_ban_args, parse_check_args, parse_commnand, parse_phone_number


@app.on_message(filters.text)
async def handle(client: Client, message: Message):
    try:
        command, args = parse_commnand(message.text)
    except ValueError:
        return

    match command:
        case "check":
            phone_number = parse_phone_number(parse_check_args(args))
            if phone_number is None:
                await message.reply("Неверный номер")
                return
            ban_info = get_ban_info(phone_number)
            if ban_info:
                await message.reply(ban_info)
            else:
                await message.reply("Не найдено")
        case "ban":
            try:
                phone_text, ban_info_text = parse_ban_args(args)
            except ValueError:
                await message.reply("Неверные аргументы")
                return
            phone_number = parse_phone_number(phone_text)
            if phone_number is None:
                await message.reply("Неверный номер")
                return
            add_ban_info(phone_number, ban_info_text)
            await message.reply("Запись добавлена")


def get_ban_info(phone_number: str) -> str | None:
    cell = worksheet.find(phone_number, in_column=1)
    if cell:
        value = worksheet.cell(cell.row, 2).value
        if value:
            return value
        return "Информация отсутствует"
    return None


def add_ban_info(phone_number: str, ban_info: str):
    cell = worksheet.find(phone_number, in_column=1)
    if cell:  # Update ban info
        worksheet.update_cell(cell.row, 2, ban_info)
    else:  # Add ban info
        worksheet.append_row([phone_number, ban_info])


def main():
    app.run()


if __name__ == "__main__":
    main()
