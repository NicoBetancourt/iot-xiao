from src.infrastructure.utils.uuid import UniqueId
from src.infrastructure.db.driver.driver import MongoDBDriver

COLLECTION_NAME = 'users'


class UserMongoRepository:

    def __init__(self):
        self.driver = MongoDBDriver(COLLECTION_NAME)
        return None

    def create(self, item):
        new_item = item
        if '_id' in new_item:
            new_item['_id'] = UniqueId.get_uuid()
        res_item = self.driver.create(new_item)
        res_item = self.mapObjectToStr(res_item.inserted_id)
        return res_item

    def get_one(self, id):
        res = self.driver.get_one(id)
        res['_id'] = self.mapObjectToStr(res['_id'])
        return res
    
    def mapObjectToStr(self, item):
        return str(item)
