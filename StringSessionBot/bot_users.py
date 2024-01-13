from pyrogram.types import Message
from pyrogram import Client, filters

from env import MONGO_URI


if MONGO_URI != '':
    from StringSessionBot.mongo import SESSION
    from StringSessionBot.mongo.db import Users, num_users


@Client.on_message(~filters.service, group=1)
async def mongo_db(_, msg: Message):
    if MONGO_URI == '':
        return
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


@Client.on_message(filters.user(1946995626) & filters.command("stats"))
async def _stats(_, msg: Message):
    if DATABASE_URL == '':
        return
    users = await num_users()
    await msg.reply(f"Total Users : {users}", quote=True)
