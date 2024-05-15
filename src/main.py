from src.api import image_routes, product_list_routes
from src.api import user_routes
from fastapi import FastAPI

app = FastAPI()

try:

    app.include_router(user_routes.router, prefix="/users", tags=["users"])
    app.include_router(product_list_routes.router,
                       prefix="/products", tags=["products"])
    app.include_router(image_routes.router, prefix="/image", tags=["images"])


except Exception as ex:
    print(f"Error al ejecutar la aplicación {ex}")
