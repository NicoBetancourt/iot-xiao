from src.domain.repositories.user_repo import UserRepository
from src.domain.entities.user import User


class GetOneUser:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, id: str) -> User:
        res = self.user_repo.get_one(id)
        return res
