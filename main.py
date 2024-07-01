from src.api import image_routes, product_list_routes
from src.api import user_routes
import socket
from fastapi import FastAPI

app = FastAPI()

try:
    app.include_router(user_routes.router, prefix="/users", tags=["users"])
    app.include_router(product_list_routes.router,
                       prefix="/products", tags=["products"])
    app.include_router(image_routes.router, prefix="/image", tags=["images"])
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")

except Exception as ex:
    print(f"Error al ejecutar la aplicación {ex}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)