from src.domain.entities.user import User
from src.infrastructure.db.implementation.user_repository import UserMongoRepository


class UserRepository:
    def __init__(self, user_repo: UserMongoRepository):
        self.user_repo = user_repo

    def create(self, user:User) -> User:
        res = self.user_repo.create(user)
        return res
    
    def get_by_id(self, id:str) -> User:
        res = self.user_repo.get_one(id)
        return res
    
    def get_all(self):
        return 'Not Implemented'
    
    def update(self, id, item):
        return 'Not Implemented'
    
    def delete(self, id):
        return 'Not Implemented'
    