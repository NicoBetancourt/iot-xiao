from src.infrastructure.db.driver.base_mongo_impl import BaseImplementation
from typing import List, Optional, TypeVar, Generic
from src.infrastructure.db.client import get_connection
from bson import ObjectId
from decouple import config

TDom = TypeVar('TDom')
FDom = TypeVar('FDom')
DB_NAME = config('DB_NAME')

class MongoDBDriver(BaseImplementation, Generic[TDom, FDom]):

    def __init__(self,collection_name:str):
        self.client =  get_connection()
        self.db = self.client[DB_NAME]
        self.collection = self.db[collection_name]

    def create(self, item: TDom) -> TDom:
        result = self.collection.insert_one(item)
        return result

    def update(self, id:str|ObjectId, item: TDom) -> Optional[TDom]:
        result = self.collection.update_one({'_id': ObjectId(id)}, {'$set': item})
        if result.raw_result['n'] > 0:
            return item
        else:
            return None

    def delete(self, id:str) -> bool:
        result = self.collection.delete_one({'_id': ObjectId(id)})
        return result.deleted_count > 0

    def get_all(self, filter:FDom, options):
        cursor = self.collection.find(filter, **options)
        return [doc for doc in cursor]

    def get_one(self, id:str|ObjectId) -> Optional[TDom]:
        return self.collection.find_one({'_id': ObjectId(id)})

    def count_registers(self, filter:FDom) -> int:
        return self.collection.count_documents(filter)

    def upsert_docs(self, query, items:TDom) -> TDom:
        result = self.collection.update_many(query, {'$set': items}, upsert=True)
        return items

    def create_many(self, items : List[TDom]) -> List[TDom]:
        result = self.collection.insert_many(items)
        return items


# class MongoDBDriver:
#     @classmethod
#     def get_connection(cls):
#         try:
#             client = MongoClient(config('MONGO_URI'))
#             return client
#         except Exception as e:
#             raise Exception(e)

#     @classmethod
#     def create(cls, collection_name, document):
#         try:
#             client = cls.get_connection()
#             db = client.get_database()
#             collection = db[collection_name]
#             result = collection.insert_one(document)
#             client.close()
#             return result.inserted_id
#         except Exception as e:
#             raise Exception(e)

#     @classmethod
#     def update(cls, collection_name, filter_query, update_query):
#         try:
#             client = cls.get_connection()
#             db = client.get_database()
#             collection = db[collection_name]
#             result = collection.update_many(filter_query, update_query)
#             client.close()
#             return result.modified_count
#         except Exception as e:
#             raise Exception(e)

#     @classmethod
#     def delete(cls, collection_name, query):
#         try:
#             client = cls.get_connection()
#             db = client.get_database()
#             collection = db[collection_name]
#             result = collection.delete_many(query)
#             client.close()
#             return result.deleted_count
#         except Exception as e:
#             raise Exception(e)

#     @classmethod
#     def get_one(cls, collection_name, query):
#         try:
#             client = cls.get_connection()
#             db = client.get_database()
#             collection = db[collection_name]
#             result = collection.find_one(query)
#             client.close()
#             return result
#         except Exception as e:
#             raise Exception(e)

#     @classmethod
#     def get_all(cls, collection_name, query=None):
#         try:
#             client = cls.get_connection()
#             db = client.get_database()
#             collection = db[collection_name]
#             if query:
#                 result = collection.find(query)
#             else:
#                 result = collection.find()
#             client.close()
#             return list(result)
#         except Exception as e:
#             raise Exception(e)
