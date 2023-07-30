from aiogram import types
from db import UserSetting, session
from loader import bot, dp, Commands


@dp.message_handler(commands=[Commands.STATS])
async def my_stats_handler(message: types.Message):
    user = types.User.get_current()
    
    with session as s:
        us = UserSetting.get(id=user.id)
        if not us:
            us = UserSetting(id=user.id)

    stat_status = "✅" if us.stats else "❌"
    
    f"{stat_status} <b>Ваша статистика:</b>\n"

    p = round((us.first_places / us.games_played) * 100) if us.games_played else 0
    
    await message.answer(f"<u>{stat_status} <b>Ваша статистика:</b></u>\n"
                         f"- Победы: {us.first_places} / {us.games_played}   ({p}%)\n"
                         f"- Кол-во атак: {us.cards_played}\n"
                         f"- Кол-во защит: {us.cards_beaten}")
    

@dp.message_handler(commands=[Commands.OFF_STATS])
async def off_stats_handler(message: types.Message):
    user = types.User.get_current()
    
    with session as s:
        us = UserSetting.get(id=user.id)
        if not us:
            us = UserSetting(id=user.id)

        us.stats = False
        
    await message.answer(f"<b>Сбор статистики приостановлен!</b>\n<i>Возобновить</i> - /{Commands.ON_STATS}")
    
    
@dp.message_handler(commands=[Commands.ON_STATS])
async def on_stats_handler(message: types.Message):
    user = types.User.get_current()
    
    with session as s:
        us = UserSetting.get(id=user.id)
        if not us:
            us = UserSetting(id=user.id)
        
        us.stats = True
        
    await message.answer(f"<b>Сбор статистики возобновлён!</b>\n<i>Приостановить</i> - /{Commands.OFF_STATS}")