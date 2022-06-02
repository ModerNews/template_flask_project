import pymysql
import os
from dotenv import load_dotenv
from pydantic import BaseModel, BaseConfig
from typing import Type

load_dotenv()


def from_tuple(model: Type['DatabaseModel'], data):
    temp = enumerate(model.__fields__.keys())
    if data is None:
        return None
    return model(**{key: data[i] for i, key in temp})


class DatabaseModel(BaseModel):
    class Config:
        orm_mode = True


class DatabaseUser(DatabaseModel):
    id: int
    username: str
    password: str
    email: str
    verified: bool


class DbHandler:
    def __int__(self):
        self.connection: pymysql.Connection = pymysql.connect(host=os.getenv("db_host"),
                                                               port=int(os.getenv("db_port")),
                                                               user=os.getenv("db_user"),
                                                               password=os.getenv("db_passwd"),
                                                               database=os.getenv("db_schema"))

    def get_users(self, limit=100):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM USERS LIMIT %s", limit)
            return [DatabaseUser(id=data[0], username=data[1], password=data[2], email=data[3], verified=data[4]) for data in cursor.fetchall()]
            # return [from_tuple(DatabaseUser, data) for data in cursor.fetchall()]

    def get_user_by_email(self, email: str):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM USERS WHERE email = %s", email)
            return from_tuple(DatabaseUser, cursor.fetchone())

    def get_user_by_username(self, username: str):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM USERS WHERE username = %s", username)
            return from_tuple(DatabaseUser, cursor.fetchone())