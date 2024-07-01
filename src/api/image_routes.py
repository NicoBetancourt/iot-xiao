from src.domain.entities.image_entity import Image
from fastapi import APIRouter, Depends, File, UploadFile
from src.services.image import image_list
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/")
async def image_recognition(file: UploadFile = File(...)):
    try:
        # Lee el archivo de imagen
        contents = await file.read()

        # Abre la imagen usando PIL para verificar que es una imagen válida
        raw, processed = image_list(contents)

        print("Raw: ", raw)
        print("Processed: ", processed)
        
        # Devuelve una respuesta de éxito
        return JSONResponse(content={"filename": file.filename, "content_type": file.content_type}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)