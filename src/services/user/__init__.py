# Use cases package
from src.services.user.create_user import CreateUser
from src.services.user.get_one_user import GetOneUser

# Repos
from src.domain.repositories.user_repo import UserRepository
from src.infrastructure.db.implementation.user_repository import UserMongoRepository

_info_repo = UserRepository(UserMongoRepository())

# Use cases
create_user = CreateUser(_info_repo).execute
get_user_by_id = GetOneUser(_info_repo).execute
# get_all_users = GetAllUsers(_info_repo).execute
# update_user = UpdateUser(_info_repo).execute
# delete_user = DeleteUser(_info_repo).execute
# load_users = LoadUsers(_info_repo).execute
