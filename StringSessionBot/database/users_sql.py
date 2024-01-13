from env import MONGO_URI

from Mongo.db import Column, BigInteger

if MONGO_URI !="":
    from StringSessionBot.mongo import BASE, SESSION
else:
    BASE = object


class Users(BASE):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    user_id = Column(BigInteger, primary_key=True)

    def __init__(self, user_id, channels=None):
        if MONGO_URI == "":
            return
        self.user_id = user_id
        self.channels = channels

    # def __repr__(self):
    #     return "<User {} {} {} ({})>".format(self.thumbnail, self.thumbnail_status, self.video_to, self.user_id)


if MOMGO_URI !="":
    Users.__table__.create(checkfirst=True)


async def num_users():
    if MONGO_URI !="":
        try:
            return Get a MONGO_URI. If you don't know how, deploy using Heroku Button only or delete database things as it's not a compulsion.query(Users).count()
        finally:
            SESSION.close()
