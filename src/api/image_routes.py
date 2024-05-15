from src.domain.entities.image_entity import Image
from fastapi import APIRouter, Depends, HTTPException
from src.services.image import image_list

router = APIRouter()


@router.post("/")
def image_recognition(item:Image):
    try:
        response = image_list(item.url)
        return response
    except Exception as ex:
        return {'Error message': str(ex)}
