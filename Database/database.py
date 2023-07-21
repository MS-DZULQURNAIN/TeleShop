import pymongo, os
from config import DATABASE_URI


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient["DzThumbnailBot"]


user_data = database['users']
prem_data = database ['prem']



async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({
      'first': first,
      'last': last,
      '_id': user_id,
      'username': username,
      'prem': False
    })
    return

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return

async def add_prem(user_id: int):
    prem_data.insert_one({'_id': user_id})
    return

async def del_prem(user_id: int):
    prem_data.delete_one({'_id': user_id})
    return

async def all_users():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

