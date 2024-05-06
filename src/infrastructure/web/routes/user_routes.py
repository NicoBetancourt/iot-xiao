from fastapi import APIRouter, Depends, HTTPException
from src.interface.controllers.user_controller import UserController
from src.domain.entities.user import User

router = APIRouter()


@router.get("/")
def get_users():
    return {"message": "Lista de usuarios"}


@router.get("/{user_id}")
def get_user(user_id: str):
    res = UserController.get_by_id(user_id)
    return {"message": f"Detalles del usuario con id {res}"}


@router.post("/create/")
def create_user(item: User):
    res = UserController.create(item)
    return {"message": "Usuario creado correctamente", "id": str(res.inserted_id)}


@router.put("/{user_id}")
def update_user(user_id: int, user: User):
    return {"message": f"Usuario con id {user_id} actualizado"}


@router.delete("/{user_id}")
def delete_user(user_id: int):
    return {"message": f"Usuario con id {user_id} eliminado"}


# # Operación para obtener todos los usuarios
# @router.get("/users/", response_model=List[User])
# async def get_users():
#     return list(database.values())

# # Operación para obtener un usuario por ID
# @router.get("/users/{user_id}", response_model=User)
# async def get_user(user_id: int):
#     if user_id not in database:
#         raise HTTPException(status_code=404, detail="Usuario no encontrado")
#     return database[user_id]

# # Operación para actualizar un usuario por ID
# @router.put("/users/{user_id}", response_model=User)
# async def update_user(user_id: int, user: User):
#     if user_id not in database:
#         raise HTTPException(status_code=404, detail="Usuario no encontrado")
#     database[user_id] = user
#     return user

# # Operación para eliminar un usuario por ID
# @router.delete("/users/{user_id}", response_model=User)
# async def delete_user(user_id: int):
#     if user_id not in database:
#         raise HTTPException(status_code=404, detail="Usuario no encontrado")
#     deleted_user = database.pop(user_id)
#     return deleted_user
