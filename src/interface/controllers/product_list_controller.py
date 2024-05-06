from src.domain.entities.product_list import ProductList
from src.interface.controllers.base_controller import BaseController
from src.application.use_cases.product_list import create_product, get_product_by_id, get_all_products, delete_product, update_product


class ProductListController(BaseController):

    @staticmethod
    def create(item):
        try:
            product_item = ProductList(**item.dict())
            res = create_product(product_item)
            response = {"message": "Producto creado correctamente", "id": str(res)}
            return response
        except Exception as ex:
            return {'Error message': str(ex)}

    @staticmethod
    def get_by_id(id):
        try:
            item = get_product_by_id(id)
            return item
        except Exception as ex:
            return {'Error message': str(ex)}

    @staticmethod
    def get_all(filter=None,options={}):
        try:
            item = get_all_products(filter,options)
            return item
        except Exception as ex:
            return {'Error message': str(ex)}

    @staticmethod
    def update(id, item):
        try:
            item = update_product(id, item)
            response = {"message": "Producto actualizado correctamente", "id": str(id)}
            return response
        except Exception as ex:
            return {'Error message': str(ex)}

    @staticmethod
    def delete(id):
        try:
            item = delete_product(id)
            response = {"message": "Producto eliminado correctamente", "id": str(id)}
            return response
        except Exception as ex:
            return {'Error message': str(ex)}
