from src.infrastructure.web.routes import user_routes, product_list_routes
from fastapi import FastAPI

app = FastAPI()

try:

    app.include_router(user_routes.router, prefix="/users", tags=["users"])
    app.include_router(product_list_routes.router,
                       prefix="/products", tags=["products"])


except Exception as ex:
    print(f"Error al ejecutar la aplicación {ex}")
