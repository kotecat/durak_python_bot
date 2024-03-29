from aiogram import types
from textwrap import dedent
from loader import bot, dp, Commands


@dp.message_handler(commands=[Commands.HELP, Commands.START_BOT])
async def help_handler(message: types.Message):
    help = dedent(f"""<b>Следуйте этим шагам:</b>
1. Добавьте этого бота в группу

2. В группе начните новую игру с помощью /new или присоединитесь к уже существующей
запуск игры с /{Commands.JOIN}

3. После того, как присоединятся как минимум два игрока, начните игру с помощью
/{Commands.START}
4. Введите тег бота в окно чата и нажмите <b>пробел</b>. 
Вы увидите свои карточки (некоторые из них выделены серым цветом), 
любые дополнительные параметры, такие как взять карты, пасс и <b>?</b>, чтобы увидеть 
текущее состояние игры. <b>серые карты</b> - это те, которые
<b>невозможно кинуть</b> в данный момент. 
Коснитесь параметра, чтобы выполнить 
выбранное действие.
Игроки могут присоединиться к игре, только если игра не запущена.
Чтобы выйти из игры, используйте /{Commands.LEAVE}.

Используйте /notify_me, чтобы получать личное сообщение при запуске новой игры.


<b>Статистика:</b>
/stats - Посмотреть вашу статистику игр
/delstats - Удалить вашу статистику игр

<b>Другие команды (только создатель игры):</b>
/{Commands.KILL} - Завершить игру
/{Commands.KICK} - Выгнать игрока из игры 
(Ответом на сообщение пользователя)""")

    await message.answer(help)