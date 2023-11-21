from ..objects import Game
from aiogram.types import User, Chat
from aiogram import Bot
from config import Config


def user_is_creator(user: User, game: Game):
    return user.id == game.creator.id


def user_is_bot_admin(user: User):
    return user.id in Config.ADMINS


async def user_is_admin(user: User, chat: Chat):
    return user.id in (await get_admin_ids(chat.id))


async def user_is_creator_or_admin(user: User, game: Game, chat: Chat):
    return user_is_creator(user, game) or user_is_bot_admin(user) or (await user_is_admin(user, chat))


async def get_admin_ids(chat_id: int):
    """Returns a list of admin IDs for a given chat."""
    bot = Bot.get_current()
    chat_admins = await bot.get_chat_administrators(chat_id)
    return [admin.user.id for admin in chat_admins]