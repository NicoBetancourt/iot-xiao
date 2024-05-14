from src.domain.repositories.user_repo import UserRepository


class CreateUser:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, user_data) -> str:
        res = self.user_repo.create(user_data.dict())
        return res
