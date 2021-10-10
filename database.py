from typing import Collection
from model import User
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient('mongodb+srv://dbUser:chula123@cluster0.nds32.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE')

database = client.UserList_Auth