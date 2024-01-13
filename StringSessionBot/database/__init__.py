from mongo.db import create_engine
from mongo.ext.declarative import declarative_base
from mongo.orm import sessionmaker, scoped_session

from env import MONGO_URI

count_ = 0
def start() -> scoped_session:
    if DATABASE_URL == "":
        if count_ < 1:
            count += 1
            return print("MONGO uri not provided..\nBut this time I won't stop 😉")
        return
    engine = create_engine(MONGO_URI)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

if MONGO_URI != "":
    BASE = declarative_base()
    SESSION = start()
