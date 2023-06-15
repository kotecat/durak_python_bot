from aiogram import types
from textwrap import dedent
from loader import bot, dp, Commands


@dp.message_handler(commands=[Commands.SOURCE])
async def help_handler(message: types.Message):
    source = dedent("""Этот бот является копией бесплатного программного обеспечения. И находится под лицензией "<b>AGPL</b>".
<b>Оригинальный код доступен здесь:</b>
https://github.com/kotecat/durak_python_bot
Атрибуции:
<b>Draw" значок от:</b>
<a href="http://www.faithtoken.com/">Faithtoken</a>
<b>"Pass" значок от:</b>
<a href="http://delapouite.com/">Delapouite</a>
Оригиналы доступны на: http://game-icons.net
Иконки, отредактированные <b>ɳick</b>"

Разработка бота: <a href='tg://user?id=1956508438'>MrKoteyka</a>
Отдельная благодарность: <a href='tg://user?id=943441135'>Dimoka113</a>""")
    
    await message.answer(source, disable_web_page_preview=True)