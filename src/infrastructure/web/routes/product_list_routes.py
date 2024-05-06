from fastapi import APIRouter, Depends, HTTPException
from src.domain.entities.product_list import ProductList
from src.interface.controllers.product_list_controller import ProductListController

router = APIRouter()


@router.get("/")
def get_all_product_list():
    res =  ProductListController.get_all()
    return res

@router.get("/{id}")
def get_product_list(id: str):
    res =  ProductListController.get_by_id(id)
    return res

@router.post("/create/")
def create_product_list(item: ProductList):
    return ProductListController.create(item)

@router.put("/{id}")
def update_product_list(id: str, item: ProductList):
    return ProductListController.update(id, item)

@router.delete("/{id}")
def delete_product_list(id: str):
    return ProductListController.delete(id)
