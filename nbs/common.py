from decouple import config
from pyrogram import Client

client = Client("botlist-recommend", api_id=config("API_ID"), api_hash=config("API_HASH"), phone_number=config("PHONE"))

