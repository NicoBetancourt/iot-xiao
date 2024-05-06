from src.interface.controllers.base_controller import BaseController
# , get_all_songs, update_song, delete_song
from src.application.use_cases.user import create_user, get_user_by_id
from src.domain.entities.user import User


class UserController(BaseController):

    @staticmethod
    def create(user_data):
        try:
            user = User(**user_data.dict())
            response = create_user(user)
            return response
        except Exception as ex:
            return {'Error message': str(ex)}

    @staticmethod
    def get_by_id(user_id):
        try:
            user = get_user_by_id(user_id)
            return user
        except Exception as ex:
            return {'Error message': str(ex)}

    @staticmethod
    def get_all():
        return 'ok'
        # return get_all_users()

    @staticmethod
    def update(user_id, user_data):
        return 'ok'
        # return update_user(user_id, user_data)

    @staticmethod
    def delete(user_id):
        return 'ok'
        # return delekte_user(user_id)
