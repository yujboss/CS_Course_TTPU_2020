import asyncio

from data import config
from utils.db_api import quick_commands
from utils.db_api.db_gino import db


async def test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.create_all()

    stu = 'u11360'
    users = await quick_commands.select_all_users()
    [print(data) for data in users ]
loop = asyncio.get_event_loop()
loop.run_until_complete(test())