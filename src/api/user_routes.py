from fastapi import APIRouter, Depends, HTTPException
from src.domain.entities.user import User

# , get_all_songs, update_song, delete_song
from src.services.user import create_user, get_user_by_id
from src.domain.entities.user import User

router = APIRouter()


@router.get("/")
def get_users():
    return {"message": "Lista de usuarios"}


@router.get("/{user_id}")
def get_user(user_id: str):
    try:
        user = get_user_by_id(user_id)
        return {"message": f"Detalles del usuario con id {user}"}
    except Exception as ex:
        return {'Error message': str(ex)}


@router.post("/create/")
def create_user(item: User):
    try:
        user = User(**item.dict())
        response = create_user(user)
        return {"message": "Usuario creado correctamente", "id": str(response.inserted_id)}
    except Exception as ex:
        return {'Error message': str(ex)}


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
