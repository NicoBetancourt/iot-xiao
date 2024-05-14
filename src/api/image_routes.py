from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.post("/")
def image_recognition(item:str):
    try:
        response = image_recognition(item)
        return response
    except Exception as ex:
        return {'Error message': str(ex)}
