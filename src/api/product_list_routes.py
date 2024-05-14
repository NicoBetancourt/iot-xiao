from fastapi import APIRouter, Depends, HTTPException
from src.domain.entities.product_list import ProductList
from src.services.product_list import create_product, get_product_by_id, get_all_products, delete_product, update_product


router = APIRouter()


@router.get("/")
def get_all_product_list(filter=None,options={}):
    try:
        item = get_all_products(filter,options)
        return item
    except Exception as ex:
        return {'Error message': str(ex)}

@router.get("/{id}")
def get_product_list(id: str):
    try:
        item = get_product_by_id(id)
        return item
    except Exception as ex:
        return {'Error message': str(ex)}

@router.post("/create/")
def create_product_list(item: ProductList):
    try:
        product_item = ProductList(**item.dict())
        res = create_product(product_item)
        response = {"message": "Producto creado correctamente", "id": str(res)}
        return response
    except Exception as ex:
        return {'Error message': str(ex)}

@router.put("/{id}")
def update_product_list(id: str, item: ProductList):
    try:
        item = update_product(id, item)
        response = {"message": "Producto actualizado correctamente", "id": str(id)}
        return response
    except Exception as ex:
        return {'Error message': str(ex)}

@router.delete("/{id}")
def delete_product_list(id: str):
    try:
        item = delete_product(id)
        response = {"message": "Producto eliminado correctamente", "id": str(id)}
        return response
    except Exception as ex:
        return {'Error message': str(ex)}