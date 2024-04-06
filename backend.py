from db import database
import random
import asyncio
from pyrogram import Client
from config import Config

DB = database()
api_id = Config.APP_ID
api_hash = Config.API_HASH

class App:
    async def add_user(self, GrobUser, inGrob, id, bot):
        account_list = DB.accounts()
        random.shuffle(account_list)
        numberMin = 40
        inGrob = inGrob.split("/")[3]
        for name in account_list:
            num = 0          
            for user in GrobUser:      
                try:
                    num += 1
                    GrobUser.remove(user)
                    async with Client("::memory::", api_id, api_hash, no_updates=True, in_memory=True, lang_code="ar", session_string=name) as app:
                        await asyncio.sleep(10)
                        try:
                            print(user)            
                            await app.add_chat_members(inGrob, user)                    
                        except Exception as e:
                            print(e)
                            if "FLOOD_WAIT_X" in str(e):
                                break
                except Exception as e:
                    print(e)

    async def get_user(self, GrobUser, Ingrob):
        administrators = []
        try:  
            account_list = DB.accounts()
            random.shuffle(account_list)
            GrobUser = GrobUser.split("/")[3]
            Ingrob = Ingrob.split("/")[3]       
            name = str("".join(random.choice(account_list) for i in range(1)))
            async with Client("::memory::", api_id, api_hash, no_updates=True, in_memory=True, lang_code="ar", session_string=name) as app:      
                await app.join_chat(Ingrob)
                async for m in app.get_chat_members(GrobUser):
                    try:
                        if m.user.username is not None:
                            administrators.append(m.user.username)
                    except Exception as e:
                        print(e)
                        pass
            print(administrators)
            return administrators
        except Exception as e:
            print(e)
