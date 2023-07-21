import pymongo, os
from DzThumbnailBot.config import DATABASE_URI


dbclient = pymongo.MongoClient(DATABASE_URI)
database = dbclient["DzThumbnailBot"]


user_data = database['users']



async def add_user(user_id: int):
    user_data.insert_one({
      'first': first,
      'last': last,
      '_id': user_id,
      'username': username,
      'prem': False,
      'ban': False
    })
    return

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return

async def prem(user_id: int):
    user_data.find_one({'_id': user_id}, {'$set': {'prem': True}})
    return

async def unprem(user_id: int):
    user_data.delete_one({'_id': user_id}, {'$set': {'prem': False}})
    return
